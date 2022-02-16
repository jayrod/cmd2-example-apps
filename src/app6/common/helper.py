from dataclasses import dataclass, field
from random import choice, getrandbits, randint
from typing import List

from attr import frozen
from faker.factory import Factory


@dataclass(frozen=True, order=True)
class Chore:
    name: str
    is_done: bool = field(compare=False)


ALL_POSSIBLE_CHORES: List[str] = [
    'Sweeping', 
    'Mopping',
    'Dusting',
    'Dishes',
    'Mowing',
]

@dataclass(order=True)
class FamilyMember:
    name: str 
    chores: List[Chore]

def rand_member() -> FamilyMember:
    Faker = Factory.create
    fake = Faker()

    # Number of chores
    num_chores = randint(1,5)
    chores = [Chore(choice(ALL_POSSIBLE_CHORES), bool(getrandbits(1))) for _ in range(num_chores)]
    chores = list(set(chores))

    return FamilyMember(fake.name(), chores)

def generate_family() -> List[FamilyMember]:
    num_family_members = randint(2,8)
    return sorted([rand_member() for _ in range(num_family_members)])
