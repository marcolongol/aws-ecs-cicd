"""
This is the main entry point for the webapp package module.
"""

import os
import sys
from dataclasses import dataclass

from webapp import create_app

app = create_app()


@dataclass
class Config:
    PROD_MODE = os.getenv("PROD_MODE", "False") == "True"
    WEBAPP_HOST = os.getenv("WEBAPP_HOST", "0.0.0.0")
    WEBAPP_PORT = os.getenv("WEBAPP_PORT", "80")
    WEBAPP_WORKERS = os.getenv("WEBAPP_WORKERS", os.cpu_count() or 1)
    DEBUG_MODE = os.getenv("DEBUG_MODE", "False") == "True"
    PLATFORM = sys.platform


CONFIG = Config()

if __name__ == "__main__":
    if CONFIG.PROD_MODE and CONFIG.PLATFORM != "win32":
        import gunicorn.app.base

        class StandaloneApplication(gunicorn.app.base.BaseApplication):
            def __init__(self, app, options=None):
                self.options = options or {}
                self.application = app
                super().__init__()

            def load_config(self):
                config = {
                    key: value
                    for key, value in self.options.items()
                    if key in self.cfg.settings and value is not None
                }
                for key, value in config.items():
                    self.cfg.set(key.lower(), value)

            def load(self):
                return self.application

        options = {
            "bind": f"{CONFIG.WEBAPP_HOST}:{CONFIG.WEBAPP_PORT}",
            "workers": f"{CONFIG.WEBAPP_WORKERS}",
        }

        StandaloneApplication(app, options).run()

    else:

        print("Running in development mode")
        app.run(
            host=CONFIG.WEBAPP_HOST,
            port=int(CONFIG.WEBAPP_PORT),
            debug=CONFIG.DEBUG_MODE,
        )
