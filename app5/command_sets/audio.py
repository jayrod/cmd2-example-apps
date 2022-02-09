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
class Audio_CS(CommandSet):
    def __init__(self):

        logger.info(f"Initializing {self.__class__.__name__}")
        super().__init__()

    def _codec_choices_provider(self) -> List[str]:
        return [".mp3", ".wav", ".aac"]

    arg_parser = Cmd2ArgumentParser()
    arg_parser.add_argument(
        "codec",
        choices_provider=_codec_choices_provider,
        help="Type of audio codec to use",
    )

    @exception_logger(logger)
    @with_argparser(arg_parser)
    def do_rip_audio(self, parms: Statement):
        """Rips audio from DVD"""

        # Get DVD drive info
        dvd_drive = self._cmd.dvd_drive
        self._cmd._log_debug(f"DVD Drive: {dvd_drive}")

        # Rip audio
        self._cmd.poutput(f"Ripping audio from {dvd_drive}")
        audio_file = Path(rand_file(parms.codec).name)

        # Create audio job object
        audio_job = AudioJob(dvd_drive, parms.codec, audio_file)
        self._cmd.poutput(f"Results located @ {audio_file}")
        logger.info(f"Executed audio rip command")

        # Save last result and log
        self._cmd.last_result = audio_job
        self._cmd._log_debug(audio_job)
