from dataclasses import dataclass
from pathlib import Path
from typing import List

from cmd2 import (
    Cmd2ArgumentParser,
    CommandSet,
    Statement,
    with_argparser,
    with_default_category,
)
from loguru import logger

from common.helper import rand_file
from common.log_helper import exception_logger


@dataclass
class AudioJob:
    dvd_drive: str
    codec: str
    output_file: Path


@with_default_category("Ripper")
class Video_CS(CommandSet):
    def __init__(self):

        super().__init__()
        logger.info(f"Initializing {self.__class__.__name__}")

    def _codec_choices_provider(self) -> List[str]:
        return [".mkv", ".wmv", ".avi"]

    arg_parser = Cmd2ArgumentParser()
    arg_parser.add_argument(
        "codec",
        choices_provider=_codec_choices_provider,
        help="Type of video codec to use",
    )

    @with_argparser(arg_parser)
    @exception_logger(logger)
    def do_rip_video(self, parms: Statement):
        """Rips video from DVD"""

        # Get DVD drive info
        dvd_drive = self._cmd.dvd_drive
        self._cmd._log_debug(f"DVD Drive: {dvd_drive}")

        # Rip audio
        self._cmd.poutput(f"Ripping video from {dvd_drive}")
        video_file = Path(rand_file(parms.codec).name)

        # Create audio job object
        video_job = AudioJob(dvd_drive, parms.codec, video_file)
        self._cmd.poutput(f"Results located @ {video_file}")
        logger.info(f"Executed video rip command")

        # Save last result and log
        self._cmd.last_result = video_job
        self._cmd._log_debug(video_job)
