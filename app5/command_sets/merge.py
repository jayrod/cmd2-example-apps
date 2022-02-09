from cmd2 import CommandSet, Statement, with_default_category
from loguru import logger

from common.log_helper import exception_logger


@with_default_category("Ripper")
class Merge_CS(CommandSet):
    def __init__(self):

        logger.info(f"Initializing {self.__class__.__name__}")
        super().__init__()

    def do_merge(self, _: Statement):
        """Merging audio and video"""

        logger.info(f"Finished merge")
