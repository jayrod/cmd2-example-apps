import cmd2_ext_test
import pytest
from cmd2 import CommandResult

from .app import BasicApp


class ExampleAppTester(cmd2_ext_test.ExternalTestMixin, BasicApp):
    def __init__(self, *args, **kwargs):
        # gotta have this or neither the plugin or cmd2 will initialize
        super().__init__(*args, **kwargs)

@pytest.fixture
def example_app():
    app = ExampleAppTester()
    app.fixture_setup()
    yield app
    app.fixture_teardown()


def test_something(example_app):

    # execute a command
    out = example_app.app_cmd("add_alert lkjfds")
    # validate the command output and result data
    assert isinstance(out, CommandResult)
