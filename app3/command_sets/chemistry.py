from cmd2 import (
    CommandSet,
    Statement,
    with_default_category,
)

@with_default_category("CHEMISTRY")
class chemistry_CS(CommandSet):

    
    def do_does(self, _: Statement):
        """Ut ipsum dolor sit."""
        self._cmd.poutput("Executing does")
    
    def do_discover(self, _: Statement):
        """Dolor sit dolor adipisci neque tempora."""
        self._cmd.poutput("Executing discover")
    
    def do_lose(self, _: Statement):
        """Numquam modi quaerat porro."""
        self._cmd.poutput("Executing lose")
    