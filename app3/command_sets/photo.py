from cmd2 import (
    CommandSet,
    Statement,
    with_default_category,
)

@with_default_category("PHOTO")
class photo_CS(CommandSet):

    
    def do_contain(self, _: Statement):
        """Consectetur ut ipsum labore eius quaerat tempora."""
        self._cmd.poutput("Executing contain")
    
    def do_understand(self, _: Statement):
        """Porro ut ipsum aliquam velit adipisci."""
        self._cmd.poutput("Executing understand")
    
    def do_avoid(self, _: Statement):
        """Sed dolore non ut tempora."""
        self._cmd.poutput("Executing avoid")
    
    def do_solve(self, _: Statement):
        """Dolor sit neque porro."""
        self._cmd.poutput("Executing solve")
    
    def do_write(self, _: Statement):
        """Etincidunt quiquia magnam magnam adipisci."""
        self._cmd.poutput("Executing write")
    