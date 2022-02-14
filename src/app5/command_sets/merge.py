from app5.common.log_helper import exception_logger
from cmd2 import CommandSet, Statement, with_default_category
from loguru import logger


@with_default_category("Ripper")
class Merge_CS(CommandSet):
    def __init__(self):

        logger.info(f"Initializing {self.__class__.__name__}")
        super().__init__()

    @exception_logger
    def do_merge(self, _: Statement):
        """Merging audio and video"""
        self._cmd.poutput("Merged everything")
        logger.info(f"Finished merge")
