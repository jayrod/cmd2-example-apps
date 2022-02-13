from cmd2 import (
    CommandSet,
    Statement,
    with_default_category,
)

@with_default_category("PIE")
class pie_CS(CommandSet):

    
    def do_afford(self, _: Statement):
        """Dolorem porro sit voluptatem quaerat eius ut."""
        self._cmd.poutput("Executing afford")
    
    def do_build(self, _: Statement):
        """Eius dolore dolore amet."""
        self._cmd.poutput("Executing build")
    
    def do_receive(self, _: Statement):
        """Est dolor ut dolor adipisci labore adipisci."""
        self._cmd.poutput("Executing receive")
    
    def do_create(self, _: Statement):
        """Aliquam non consectetur quaerat consectetur consectetur."""
        self._cmd.poutput("Executing create")
    