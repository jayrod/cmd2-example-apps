from tempfile import NamedTemporaryFile


def rand_file(suffix: str = "") -> NamedTemporaryFile:
    return NamedTemporaryFile(suffix=suffix)
