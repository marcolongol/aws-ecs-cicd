"""
This is the main entry point for the webapp package.
It imports the app object from the main module and makes it available to the package's users.
"""

__all__ = ["app", "create_app"]

from .main import app, create_app
