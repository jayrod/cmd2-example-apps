from cmd2 import (
    CommandSet,
    Statement,
    with_default_category,
)

@with_default_category("ASSIGNMENT")
class assignment_CS(CommandSet):

    
    def do_apply(self, _: Statement):
        """Dolorem porro dolore dolorem."""
        self._cmd.poutput("Executing apply")
    
    def do_describe(self, _: Statement):
        """Porro dolore porro quaerat."""
        self._cmd.poutput("Executing describe")
    
    def do_discover(self, _: Statement):
        """Consectetur quaerat sed ipsum consectetur ipsum labore."""
        self._cmd.poutput("Executing discover")
    