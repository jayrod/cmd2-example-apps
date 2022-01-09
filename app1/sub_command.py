from cmd2 import CommandSet, Statement, Cmd2ArgumentParser, with_argparser


class TestCS(CommandSet):
    def __init__(self):
        super().__init__()


    parser = Cmd2ArgumentParser()
    parser.add_argument('alert_text', help='Alert text')

    @with_argparser(parser)
    def do_add_alert_backwords(self, parms: Statement):
        self._cmd.alert_queue.put(parms.alert_text[::-1])
