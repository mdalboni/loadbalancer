import sys

from app import Application
from app.config import config_settings

if __name__ == '__main__':
    config_settings.setup_config(sys.argv[1])
    Application().run()
