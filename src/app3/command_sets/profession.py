from cmd2 import (
    CommandSet,
    Statement,
    with_default_category,
)

@with_default_category("PROFESSION")
class profession_CS(CommandSet):

    
    def do_choose(self, _: Statement):
        """Dolorem quaerat dolorem non."""
        self._cmd.poutput("Executing choose")
    
    def do_hear(self, _: Statement):
        """Numquam labore etincidunt quaerat est sit ipsum."""
        self._cmd.poutput("Executing hear")
    
    def do_describe(self, _: Statement):
        """Neque dolorem modi quiquia dolor sed quiquia neque."""
        self._cmd.poutput("Executing describe")
    
    def do_solve(self, _: Statement):
        """Porro porro adipisci modi ipsum velit."""
        self._cmd.poutput("Executing solve")
    