from loguru import logger

from command_sets.audio import Audio_CS
from command_sets.merge import Merge_CS
from command_sets.video import Video_CS

__all__ = ["Video_CS", "Audio_CS", "Merge_CS"]
logger.debug(f"Loaded modules {__all__}")
