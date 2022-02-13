import cmd2_ext_test
import pytest
from app3.app import App
from cmd2 import CommandResult


class ExampleAppTester(cmd2_ext_test.ExternalTestMixin, App):
    def __init__(self, *args, **kwargs):
        # gotta have this or neither the plugin or cmd2 will initialize
        super().__init__(*args, **kwargs)

@pytest.fixture
def example_app():
    app = ExampleAppTester()
    app.fixture_setup()
    yield app
    app.fixture_teardown()


def test_search_command(example_app):

    # execute a command
    out = example_app.app_cmd("search_commands bl")
    # validate the command output and result data
    assert isinstance(out, CommandResult)
    assert out
    assert len(out.data) == 2
