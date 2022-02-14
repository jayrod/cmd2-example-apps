#!/usr/bin/env python3
# coding=utf-8
"""A simple example demonstrating the following:
    1) Use of loguru library 
    2) Use of intro banner
    3) Automatic logging of commands via decorator
    4) Using dataclasses for command results
    5) Command completion using simple choices provider  
"""
import sys
from pathlib import Path

from cmd2 import Cmd, Settable, Statement
from loguru import logger
from xdg import XDG_CACHE_HOME

from app5.command_sets.audio import Audio_CS
from app5.command_sets.merge import Merge_CS
from app5.command_sets.video import Video_CS
from app5.common.banner import get_banner
from app5.common.log_helper import exception_logger


def configure_logger():

    # Remove default logger that prints to stdout
    logger.remove()

    # Consistent path to log files
    log_file = Path(XDG_CACHE_HOME).joinpath('App5', 'run.log')
    
    # if it doesn't exist then create it
    log_file.parent.mkdir(parents=True, exist_ok=True)

    # Log all out put to log file 
    logger.add(log_file, rotation="5 MB")


class App(Cmd):

    def __init__(self, *args, **kwargs):
        logger.info(f"Initializing {self.__class__.__name__}")

        super().__init__(*args, **kwargs)
        logger.debug(f"Loaded Command Sets: {self._installed_command_sets}")

        # Set intro
        self.intro = get_banner()

        # Add setting to point to DVD Drive
        self.dvd_drive: str = "D"
        self.add_settable(Settable("dvd_drive", str, "Drive letter for DVD device", self))

        # Add path output folder
        self.output_folder: Path = Path("/tmp")
        self.add_settable(
            Settable("output_folder", Path, "Output folder to save ripped DVDs", self)
        )

    def _log_debug(self, message: str) -> None:
        if self.debug:
            logger.debug(message)

def main():

    configure_logger()
    logger.info("Start of application")

    # Load command sets manually
    try:

        cs = [Audio_CS(), Merge_CS(), Video_CS()]
        logger.debug(f"Command Sets: {cs}")

        app = App(command_sets=cs, auto_load_commands=False)
        logger.info("Cmd App Created")

        app.cmdloop()
        logger.info("Exited Command Loop gracefully")

    except Exception:
        logger.opt(exception=True).critical("Application has crashed")
        print("Application shutdown unexpectantly")
        sys.exit(-1)

    logger.info("Application shutdown complete")
    return 0

if __name__ == "__main__":
    sys.exit(main())
