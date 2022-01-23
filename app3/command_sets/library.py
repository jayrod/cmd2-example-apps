from cmd2 import (
    CommandSet,
    Statement,
    with_default_category,
)

@with_default_category("LIBRARY")
class library_CS(CommandSet):

    
    def do_consider(self, _: Statement):
        """Tempora modi labore sed quaerat modi adipisci."""
        self._cmd.poutput("Executing consider")
    
    def do_prepare(self, _: Statement):
        """Velit sit tempora dolore sed labore velit voluptatem."""
        self._cmd.poutput("Executing prepare")
    
    def do_exist(self, _: Statement):
        """Non ut quisquam amet modi."""
        self._cmd.poutput("Executing exist")
    