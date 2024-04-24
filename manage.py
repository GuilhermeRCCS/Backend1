import os
import sys
from dotenv import load_dotenv

def load_app():
    """Load the FastAPI app instance."""
    from app.main import app
    return app

def load_extensions():
    """Load any required extensions."""
    pass

def cli():
    """Define the command line interface."""
    import click

    @click.group()
    def cli():
        """Command line interface for the FastAPI project."""
        pass

    @cli.command()
    @click.option("--reload", is_flag=True, help="Enable reload mode.")
    def run(reload):
        """Run the FastAPI application."""
        from waitress import serve

        app = load_app()
        extensions = load_extensions()

        if reload:
            import uvicorn

            uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
        else:
            serve(app, host="0.0.0.0", port=8000)

    return cli

if __name__ == "__main__":
    load_dotenv()
    sys.path.append(os.getcwd())

    cli = cli()
    cli(prog_name="manage")