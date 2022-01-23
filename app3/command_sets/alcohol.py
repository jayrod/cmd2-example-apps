from cmd2 import (
    CommandSet,
    Statement,
    with_default_category,
)

@with_default_category("ALCOHOL")
class alcohol_CS(CommandSet):

    
    def do_seem(self, _: Statement):
        """Quisquam dolore dolorem numquam aliquam velit."""
        self._cmd.poutput("Executing seem")
    
    def do_reduce(self, _: Statement):
        """Sit dolorem quisquam voluptatem porro quisquam neque."""
        self._cmd.poutput("Executing reduce")
    
    def do_occur(self, _: Statement):
        """Voluptatem est consectetur neque quisquam numquam eius."""
        self._cmd.poutput("Executing occur")
    
    def do_find(self, _: Statement):
        """Adipisci voluptatem etincidunt ut porro aliquam."""
        self._cmd.poutput("Executing find")
    