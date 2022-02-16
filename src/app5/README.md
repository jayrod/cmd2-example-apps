#  Logging
Logging example

## Features of this application
1) Use of loguru library 
2) Use of intro banner
3) Automatic logging of commands via decorator
4) Using dataclasses for command results
5) Command completion using simple choices provider  

## Application Design

This sample application introduces a few simple cmd2 features and attempts an intermediate to advanced technique to make logging automatic for decorated commands. We rely on the easy use of the [loguru](https://github.com/Delgan/loguru) library. This fictional application is meant to simulate the good old days of ripping content from DVD's for electronic storage. There were a number of tools required at the time that did many different small parts of the process. One item would rip video, another audio and finally a tool that would bring both parts back together to create a whole. 

The application has three command sets each with one simple command. The main focus of this example was to illustrate application logging and the nuances of creating function decorators for cmd2 applications. 


## Application Walk-through

We start by simply importing and configuring the loguru library. 

```python
from loguru import logger
...
from common.log_helper import exception_logger

def configure_logger():
    logger.remove()
    logger.add("file_1.log", rotation="5 MB")
```

The configure logger function is called during main application start at the very beginning and annotates the cmd2 bootstrap process writing logs before and after the `cmd2.cmdloop()` function. This is helpful to see audit trails of start and end of application. This would be a good time to capture platform and user information for usage statistics. 

There is a large try except structure around the command loop there to log any application crash stack traces. This is a last ditch effort to capture information about a critical failure. 


Custom command completion in cmd2 can not be understated as to its ease and power as evidenced by the below snippet. 

```python
     def _codec_choices_provider(self) -> List[str]:
        return [".mkv", ".wmv", ".avi"]

    arg_parser = Cmd2ArgumentParser()
    arg_parser.add_argument(
        "codec",
        choices_provider=_codec_choices_provider,
        help="Type of video codec to use",
    )

    @exception_logger
    @with_argparser(arg_parser)
    def do_rip_video(self, parms: Statement):
        """Rips video from DVD"""
...
```

With a few lines of code we have created a rip_video command with one parameter that has three custom command completion arguments. 

We should note here that this command also sports a custom (but poorly named) exception_logger decorator that automatically logs informational information about each command. I attempted to catch any exceptions resulting from any function call but that proved to be a bit more complicated due to the way cmd2 handles and re throws exceptions. I will leave this endeavor up to those far smarter than I or possessing more *free* time. 

By creating the decorator a log file is created with the following data.

```
2022-02-10 00:39:50.152 | INFO     | common.log_helper:do_rip_video:19 - Command: rip_video
2022-02-10 00:39:50.154 | DEBUG    | common.log_helper:do_rip_video:22 - Statement arguments: ['.aac']
2022-02-10 00:39:50.156 | DEBUG    | common.log_helper:do_rip_video:34 - Last Result: AudioJob(dvd_drive='D', codec='.aac', output_file=PosixPath('/var/folders/y6/fh8w8ykx6d75865zmjbh9mvm0000gn/T/tmpa8rjf8f7.aac'))
```

After some initial floundering I used the [cmd2 plugin tempalte](https://github.com/python-cmd2/cmd2-plugin-template/blob/master/cmd2_myplugin/myplugin.py) as a starting point and was infinitely more successful. Long story short, make use `functools.wraps`. 

Our goal is to log the *State* of the cmd2 application during a given command execution. To that end we wish to know which function was called, the arguments that were passed in and any results thereof.  

```python

def exception_logger(func: Callable) -> Callable:
    """A logger decorator"""

    @wraps(func)
    def _empty_decorator(self, *args, **kwargs):

        # Get statements from args
        statements = [i for i in args if hasattr(i, "command") if hasattr(i, "arg_list")]
```

Continuing with the example above lets suppose the `rip_video` command was executed and our decorator goes into action. The `func` parameter passed into `exception_logger` is the `do_rip_video` function. The `self` passed to the inner function is the `cmd2` application or `CommandSet` while the `*args` parameter is a Tuple containing `cmd2.Statement` objects. This is all of the information we need. 

In the last line of the example above we cycle through all of the items in args and pull out things that [quack](https://en.wikipedia.org/wiki/Duck_typing) like a `cmd2.Statement` object. From here we can cycle through all of the Statements and log information.

```python
...
        for statement in statements:
            # Patch the logger so that it appears to come from the called function
            logger.patch(lambda r: r.update(function=func.__name__)).info(
                f"Command: {statement.command}"
...
```
The `logger.patch` function is a bit of loguru ninja black magic that insures that log messages appear to originate from the wrapped function and not from `_empty_decorator`. After a bit of inspection and debugging it is trivial to locate the command issued along with the arguments given. 

Locating the last result was a bit trickier due to use of CommandSets.

```python
        ...
        func(self, *args, **kwargs)

        # save last result if available
        if issubclass(type(self), CommandSet):
            lr = self._cmd.last_result
        if issubclass(type(self), Cmd):
            lr = self.last_result
```

The above locates a last_result object based on what type of object self is. It could either be a cmd2 object or a CommandSet. Depending on its value we locate the last_result variable for logging. 

While this decorator is a bit complicated it cuts down drastically how much time and effort a developer must use in order to get basic logging and telemetry from their program.

## Caveats

* There is a slight differentiation between cmd2 argument options `choices_provider` and `choices`. The later is more restrictive and in the example application not enough detail is given to make sure that parameters NOT known are handled. 
* Be careful to make sure that `self.last_result` is being set and un set appropriately. If a command does not assign value to the variable then the last command to do so will persist. 

## Requirements

* python >= 3.7
* cmd2 >= 2.3.3
* loguru==0.6.0
* xdg