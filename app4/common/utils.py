from pathlib import Path

from xdg import XDG_CACHE_HOME, XDG_DATA_HOME


class AppFileManager:
    """Application file manager used to abstract location and usage of persistent history file."""

    def __init__(self, app_name: str):
        """Initialization

        Args:
            app_name (str): Name of application for use in folder creation
        """
        self.app_name = app_name
        self._hist_file = XDG_DATA_HOME.joinpath(self.app_name, "persistent_history.cmd2")

    @property
    def hist_file(self) -> Path:
        """Retrieves path to history file

        Returns:
            Path: persistent history file path
        """
        return self._hist_file

    def create_hist_dir(self) -> Path:
        """Creates the directory to store history file

        Returns:
            Path: History dir path
        """
        XDG_DATA_HOME.joinpath(self.app_name).mkdir(parents=True, exist_ok=True)
