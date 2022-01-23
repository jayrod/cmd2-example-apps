from cmd2 import (
    CommandSet,
    Statement,
    with_default_category,
)

@with_default_category("POET")
class poet_CS(CommandSet):

    
    def do_prefer(self, _: Statement):
        """Magnam numquam ipsum dolore quisquam non."""
        self._cmd.poutput("Executing prefer")
    