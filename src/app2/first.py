from queue import Queue
from time import sleep

from cmd2 import CommandSet, Fg, Statement, ansi, with_default_category
from RandomWordGenerator import RandomWord
from rich import print
from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.table import Table


@with_default_category("JOB MANAGER")
class FirstCommandSet(CommandSet):
    def __init__(self):
        super().__init__()

    def _update_tables(self, layout: Layout, active: Queue, completed: Queue):

        # Active jobs
        active_jobs = list(active.queue)
        completed_jobs = list(completed.queue)

        active_table = Table(title="Active Jobs", expand=True)
        completed_table = Table(title="Completed Jobs", expand=True)

        active_table.add_column("Job Name")
        completed_table.add_column("Job Name")

        # Add rows
        [active_table.add_row(j) for j in active_jobs]
        [completed_table.add_row(j) for j in completed_jobs]

        layout["upper"].update(active_table)
        layout["lower"].update(completed_table)

    def do_add(self, args: Statement):
        """Adds a new job to the queue"""
        rw = RandomWord()
        job = rw.generate()
        self._cmd.active.put(job)

        output_msg = f"Added job: {ansi.style(job, fg=Fg.GREEN)}"
        self._cmd.poutput(output_msg)

        self._cmd.last_result = job


    def do_complete(self, args: Statement):
        """completes a job"""
        if self._cmd.active.empty():
            self._cmd.perror("No available tasks to complete")
            return

        active_task = self._cmd.active.get()
        message = f"Tasked {ansi.style(active_task, fg=Fg.RED)} for completion"
        self._cmd.poutput(message)
        self._cmd.completed.put(active_task)

        self._cmd.last_result = active_task

    def do_show(self, args: Statement):
        """Shows all jobs"""

        console = Console()
        layout = Layout()

        layout.split_column(Layout(name="upper"), Layout(name="lower"))

        # Update output table
        self._update_tables(layout, self._cmd.active, self._cmd.completed)

        # Create live panel
        with Live(layout, screen=True, redirect_stderr=False) as live:
            try:
                while True:
                    self._update_tables(layout, self._cmd.active, self._cmd.completed)
                    sleep(3)

            except KeyboardInterrupt:
                pass
