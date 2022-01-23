from cmd2 import (
    CommandSet,
    Statement,
    with_default_category,
)

@with_default_category("VERSION")
class version_CS(CommandSet):

    
    def do_develop(self, _: Statement):
        """Sit est quaerat eius dolorem."""
        self._cmd.poutput("Executing develop")
    