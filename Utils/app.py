#!/usr/bin/env python3
# coding=utf-8
"""Application used in helping to create other example apps
"""

from cmd2 import Cmd


class BasicApp(Cmd):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = BasicApp()
    app.cmdloop()
