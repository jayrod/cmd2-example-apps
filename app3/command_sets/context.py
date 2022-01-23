from cmd2 import (
    CommandSet,
    Statement,
    with_default_category,
)

@with_default_category("CONTEXT")
class context_CS(CommandSet):

    
    def do_agree(self, _: Statement):
        """Sed ut amet porro magnam quiquia voluptatem."""
        self._cmd.poutput("Executing agree")
    