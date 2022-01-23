from cmd2 import (
    CommandSet,
    Statement,
    with_default_category,
)

@with_default_category("CANDIDATE")
class candidate_CS(CommandSet):

    
    def do_ensure(self, _: Statement):
        """Sed quaerat magnam sit eius."""
        self._cmd.poutput("Executing ensure")
    
    def do_refer(self, _: Statement):
        """Dolorem modi aliquam non."""
        self._cmd.poutput("Executing refer")
    