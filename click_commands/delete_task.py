# Import required libraries

import click

from app.crud import delete_task


# Define the `delete_task` command

@click.command()

@click.argument('task_id')

@click.pass_context

def delete_task_command(ctx, task_id):

    """Delete a task with the given ID."""

    

    # Call the `delete_task` function from the `crud` module to delete the task

    delete_task(task_id)


    # Print a message to confirm that the task was deleted

    click.echo(f"Task with ID {task_id} deleted")


# Add the `delete_task_command` to the `click_commands` context

ctx.add_command(delete_task_command)