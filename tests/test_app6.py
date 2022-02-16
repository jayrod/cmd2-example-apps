import os

import cmd2_ext_test
import pytest
from app6.app import App
from app6.common.helper import FamilyMember
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

def test_show_family(example_app):
    # execute a command
    out = example_app.app_cmd("show_family")
    # validate the command output and result data
    assert isinstance(out, CommandResult)

    # There should be 2 or more family members
    assert len(out.data) >= 2
    # All instances are Family members
    assert all([isinstance(i, FamilyMember) for i in out.data])
