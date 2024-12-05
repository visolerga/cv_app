import os

# Base directory of the project (absolute path)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Database configurations
DATABASE_DIR = os.path.join(BASE_DIR, 'database')
DATABASE_FILE = os.path.join(DATABASE_DIR, 'cv_app.db')

# Application configurations
APP_NAME = "CV Generator App"
VERSION = "1.0.0"

# Environment-specific variables (can be overridden in dev_config or prod_config)
DEBUG = True  # Default to True for development
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# Ensure necessary directories exist
os.makedirs(DATABASE_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)
