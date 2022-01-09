#  Asynchronus Alerts
A Minimal example demonstrating the following:

1) Cmd2 Thread registration
2) CommandSets


## Caveats

In the sub_command.py file we access the global cmd2 alert queue using the `self._cmd2` reference. This technque will
be repeated frequently when using `CommandSet` organization.

```python
 self._cmd.alert_queue.put(parms.alert_text[::-1])
```