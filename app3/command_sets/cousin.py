from cmd2 import (
    CommandSet,
    Statement,
    with_default_category,
)

@with_default_category("COUSIN")
class cousin_CS(CommandSet):

    
    def do_learn(self, _: Statement):
        """Dolore amet dolor voluptatem dolor magnam sed ut."""
        self._cmd.poutput("Executing learn")
    
    def do_apply(self, _: Statement):
        """Tempora sed non dolorem ut."""
        self._cmd.poutput("Executing apply")
    