from re import I
from typing import Any, List

from app6.common.helper import Chore, FamilyMember, generate_family
from cmd2 import (
    Cmd2ArgumentParser,
    CommandSet,
    Fg,
    Statement,
    ansi,
    with_argparser,
    with_default_category,
)
from cmd2.table_creator import BorderedTable, Column


@with_default_category("FAMILY")
class family_CS(CommandSet):

    def __init__(self):
        super().__init__()

        # Create a family  
        self._family: List[FamilyMember] = generate_family()

    def _generate_chore_string(self, chores: List[Chore]) -> str:
        chore_list = list()
        for chore in sorted(chores):
            if chore.is_done:
                color = Fg.GREEN
            else:
                color = Fg.RED
            chore_list.append(ansi.style(chore.name, fg=color))

        return ", ".join(chore_list)

    def _member_provider(self) -> List[str]:
        return [m.name for m in self._family]

    def do_show_family(self, _: Statement):
        """Shows all family members"""

        data_list: List[List[Any]] = list()
        columns: Column = list()

        for member in self._family:
            data_list.append([
               member.name, 
               self._generate_chore_string(member.chores)])

        columns.append(Column("Name", width=20))
        columns.append(Column("Chores", width=40))

        bt = BorderedTable(columns)
        table = bt.generate_table(data_list)
        self._cmd.poutput(table) 

        # Set return result
        self._cmd.last_result = self._family

    arg_parser = Cmd2ArgumentParser()
    arg_parser.add_argument('--name', choices_provider=_member_provider, help="Family Member")
    arg_parser.add_argument('--chore', help="Unfinished Chore")

    @with_argparser(arg_parser) 
    def do_complete_chore(self, parms: Statement):
        """ Sets a chore to complete for a given family member"""
