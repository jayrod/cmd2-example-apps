#  Fuzzy Command searching
A Minimal example demonstrating the following:

1) Dynamic discovery of command information via  ``cmd2._build_command_info()``
2) Organization of fairly large ecosystem of commands.
3) Manual instantiation of all CommandSets via __init__.py
4) Automatic shortcut creation 
5) Tabular cmd2 output
6) Dataclass integration

## Philosophy

Any designer faced with the fortunate misfortune of large complex applications will seek out ways to help 
end users navigate bloat. One of the core tenets of the [Command Line Interface Guidelines](https://clig.dev/#foreword) philosophy is [ease of discovery](https://clig.dev/#ease-of-discovery). Cmd2 provides designers with a 
myriad of tools to facilitate ease of discovery to include automatic help text generation and prolific tab completion
throughout the user experience. As evidenced in this large bloated sample application normal means of discovery can be
augmented. 


## Design

There is one main ``search_commands`` located in the base application. It's sole purpose is to gather search terms from the user, build a list of commands and attached help text then apply a fuzzy search  and finally present the user
with legible output. Cmd2 will automatically load commands located in ``CommandSet`` objects provided they have been loaded. We perform this loading by overriding the `__all__` list in command_sets/__init__.py and then importing all from app.py


```python
from command_sets import *
```

The bulk of the heavy lifting is done by the private cmd2 function cmd2._build_command_info:

```python
cmds_cats, cmds_doc, cmds_undoc, _ = self._build_command_info()
```

Roughly speaking the three members can be explained as :

* cmds_cats - Commands and their corresponding categories
* cmds_doc - Documented commands or builtin
* cmds_undoc - Undocumented commands

Using this data it was then fairly straight forward to extract docstring help for each function.

```python
    for command in commands:
        func = self.cmd_func(command)
        desc = pydoc.getdoc(func)
```

The ``cmd2.cmd_func('COMMAND NAME')`` is used to retrieve the actual function matching the command name. i.e. 

```python
command_name = 'help'
func = self.cmd_func(command_name)
print(func)
```

will result in ``do_help``. This is a handy technique for future use. 

Use of dataclasses in this instance may seem over kill but they are super helpful for adding functionality. By creating a ``SearchResult`` dataclass I was able to easily sort results and maintain readability of code. As an 
added benefit script writers will appreciate a ``CommandResult.data`` member that is a dataclass.

```python
@dataclass(order=True)
class SearchResult:
    sort_index: int = field(init=False)
    command_info: CommandInfo
    fuzz_ratio: float

...
        results: List[SearchResult] = []

...
            # Save all results for scripted users
            self.last_result = results
```


Finally, in an effort to [say just enough](https://clig.dev/#saying-just-enough) the user is only presented with at most the
top ten most likely matches to their query. 

```
(Cmd) search_commands temp
╔══════════════════════╤══════════════════════════════════════════════════╗
║ Command              │ Description                                      ║
╠══════════════════════╪══════════════════════════════════════════════════╣
║ create               │ Aliquam non consectetur quaerat consectetur      ║
║                      │ consectetur.                                     ║
║ become               │ Consectetur numquam quaerat quaerat.             ║
║ take                 │ Modi magnam quaerat voluptatem est ut.           ║
║ tend                 │ Velit dolorem dolore voluptatem magnam velit non ║
║                      │ etincidunt.                                      ║
║ seem                 │ Quisquam dolore dolorem numquam aliquam velit.   ║
║ remain               │ Dolorem dolore amet adipisci.                    ║
║ help                 │ List available commands or provide detailed help ║
║                      │ for a specific command                           ║
╚══════════════════════╧══════════════════════════════════════════════════╝
```

## Caveats

* My use of ``thefuzz`` library is most likely flawed and should be done better.
* cmd2._build_command_info() is a private function and should not be relied on **too** heavily. 
* This application construction is an exaggeration so please take it with a grain of salt.

## Requirements

* python == 3.7
* cmd2 == 2.3.3
* thefuzz == 0.19.0