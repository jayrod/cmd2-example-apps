from re import I
from typing import Any, Dict, List, Optional

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
        """ Prints a pretty string for chores showing red for undone and green for done"""

        chore_list = list()

        for chore in sorted(chores):
            if chore.is_done:
                color = Fg.GREEN
            else:
                color = Fg.RED
            chore_list.append(ansi.style(chore.name, fg=color))

        return ", ".join(chore_list)

    def _member_provider(self) -> List[str]:
        """ All family members names used for tab completion"""
        return [m.name for m in self._family]

    def _all_unfinished_chores(self) -> List[str]:

        return list(set([c.name for m in self._family
                    for c in m.chores
                        if not c.is_done]))

    def _get_unfinished_chores(self, name: str) -> List[Chore]:
        if not name:
            return []

        # Find the family member
        fm = [m for m in self._family if m.name == name]

        # If we found nothing or more than one family member
        if len(fm) != 1:
            return []

        return [chore.name for chore in fm[0].chores if not chore.is_done]

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

    def _choices_arg_tokens(self, arg_tokens: Dict[str, List[str]]) -> List[str]:

        # Retrieve the `name` value from list of tokenized arguments
        family_name = arg_tokens.get('name')
        chore_name = arg_tokens.get('chore')

        # If a family name was present
        if family_name:
            # Return the list of chores for the given family member
            return self._get_unfinished_chores(family_name[0])

        # If no family name return all possible unfinished chores
        return self._all_unfinished_chores()

    def _complete_chore(self, name: str, chore_name: str) -> bool:

        # Find the family member
        fm = [m for m in self._family if m.name == name]

        # family member not found
        if not fm:
            return False

        # Search for chore 
        for chore in fm[0].chores:
            if chore.name == chore_name:
                # Remove the old chore 
                fm[0].chores.remove(chore)
                # Add new chore that is now done
                fm[0].chores.append(Chore(chore_name, True))
                return True

        return False

    arg_parser = Cmd2ArgumentParser()
    arg_parser.add_argument('--name', choices_provider=_member_provider, help="Family Member")
    arg_parser.add_argument('--chore', choices_provider=_choices_arg_tokens, help="Unfinished Chore")

    @with_argparser(arg_parser) 
    def do_complete_chore(self, parms: Statement):
        """ Sets a chore to complete for a given family member"""

        name = parms.name
        chore = parms.chore

        if not self._complete_chore(name, chore):
            self._cmd.perror(f"Error while trying to remove {chore}")
            return

        self._cmd.poutput(f"{chore} for {name} is now Completed")
