from cmd2 import (
    CommandSet,
    Statement,
    with_default_category,
)

@with_default_category("EXPLANATION")
class explanation_CS(CommandSet):

    
    def do_include(self, _: Statement):
        """Dolor non labore dolor non numquam quaerat."""
        self._cmd.poutput("Executing include")
    
    def do_receive(self, _: Statement):
        """Eius velit modi ipsum consectetur adipisci."""
        self._cmd.poutput("Executing receive")
    
    def do_choose(self, _: Statement):
        """Quaerat eius velit labore velit dolorem."""
        self._cmd.poutput("Executing choose")
    
    def do_does(self, _: Statement):
        """Aliquam consectetur consectetur voluptatem."""
        self._cmd.poutput("Executing does")
    
    def do_seem(self, _: Statement):
        """Eius sed eius est."""
        self._cmd.poutput("Executing seem")
    