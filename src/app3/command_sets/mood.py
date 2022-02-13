from cmd2 import (
    CommandSet,
    Statement,
    with_default_category,
)

@with_default_category("MOOD")
class mood_CS(CommandSet):

    
    def do_involve(self, _: Statement):
        """Neque eius dolorem sed aliquam non."""
        self._cmd.poutput("Executing involve")
    
    def do_create(self, _: Statement):
        """Sed eius quiquia sit magnam dolor quiquia ut."""
        self._cmd.poutput("Executing create")
    
    def do_reduce(self, _: Statement):
        """Amet dolorem quiquia velit numquam dolorem dolorem."""
        self._cmd.poutput("Executing reduce")
    