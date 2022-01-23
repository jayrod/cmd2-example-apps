from cmd2 import (
    CommandSet,
    Statement,
    with_default_category,
)

@with_default_category("ENGINE")
class engine_CS(CommandSet):

    
    def do_follow(self, _: Statement):
        """Labore dolorem quisquam sed quaerat neque modi."""
        self._cmd.poutput("Executing follow")
    