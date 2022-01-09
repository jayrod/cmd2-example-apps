#!/usr/bin/env python3
# coding=utf-8
"""A simple example demonstrating the following:
    1) How to add a command
    2) How to add help for that command
    3) Persistent history
    4) How to run an initialization script at startup
    5) How to add custom command aliases using the alias command
    6) Shell-like capabilities
"""
from typing import List
import cmd2
from cmd2 import (
    Bg,
    Fg,
    style,
    Cmd2ArgumentParser,
    with_argparser,
)
from cmd2 import CommandSet

import threading
from queue import Queue
from sub_command import TestCS


class BasicApp(cmd2.Cmd):

    def __init__(self):
        super().__init__(
            persistent_history_file='cmd2_history.dat',
            include_ipy=True,
        )

        # Alert Queue
        self.alert_queue = Queue()
        
        # The thread that will asynchronously alert the user of events
        self._stop_event = threading.Event()
        self._alerter_thread = threading.Thread()

        # Create some hooks to handle the starting and stopping of our thread
        self.register_preloop_hook(self._preloop_hook)
        self.register_postloop_hook(self._postloop_hook)

    def _preloop_hook(self) -> None:
        """Start the alerter thread"""
        # This runs after cmdloop() acquires self.terminal_lock, which will be locked until the prompt appears.
        # Therefore this is the best place to start the alerter thread since there is no risk of it alerting
        # before the prompt is displayed. You can also start it via a command if its not something that should
        # be running during the entire application. See do_start_alerts().
        self._stop_event.clear()

        self._alerter_thread = threading.Thread(name='alerter', target=self._alerter_thread_func)
        self._alerter_thread.start()

    def _postloop_hook(self) -> None:
        """Stops the alerter thread"""

        # After this function returns, cmdloop() releases self.terminal_lock which could make the alerter
        # thread think the prompt is on screen. Therefore this is the best place to stop the alerter thread.
        # You can also stop it via a command. See do_stop_alerts().
        self._stop_event.set()
        if self._alerter_thread.is_alive():
            self._alerter_thread.join()

    def _get_all_alerts(self) -> List[str]:
        alerts = []
        while not self.alert_queue.empty():
            alerts.append(self.alert_queue.get())

        return alerts

    def _alerter_thread_func(self) -> None:
        """Prints alerts and updates the prompt any time the prompt is showing"""

        while not self._stop_event.is_set():
            # Always acquire terminal_lock before printing alerts or updating the prompt
            # To keep the app responsive, do not block on this call
            if self.terminal_lock.acquire(blocking=False):
                
                # print all alerts in the queue
                alerts = self._get_all_alerts()
                if alerts:
                    [self.async_alert(alert) for alert in alerts]

                # Don't forget to release the lock
                self.terminal_lock.release()

            self._stop_event.wait(10)


    def do_intro(self, _):
        """Display the intro banner"""
        self.poutput(self.intro)

    parser = Cmd2ArgumentParser()
    parser.add_argument('alert_text', help='Alert text')

    @with_argparser(parser)
    def do_add_alert(self, parms: cmd2.Statement):
        self.alert_queue.put(parms.alert_text)

if __name__ == '__main__':
    app = BasicApp()
    app.cmdloop()