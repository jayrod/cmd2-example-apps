from cmd2 import (
    CommandSet,
    Statement,
    with_default_category,
)

@with_default_category("SOUP")
class soup_CS(CommandSet):

    
    def do_provide(self, _: Statement):
        """Quaerat aliquam quaerat velit eius dolore amet neque."""
        self._cmd.poutput("Executing provide")
    
    def do_vary(self, _: Statement):
        """Tempora non ut eius magnam adipisci etincidunt."""
        self._cmd.poutput("Executing vary")
    