#  Asynchronus Alerts
A Minimal example demonstrating the following:

1) Cmd2 Thread registration
2) CommandSet interaction with main application instance.

This example app is based on the [async printing](https://github.com/python-cmd2/cmd2/blob/master/examples/async_printing.py) cmd2 example. 

## Application Design

The important features of this application reside in the `BasicApp.__init__()` function. First a class instance variable called `alert_queue` is created. This is the thread safe object to hold alerts generated by the user via `add_alert` commands. The `_stop_event` and `_alerter_thread` are thread instance variables. Finally the calls to `register_preloop_hook` and `register_postloop_hook` are responsible for save execution and shutdown of the alerter thread.

The `_alerter_thread_func` contains the thread logic which in a loop every 10 seconds pulls alerts from the alert_queue and `async_alert` prints them. When printing in this fashion it is advisable to acquire a terminal lock and not block other calls. By using

```python
self.terminal_lock.acquire(blocking=False)
```

[see also](https://cmd2.readthedocs.io/en/stable/features/prompt.html?highlight=terminal_lock#asynchronous-feedback)


## Caveats

In the sub_command.py file we access the global cmd2 alert queue using the `self._cmd2` reference. This technque will
be repeated frequently when using `CommandSet` organization.

```python
 self._cmd.alert_queue.put(parms.alert_text[::-1])
```

## Requirements

* python >= 3.7
* cmd2 >= 2.3.3