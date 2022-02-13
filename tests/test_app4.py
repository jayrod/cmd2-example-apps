import os

import cmd2_ext_test
import pytest
from app4.app import App
from app4.common.utils import AppFileManager
from cmd2 import CommandResult


class ExampleAppTester(cmd2_ext_test.ExternalTestMixin, App):
    def __init__(self, *args, **kwargs):
        # gotta have this or neither the plugin or cmd2 will initialize
        super().__init__(*args, **kwargs)

@pytest.fixture
def app_file_man():

    afm = AppFileManager('TestApp')
    yield afm


@pytest.fixture
def example_app(app_file_man):
    app = ExampleAppTester(application_manager=app_file_man)
    app.fixture_setup()
    yield app
    app.fixture_teardown()

def test_curl(example_app):

    # execute a command
    out = example_app.app_cmd("curl http://one.two")
    # validate the command output and result data
    assert isinstance(out, CommandResult)
