from cmd2 import (
    CommandSet,
    Statement,
    with_default_category,
)

@with_default_category("DRIVER")
class driver_CS(CommandSet):

    
    def do_want(self, _: Statement):
        """Dolorem labore sed dolor consectetur sed dolore."""
        self._cmd.poutput("Executing want")
    
    def do_discuss(self, _: Statement):
        """Modi dolore ut est non."""
        self._cmd.poutput("Executing discuss")
    
    def do_tend(self, _: Statement):
        """Velit dolorem dolore voluptatem magnam velit non etincidunt."""
        self._cmd.poutput("Executing tend")
    