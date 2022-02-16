#  Asynchronus Alerts
This is a sample cmd2 application to showcase async rich console integration. 

1) Cmd2 Thread registration
2) CommandSet interaction with main cmd2 instance
3) Rich console integration

## Application Design
app.py is responsible for setting up all of the thread functionality and does not contain any user commands. While the first.py file houses the main featured logic for showing off the rich Live panel. It should be noted that the add and complete commands are superflous and not necessary for execution. 

### App.py

#### __init__

The scaffolding of the application is here in this function. We instantiate two class variables called `active` and `completed`. These queues hold data to be processed. We also create a `stop_event` that make sure the `sim_thread` stops gracefully. Finally we register the pre and postloop hooks.

#### sim_jobs

Sim jobs is a simulation function meant to fill the active queues with data for pretty viewing. 

#### preloop_hook

Here we clear thread events (as a precausion), then create the sim_thread fo the based on the sim_jobs target function and finally start the thread.

#### postloop_hook
Gracefully shutdown the sim thread.

### first.py

#### update_tables
This fuction is responsible for adding content to the `rich.layout` object via a `rich.table` interface. This function accepts two queues as input data originating from the main `cmd2.Cmd` instance.

### App Commands

#### add
This command adds an arbitrary random word to the `active` job queue.

#### complete
This command will perform a `complete` action. For simulation purposes this means choosing a random active task and moving it to the completed queue.

#### show
This command is the main draw in this application. It creates a `rich.console` and `rich.layout` instance to render a `rich.live` screen. This creates a real time window that updates the layout table based on the queue input. 

Notice that this command creates an infinite loop continually updating the layout until the user presses `ctrl-c` to exit. The keyboard interrupt is captured and handled gracefully so as to return execution focus the cmd2 application. 

While this command executes a ***mode*** change it may not be necessary to have a live feed for information. 

## Requirements

* python >= 3.7
* rich >= 11.0.0