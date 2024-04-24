from app.schemas import TaskCreate


# Define a function for creating a new task with a given title and description

def create_task(title: str, description: str = None) -> TaskCreate:

    """Create a new task."""

    # Create a new TaskCreate object with the given title and description

    task = TaskCreate(title=title, description=description)

    # Return the TaskCreate object

    return task