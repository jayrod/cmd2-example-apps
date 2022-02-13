from cmd2 import (
    CommandSet,
    Statement,
    with_default_category,
)

@with_default_category("BASIS")
class basis_CS(CommandSet):

    
    def do_remember(self, _: Statement):
        """Est aliquam ipsum velit dolore."""
        self._cmd.poutput("Executing remember")
    