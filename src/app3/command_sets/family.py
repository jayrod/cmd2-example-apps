from cmd2 import (
    CommandSet,
    Statement,
    with_default_category,
)

@with_default_category("FAMILY")
class family_CS(CommandSet):

    
    def do_understand(self, _: Statement):
        """Tempora labore ut quisquam aliquam adipisci."""
        self._cmd.poutput("Executing understand")
    