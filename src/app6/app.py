#!/usr/bin/env python3
# coding=utf-8
"""A simple example demonstrating the following:
    1) CommandSet organization
    2) Use of dataclasses for readability
    3) Simple custom tab completion
    4) Conditional tab completion
    5) Ansi coloring of output
"""

from cmd2 import Cmd

from app6.command_sets import *


class App(Cmd):
    def __init__(self):
        super().__init__()

def main():

    app = App()
    app.cmdloop()

if __name__ == "__main__":
    main()
