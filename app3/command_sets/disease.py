from cmd2 import (
    CommandSet,
    Statement,
    with_default_category,
)

@with_default_category("DISEASE")
class disease_CS(CommandSet):

    
    def do_expect(self, _: Statement):
        """Amet voluptatem quisquam dolorem sed."""
        self._cmd.poutput("Executing expect")
    
    def do_represent(self, _: Statement):
        """Sit quiquia quisquam quaerat eius voluptatem porro."""
        self._cmd.poutput("Executing represent")
    