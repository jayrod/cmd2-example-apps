from cmd2 import (
    CommandSet,
    Statement,
    with_default_category,
)

@with_default_category("BREAD")
class bread_CS(CommandSet):

    
    def do_realize(self, _: Statement):
        """Quisquam est quisquam neque est ut non."""
        self._cmd.poutput("Executing realize")
    
    def do_perform(self, _: Statement):
        """Dolor non dolore voluptatem consectetur dolor ipsum."""
        self._cmd.poutput("Executing perform")
    