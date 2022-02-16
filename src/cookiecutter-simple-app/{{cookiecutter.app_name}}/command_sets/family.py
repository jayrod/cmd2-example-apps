from dataclasses import dataclass
from enum import Enum
from re import I
from typing import List

from cmd2 import CommandSet, Statement, with_default_category


class Chore(Enum):
    Sweep = 1
    Mop = 2
    Vacuum = 3
    Garbage = 4
    Dishes = 5

@dataclass
class FamilyMember:
    name: str
    chores: List[Chore]

@with_default_category("FAMILY")
class family_CS(CommandSet):

    
    def do_understand(self, _: Statement):
        """Tempora labore ut quisquam aliquam adipisci."""
        self._cmd.poutput("Executing understand")
    