import os

import cmd2_ext_test
import pytest
from app5.app import App
from app5.command_sets.audio import AudioJob
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

def test_set(example_app):
    # execute a command
    out = example_app.app_cmd("set")
    # validate the command output and result data
    assert isinstance(out, CommandResult)
    assert 'dvd_drive' in out.data
    assert 'output_folder' in out.data

def test_video(example_app):
    # execute a command
    out = example_app.app_cmd("rip_video .mkv")
    # validate the command output and result data
    assert isinstance(out, CommandResult)
    assert out.data.codec == '.mkv'
