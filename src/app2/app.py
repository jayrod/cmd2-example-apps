#!/usr/bin/env python
# coding=utf-8
"""
A simple application using cmd2  and rich console

"""

import argparse
from queue import Queue
from random import choice
from threading import Event, Thread
from time import sleep

from cmd2 import Cmd
from RandomWordGenerator import RandomWord

from .first import FirstCommandSet


class App(Cmd):
    def __init__(self):
        super().__init__()

        # Active job queue
        self.active = Queue()

        # Completed job queue
        self.completed = Queue()

        # Register pre and post hooks
        self.register_preloop_hook(self._preloop_hook)
        self.register_postloop_hook(self._postloop_hook)

        # globals
        self.stop_event = Event()
        self.sim_thread = Thread()

    def sim_jobs(self, active: Queue, completed: Queue, stop_event: Event):

        while not stop_event.is_set():

            # Add a new job
            def add():
                rw = RandomWord()
                active.put(rw.generate())

            # Complete job
            def complete():
                if not active.empty():
                    completed.put(active.get())

            # remove an item from completed
            def remove():
                if not completed.empty():
                    completed.get()

            # do Nothing
            def nothing():
                sleep(1)

            all_choices = [add, complete, remove, nothing]

            choice(all_choices)()

            sleep(1)

    def _preloop_hook(self) -> None:

        # Event object
        self.stop_event.clear()

        # Create simulation thread
        self.sim_thread = Thread(
            name="sim_thread",
            target=self.sim_jobs,
            args=(self.active, self.completed, self.stop_event),
        )

        # Start sim thread
        self.sim_thread.start()

    def _postloop_hook(self) -> None:

        self.stop_event.set()
        self.sim_thread.join()


def main():

    c = App()
    c.cmdloop()

if __name__ == "__main__":
    main()
