from functools import wraps
from typing import Callable

from cmd2 import Cmd, CommandSet
from loguru import logger


def exception_logger(func: Callable) -> Callable:
    """A logger decorator"""

    @wraps(func)
    def _empty_decorator(self, *args, **kwargs):

        # Get statements from args
        statements = [i for i in args if hasattr(i, "command") if hasattr(i, "arg_list")]

        for statement in statements:
            # Patch the logger so that it appears to come from the called function
            logger.patch(lambda r: r.update(function=func.__name__)).info(
                f"Command: {statement.command}"
            )
            logger.patch(lambda r: r.update(function=func.__name__)).debug(
                f"Statement arguments: {statement.arg_list}"
            )

        func(self, *args, **kwargs)

        # save last result if available
        if issubclass(type(self), CommandSet):
            lr = self._cmd.last_result
        if issubclass(type(self), Cmd):
            lr = self.last_result

        logger.patch(lambda r: r.update(function=func.__name__)).debug(f"Last Result: {lr}")

    _empty_decorator.__doc__ = func.__doc__

    return _empty_decorator
