#!/usr/bin/env python3
# coding=utf-8
"""A simple example demonstrating the following:
    1) DEMONSTRABLE ITEMS
"""
import sys
from pathlib import Path

from cmd2 import Cmd, Settable, Statement
from loguru import logger

from command_sets.audio import Audio_CS
from command_sets.merge import Merge_CS
from command_sets.video import Video_CS
from common.banner import get_banner
from common.log_helper import exception_logger


def configure_logger():
    logger.remove()
    logger.add("file_1.log", rotation="5 MB")
    logger.add("file.ser.log", serialize=True)


class BasicApp(Cmd):
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

    @exception_logger
    def do_simple(self, _: Statement):
        """simple stuff"""

    def _log_debug(self, message: str) -> None:
        if self.debug:
            logger.debug(message)


if __name__ == "__main__":

    configure_logger()
    logger.info("Start of application")

    # Load command sets manually
    try:

        cs = [Audio_CS(), Merge_CS(), Video_CS()]
        logger.debug(f"Command Sets: {cs}")

        app = BasicApp(command_sets=cs, auto_load_commands=False)
        logger.info("Cmd App Created")

        app.cmdloop()
        logger.info("Exited Command Loop gracefully")

    except Exception:
        logger.opt(exception=True).critical("Application has crashed")
        print("Application shutdown unexpectantly")
        sys.exit(-1)

    logger.info("Application shutdown complete")
    sys.exit()
