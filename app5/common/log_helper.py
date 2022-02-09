def exception_logger(logger):
    """
    A decorator that wraps the passed in function and logs
    exceptions should one occur

    @param logger: The logging object
    """

    def decorator(func):
        logger.info(f"Exception decorator applied to {func.__name__}")

        def wrapper(*args, **kwargs):

            statement = args[1]

            logger.info(f"Called Command {statement.command}")
            logger.debug(f"Statement arguments: {statement.arg_list}")

            return func(*args, **kwargs)

        return wrapper

    return decorator
