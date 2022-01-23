#!/usr/bin/env python3
# coding=utf-8
"""A simple example demonstrating the following:
    1) How to add a command
"""
import threading
from queue import Queue
from typing import List

from cmd2 import Cmd, Cmd2ArgumentParser, CommandSet, Statement, with_argparser
from command_sets import *


class BasicApp(Cmd):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = BasicApp()
    app.cmdloop()
