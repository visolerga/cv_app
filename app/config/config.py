import os

# Define base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Directories
DATABASE_DIR = os.path.join(BASE_DIR, 'database')
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# Database configurations
DATABASE_FILE = os.path.join(DATABASE_DIR, 'cv_app.db')
DATABASE_JSON = os.path.join(DATABASE_DIR, 'sample_data.json')

# Application configurations
APP_NAME = "CV Generator App"
VERSION = "1.0.0"
DEBUG = True  # Set True for development, False for production

# Ensure necessary directories exist
for directory in [DATABASE_DIR, LOG_DIR]:
    os.makedirs(directory, exist_ok=True)

def get_config():
    """
    Returns the application configuration as a dictionary.
    """
    return {
        "BASE_DIR": BASE_DIR,
        "DATABASE_DIR": DATABASE_DIR,
        "DATABASE_FILE": DATABASE_FILE,
        "LOG_DIR": LOG_DIR,
        "APP_NAME": APP_NAME,
        "VERSION": VERSION,
        "DEBUG": DEBUG,
        "DATABASE_JSON": DATABASE_JSON,
    }
