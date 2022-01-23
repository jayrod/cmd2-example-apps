from cmd2 import (
    CommandSet,
    Statement,
    with_default_category,
)

@with_default_category("CONCEPT")
class concept_CS(CommandSet):

    
    def do_appear(self, _: Statement):
        """Quiquia sit neque voluptatem ipsum."""
        self._cmd.poutput("Executing appear")
    
    def do_continue(self, _: Statement):
        """Sit voluptatem neque sit etincidunt."""
        self._cmd.poutput("Executing continue")
    