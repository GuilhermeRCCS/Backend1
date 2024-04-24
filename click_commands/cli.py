# Import required modules

import click

from app.crud import create_task, update_task, delete_task


# Define the click command group

@click.group()

def cli():

    """Task management CLI commands"""

    pass


# Define the create task command

@cli.command()

@click.argument('title')

@click.argument('description', required=False)

def create(title, description=None):

    """Create a new task with the given title and optional description.


    Args:

        title (str): The title of the task.

        description (str, optional): The description of the task. Defaults to None.

    """

    # Call the create_task function from the crud module

    create_task(title, description)

    click.echo(f"Task '{title}' created.")


# Define the update task command

@cli.command()

@click.argument('task_id')

@click.argument('title', required=False)

@click.argument('description', required=False)

def update(task_id, title=None, description=None):

    """Update an existing task with the given ID, title, and optional description.


    Args:

        task_id (int): The ID of the task to update.

        title (str, optional): The new title of the task. Defaults to None.

        description (str, optional): The new description of the task. Defaults to None.

    """

    # Call the update_task function from the crud module

    update_task(task_id, title, description)

    click.echo(f"Task with ID '{task_id}' updated.")


# Define the delete task command

@cli.command()

@click.argument('task_id')

def delete(task_id):

    """Delete a task with the given ID.


    Args:

        task_id (int): The ID of the task to delete.

    """

    # Call the delete_task function from the crud module

    delete_task(task_id)

    click.echo(f"Task with ID '{task_id}' deleted.")


# Run the click command group

if __name__ == '__main__':

    cli()