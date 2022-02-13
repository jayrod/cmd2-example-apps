from cmd2 import (
    CommandSet,
    Statement,
    with_default_category,
)

@with_default_category("ECONOMICS")
class economics_CS(CommandSet):

    
    def do_remain(self, _: Statement):
        """Dolorem dolore amet adipisci."""
        self._cmd.poutput("Executing remain")
    
    def do_represent(self, _: Statement):
        """Adipisci sit aliquam etincidunt."""
        self._cmd.poutput("Executing represent")
    
    def do_protect(self, _: Statement):
        """Amet adipisci velit neque ut tempora dolore eius."""
        self._cmd.poutput("Executing protect")
    