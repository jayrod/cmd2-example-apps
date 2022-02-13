from cmd2 import (
    CommandSet,
    Statement,
    with_default_category,
)

@with_default_category("BASKET")
class basket_CS(CommandSet):

    
    def do_decide(self, _: Statement):
        """Consectetur sed aliquam dolor tempora tempora consectetur quaerat."""
        self._cmd.poutput("Executing decide")
    
    def do_supply(self, _: Statement):
        """Quisquam ut dolore ut."""
        self._cmd.poutput("Executing supply")
    
    def do_identify(self, _: Statement):
        """Labore ipsum neque tempora magnam."""
        self._cmd.poutput("Executing identify")
    
    def do_explain(self, _: Statement):
        """Non quaerat ut dolorem voluptatem."""
        self._cmd.poutput("Executing explain")
    