import cmd2_ext_test
import pytest
from app2.app import App
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


def test_add(example_app):

    # execute a command
    out = example_app.app_cmd("add")
    # validate the command output and result data
    assert isinstance(out, CommandResult)

def test_complete(example_app):

    # execute a command
    out = example_app.app_cmd("complete")
    # validate the command output and result data
    assert isinstance(out, CommandResult)
