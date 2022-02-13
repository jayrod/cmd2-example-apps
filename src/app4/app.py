#!/usr/bin/env python3
# coding=utf-8
"""A simple example demonstrating the following:
    1) How to pass in external variables to cmd2 instance.
    2) Use of XDG library for platform independent path abstraction
    3) Simple app specific persistent command history
    4) Parameter tab completion based on history
"""

from typing import List

from cmd2 import Cmd, Statement

from app4.command_sets import *
from app4.common.utils import AppFileManager

__app_name__ = "App4"


class App(Cmd):
    def __init__(self, **kwargs):
        """Basic cmd2 application
        kwargs contains a passed in custom variable
        """
        # Get application manager object passed in
        self.app_man = kwargs.get("application_manager")

        hist_file = self.app_man.hist_file

        super().__init__(
            persistent_history_file=hist_file, persistent_history_length=500, allow_cli_args=False
        )

        # Create a cache object to save url information to
        self._url_cache: List = self._get_urls_from_history()

    def _get_urls_from_history(self) -> List[str]:
        """Returns urls from history collection

        Returns:
            List[str]: List of urls gathered from history collection.
        """

        return [
            h.statement.args for h in self.history if h.statement.command in ["curl", "snap_shot"]
        ]


def main():


    # Create application file manager object
    app_man = AppFileManager(__app_name__)

    # Create history and cache directories
    app_man.create_hist_dir()
    app = App(application_manager=app_man)
    app.cmdloop()

if __name__ == "__main__":
    main()
