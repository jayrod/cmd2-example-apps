from cmd2 import (
    Cmd2ArgumentParser,
    CommandSet,
    Statement,
    with_argparser,
    with_default_category,
)


@with_default_category("ALERT")
class TestCS(CommandSet):

    parser = Cmd2ArgumentParser()
    parser.add_argument("alert_text", help="Alert text")

    @with_argparser(parser)
    def do_add_alert_backwords(self, parms: Statement):
        """ Adds an alert with reverse naming"""
        self._cmd.alert_queue.put(parms.alert_text[::-1])
