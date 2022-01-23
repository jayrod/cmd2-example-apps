from cmd2 import (
    CommandSet,
    Statement,
    with_default_category,
)

@with_default_category("CHILD")
class child_CS(CommandSet):

    
    def do_improve(self, _: Statement):
        """Eius neque dolor est est dolor non."""
        self._cmd.poutput("Executing improve")
    