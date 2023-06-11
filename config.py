"""Class-based Flask app configuration."""
from os import environ, path
from dotenv import load_dotenv

# Setting paths and directories
dirname = path.dirname(__file__)
basedir = path.abspath(dirname)
env_path = path.join(basedir, ".env")

print('__file__: ', __file__)
print('dirname: ', dirname)
print('basedir: ', basedir)
print('env_path: ', env_path)

# Loading environment variables from .env
load_dotenv(env_path)

class Config:
    """Set the variables"""
    SECRET_KEY = environ.get("SECRET_KEY")
    FLASK_ENV = environ.get("FLASK_DEBUG")
    FLASK_APP = environ.get("FLASK_APP")

    