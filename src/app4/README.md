#  Persistent File Command History
Application showcasing persistent command file history

## Features of this application

1) How to pass in external variables to cmd2 instance.
2) Use of XDG library for platform independent path abstraction
3) Simple app specific persistent command history
4) Parameter tab completion based on history

## Application Design

This application was created to show off the levels of history and tab completion that can be achieved. The application relies on the xdg pypi library and [XDG Spec](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html) for platform generic storage (See caveats below). 

The first thing that should be noted is the inclusion of a generic `AppFileManager` object during app initialization.

```python

   # Create application file manager object
    app_man = AppFileManager(__app_name__)
```

This object handles references to where the persistent history file should be stored and created.

```python
    ...
    self.hist_file = XDG_DATA_HOME.joinpath(self.app_name, "persistent_history.cmd2")
    ...

```

This `AppFileManager` is passed into the `cmd2` app instance.

```python

    # Create history and cache directories
    app_man.create_hist_dir()

    app = BasicApp(application_manager=app_man)
    app.cmdloop()
```

And then readily accessed from within the main cmd2 application, for eventual passage to the parent class via the super() call.

```python

class BasicApp(Cmd):
    def __init__(self, **kwargs):
        self.app_man = kwargs.get("application_manager")

        hist_file = self.app_man.hist_file
        super().__init__(
            persistent_history_file=hist_file, persistent_history_length=500, allow_cli_args=False
        )
```

This results in readline level persistent history of commands accessible by the user pressing up and down arrows as well as <ctrl-r> key maps. We however would like to go a step further. 

This application exposes two commands `curl` and `snap_shot`. Ostensibly one command would performa  curl on a website and the snapshot would be responsible for creating a thumbnail of the site. It would be tedious to have to type in a long url more than once so we will create a `url_cache` object to parse persistent history and provide the user with helpful command parameter hints. 

The following `app.py' code creates and initializes the url cache based on history.

```python
# Create a cache object to save url information to
self._url_cache: List = self._get_urls_from_history()

def _get_urls_from_history(self) -> List[str]:

    return [
        h.statement.args for h in self.history if h.statement.command in ["curl", "snap_shot"]
        ]
```

Finally the website `cmd2.CommandSet` performs three things to make this magic happen.

1) 

Creates a function responsible for retrieving urls from the cmd2.app space

```python
    def _add_url_to_cache(self, url: str) -> None:
          if url not in self._cmd._url_cache:
            self._cmd._url_cache.append(url)
```

2) 

Adds a choices provider to each command

```python
    ...
    curl_parser.add_argument(
        "url", choices_provider=_url_choices_provider, help="URL to perform curl on"
    )
    ...
```

3) 

Finally after each command invocation a url is saved to the cache if it is new.

```python
    def _add_url_to_cache(self, url: str) -> None:
        if url not in self._cmd._url_cache:
            self._cmd._url_cache.append(url)

    ...

    def do_snap_shot(self, parms: Statement):
        ...
        # Add new url to cache for further usage
        self._add_url_to_cache(parms.url)
```

This produces a fairly seamless transition of urls being saved and reused between commands through tab completion.

## Caveats
The persistent history file is set to contain only 500 items. This is rather small and the url history
is parsing a subset of history one time at cmd2 app initialization. It should be noted that if the history
file were to grow rather large then it can be assumed that the application may take some time to load each time.
This may not be acceptable and perhaps a more robust threaded option should be adopted.

The xdg library provides a fairly robust platform independent set of folder descriptions but does not guaruntee all folders are available and already created on each platform.

## Requirements

* attrs==21.4.0
* cmd2==2.3.3
* pyperclip==1.8.2
* wcwidth==0.2.5
* xdg==5.1.1