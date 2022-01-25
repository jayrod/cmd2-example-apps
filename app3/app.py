#!/usr/bin/env python3
# coding=utf-8
"""A simple example demonstrating the following:
    1) How to add a command
"""
import pydoc
from dataclasses import dataclass, field
from typing import Any, List

from cmd2 import (
    DEFAULT_SHORTCUTS,
    Cmd,
    Cmd2ArgumentParser,
    CommandSet,
    Statement,
    with_argparser,
)
from cmd2.table_creator import AlternatingTable, BorderedTable, Column
from thefuzz import fuzz

from command_sets import *


@dataclass(order=True)
class CommandInfo:
    category: str
    command: str
    docstring: str


@dataclass(order=True)
class SearchResult:
    sort_index: int = field(init=False)
    command_info: CommandInfo
    fuzz_ratio: float

    def __post_init__(self):
        self.sort_index = self.fuzz_ratio


class BasicApp(Cmd):
    def __init__(self):
        shortcuts = DEFAULT_SHORTCUTS
        shortcuts.update({"/": "search_commands"})
        super().__init__(shortcuts=shortcuts)

    def _get_command_info(self, category: str, command: str) -> CommandInfo:
        func = self.cmd_func(command)
        desc = pydoc.getdoc(func)
        return CommandInfo(category, command, desc)

    parser = Cmd2ArgumentParser()
    parser.add_argument("search_term", help="Search term")

    @with_argparser(parser)
    def do_search_commands(self, parms: Statement):
        cmds_cats, cmds_doc, cmds_undoc, _ = self._build_command_info()

        # other commands
        other_commands = {"Documented": cmds_doc, "Uncategorized": cmds_undoc}

        # add documented and undocument commands together into one dict
        cmds_cats.update(other_commands)

        all_command_info: List[CommandInfo] = []

        for category, commands in cmds_cats.items():
            for command in commands:
                func = self.cmd_func(command)
                desc = pydoc.getdoc(func)
                all_command_info.append(CommandInfo(category, command, desc))

        # Search through all commands
        search_term = parms.search_term

        results: List[SearchResult] = []

        # Only return things higher than the search threshold
        search_threshold = 40

        for ci in all_command_info:
            # Perform a fuzzy search on the command name
            command_ratio = fuzz.ratio(search_term, ci.command)
            # Fuzzy search the function doc string
            doc_string_ratio = fuzz.ratio(search_term, ci.docstring)

            # if neither search result meets threshold then move on
            if all([command_ratio < search_threshold, doc_string_ratio < search_threshold]):
                continue

            # Choose the higher of the two search ratios as the sorting factor
            ratio = command_ratio if command_ratio > doc_string_ratio else doc_string_ratio
            results.append(SearchResult(ci, ratio))

        # if no results found
        if not results:
            self.pwarning("No results found")
            return

        # Prepare data for output
        data_list: List[List[Any]] = list()
        columns: List[Column] = list()
        columns.append(Column("Command", width=20))
        columns.append(Column("Description", width=48))

        sorted_results = sorted(results)

        # If less than 10 items just return all
        if len(results) < 11:
            [data_list.append([i.command_info.command, i.command_info.docstring]) for i in results]

            # Save all results for scripted users
            self.last_result = results
        else:
            # Limit to top 10 results
            top_ten = results[-10:]

            # Save top ten results for scripted users
            self.last_result = top_ten
            [data_list.append([i.command_info.command, i.command_info.docstring]) for i in top_ten]

        # geneate table and print
        at = AlternatingTable(columns)
        table = at.generate_table(data_list)
        self.poutput(table)


if __name__ == "__main__":
    app = BasicApp()
    app.cmdloop()
