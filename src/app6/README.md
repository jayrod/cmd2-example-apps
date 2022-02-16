#  Situationaly aware tab completion
Dynamic tab completion that changes depending on state.

[![asciicast](https://asciinema.org/a/469436.svg)](https://asciinema.org/a/469436)

## Overview

This fictitious application is a family household chore manager containing two basic commands, `show_family` and `complete_chore`. A judicious family administrator should be able to quickly see who has which chores assigned and then quickly mark chores for a family member as done.

## Application Walk-through

We start with the below simple application structure. The app.py is the main entry point into the application and has the basic cmd2 app declaration. All of the juicy commands are in the family.py file. The helper.py script can be largely ignored as this is merely an application driver providing data support. 

```
.
├── README.md
├── __init__.py
├── app.py
├── command_sets
│   ├── __init__.py
│   └── family.py
└── common
    ├── __init__.py
    └── helper.py
```

Of note however, the helper file contains two dataclasses that make conditional printing very easy. The `order` parameter makes it easier to sort collections.

```python
@dataclass(frozen=True, order=True)
class Chore:
    name: str
    is_done: bool = field(compare=False)

...

@dataclass(order=True)
class FamilyMember:
    name: str 
    chores: List[Chore]

```

During initialization of the command_set we create a list of family members. In a real world application this may be a call to a database or a lazy call later to another data store.

```python
class family_CS(CommandSet):
    def __init__(self):
        super().__init__()

        # Create a family  
        self._family: List[FamilyMember] = generate_family()

```

Here is a quick rundown of private helper functions

```python
def _generate_chore_string(self, chores: List[Chore]) -> str:
    """ Prints a pretty string for chores showing red for 
    undone and green for done"""
def _member_provider(self) -> List[str]:
    """ All family members names used for tab completion"""
def _all_unfinished_chores(self) -> List[str]:
    """ Used to populate chore list when no name given """
def _get_unfinished_chores(self, name: str) -> List[Chore]:
    """ Gets unfinished chores for a given family member """
def _choices_arg_tokens(self, arg_tokens: Dict[str, List[str]]) -> List[str]:
    """Main custom conditional tab completion function"""
```

The `do_show_family` command is fairly straightforward but does give an example of using table creation and ansi coloring for useful formatting. This magic happens in the `_generate_chore_string` function using `ansi.sytle`

```python

    def _generate_chore_string(self, chores: List[Chore]) -> str:
            ...
            else:
               color = Fg.RED
            chore_list.append(ansi.style(chore.name, fg=color))
    ...

```

The `show_family` command then uses this function to dynamically draw a colored table.

```python

    def do_show_family(self, _: Statement):
        ...

        for member in self._family:
            data_list.append([
               member.name, 
               self._generate_chore_string(member.chores)])
```
The result is a table that at a glance shows a ton of information and quickly answers a slew of questions.

* Who are all of the family members?
* What chores do they have assigned?
* What is the status of each of those chores?
* Which family member should get voted off the island for being lazy?

The super interesting and useful command is the `complete_chore` command. It performs a simple function which is to complete a chore for a given household member. While the `--name` parameter is optional, functionality wise it should be given. (See Caveats below)

```python

    arg_parser = Cmd2ArgumentParser()
    arg_parser.add_argument('--name', choices_provider=_member_provider, help="Family Member")
    arg_parser.add_argument('--chore', choices_provider=_choices_arg_tokens, help="Unfinished Chore")

    @with_argparser(arg_parser) 
    def do_complete_chore(self, parms: Statement):
        """ Sets a chore to complete for a given family member"""

```

You will notice each argument utilizes a custom choice provider. Let's start with the `--name` flag as it is straight forward. When a user types or tab completes the `complete_chore` command and begins to tab complete the --name value, the `_member_provider` function fires returning a list of all member names.

```python

    def _member_provider(self) -> List[str]:
        """ All family members names used for tab completion"""
        return [m.name for m in self._family]

```

The `--chore` _choices_arg_tokens is a bit more complex. But in short summary, when the user tab completes this command:

```
complete_chore --name XXXXX --chore <TAB>
```

The `_choices_arg_tokens` function then performs a lookup using the provided name argument and returns all unfinished chores for the user. If no name value is given like so...  

```
complete_chore --chore <TAB>
```

Then the user is presented with a list of unfinished chores that could belong to *any* family member. 

While this is a contrived example this functional nuance *cannot* be overstated. When a user wants to complete a chore we have limited information to only what they care about thereby tailoring design to fit normal mental models. In addition to this tab completion goodness we have left the interface flexible enough that a user could input names not already available with out error. This would be super useful if one were automating chore completion from an external script.


So how did we accomplish this feat of CLI superiority?

```python
    def _choices_arg_tokens(self, arg_tokens: Dict[str, List[str]]) -> List[str]:

        chore_name = arg_tokens.get('chore')

        if family_name:
            return self._get_unfinished_chores(family_name[0])

        return self._all_unfinished_chores()
```

The `Cmd2ArgumentParser` object when executed by a choices_provider function will pass in a list of argument tokens at the very moment tab completion is called for the corresponding option. At that time a designer can inspect the current state of entered arguments. 

Consider the following state examples

```
complete_chore --name XXXXX --chore <TAB>
arg_tokens = {'name': 'XXXXX'}

complete_chore  --chore <TAB>
arg_tokens = {}

complete_chore  --chore l
arg_tokens = {'chore': 'l'}

```

Something else that is super useful for even more complex functionality is that the `self` object passed in is either a `cmd2` or `cmd2.CommandSet` instance. One can imagine holding state information at the class level and referring to it from all choice_provider functions. 

Armed with this knowledge it becomes clear how a designer can implement conditional tab completions. 

```python
        ...
        if family_name:
            return self._get_unfinished_chores(family_name[0])

```

The above snippet is the coup de grâce. In pseudo code.

```
if a family name was given
return a list of unfinished chores based on a given family name
```

the `family_name[0]` denotes the first entry of the name tokens. All entries for arg_tokens are lists which makes sense when thinking of how `nargs` may be present and parsed. 


## Caveats

The example application is NO where near feature complete but it is left up to the avid cmd2 reader to realize its finality. The `complete_chore` command used flag based parameters and it could be argued that the family name is NOT optional or if no name is provided then perhaps we should consider the given `chore` to be complete for all family members. A command for assigning new chores could be added as well. 

There is a lot of business logic stored in tab completion for this application and may be prone to error. For the adventurous reader unable to reconcile not being able to test every line of code the following [example set](https://github.com/python-cmd2/cmd2/blob/master/tests/test_completion.py) from cmd2 may help (or hinder) your efforts. 


Due to the way cmd2 implements tab completion in conjunction with readline it is extremely difficult to debug through custom completer functions. A passable technique is to abstract as much logic from the completer function and use print statements when possible. 


## Requirements

* python >= 3.7

## Further reading
* [Argparse Complete](https://github.com/python-cmd2/cmd2/blob/master/examples/argparse_completion.py)

* [cmd2 argeparse enhancements](https://github.com/python-cmd2/cmd2/blob/master/cmd2/argparse_custom.py#L103)




