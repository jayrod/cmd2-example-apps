from cmd2 import (
    CommandSet,
    Statement,
    with_default_category,
)

@with_default_category("CIGARETTE")
class cigarette_CS(CommandSet):

    
    def do_bring(self, _: Statement):
        """Aliquam quisquam magnam quisquam sed quisquam."""
        self._cmd.poutput("Executing bring")
    
    def do_contain(self, _: Statement):
        """Tempora velit magnam tempora."""
        self._cmd.poutput("Executing contain")
    
    def do_come(self, _: Statement):
        """Dolore est ut voluptatem aliquam amet tempora aliquam."""
        self._cmd.poutput("Executing come")
    
    def do_avoid(self, _: Statement):
        """Amet dolor sed quiquia quaerat."""
        self._cmd.poutput("Executing avoid")
    