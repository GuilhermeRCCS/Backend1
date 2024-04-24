# Import required libraries

import click

from app.crud import update_task

from app.schemas import TaskUpdate


# Define the `update_task` command

@click.command()

@click.argument('task_id')

@click.argument('title', required=False)

@click.argument('description', required=False)

@click.pass_context

def update_task_command(ctx, task_id, title=None, description=None):

    """Update a task with the given ID."""

    

    # Create a new `TaskUpdate` instance with the given title and description

    task_data = TaskUpdate(title=title, description=description)


    # Call the `update_task` function from the `crud` module to update the task

    updated_task = update_task(task_id, task_data)


    # Print a message to confirm that the task was updated

    click.echo(f"Task '{updated_task.title}' updated with ID {updated_task.id}")


# Add the `update_task_command` to the `click_commands` context

ctx.add_command(update_task_command)