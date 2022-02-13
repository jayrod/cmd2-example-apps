from typing import List

from cmd2 import (
    Cmd2ArgumentParser,
    CommandSet,
    Statement,
    with_argparser,
    with_default_category,
)


@with_default_category("WEBSITE")
class WebsiteTools_CS(CommandSet):
    """This command set performs actions against urls"""

    def _url_choices_provider(self) -> List[str]:
        """Generates list of url choices

        Returns:
            List[str]: urls from cmd instance url cache
        """
        return self._cmd._url_cache

    def _add_url_to_cache(self, url: str) -> None:
        """Adds a url to cmd instance url cache. This allowes for history to be shared among commands without waiting for history to be saved to disk.

        Args:
            url (str): Url to add to cache
        """

        if url not in self._cmd._url_cache:
            self._cmd._url_cache.append(url)

    curl_parser = Cmd2ArgumentParser()
    curl_parser.add_argument(
        "url", choices_provider=_url_choices_provider, help="URL to perform curl on"
    )

    @with_argparser(curl_parser)
    def do_curl(self, parms: Statement):
        """Curls a website url"""
        self._cmd.poutput(f"Performing curl on url {parms.url}")

        # Add new url to cache for further usage
        self._add_url_to_cache(parms.url)

    snapshot_parser = Cmd2ArgumentParser()
    snapshot_parser.add_argument(
        "url", choices_provider=_url_choices_provider, help="URL to snapshot"
    )

    @with_argparser(snapshot_parser)
    def do_snap_shot(self, parms: Statement):
        """Takes a thumbnail snapshot of a website url"""
        self._cmd.poutput(f"Performing snapshot of url {parms.url}")

        # Add new url to cache for further usage
        self._add_url_to_cache(parms.url)
