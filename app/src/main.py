# app/src/main.py
import sys
import os

# Add the parent directory (app/) to the system path
app_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(app_directory)


# Attempt to import the configuration
try:
    from config import get_config
    print("Successfully imported get_config from config.")
except ModuleNotFoundError as e:
    print("Error: ModuleNotFoundError -", e)

# Proceed to get the configuration if the import was successful
try:
    config = get_config()

    print(f"Running {config['APP_NAME']} in {'DEBUG' if config['DEBUG'] else 'PRODUCTION'} mode.")
    print(f"Database file: {config['DATABASE_FILE']}")
except NameError:
    print("Error: The configuration could not be loaded. Ensure the import was successful.")
