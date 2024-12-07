import os
import sys

# Ensure the base directory is in the Python path
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if base_dir not in sys.path:
    sys.path.append(base_dir)

# Import configurations
try:
    from config.config import get_config
    CONFIG = get_config()
    print(f"Running {CONFIG['APP_NAME']} version {CONFIG['VERSION']}")
    print(f"Database file: {CONFIG['DATABASE_FILE']}")
except ModuleNotFoundError as e:
    print(f"Error importing configuration: {e}")
    sys.exit(1)

# Import database utilities
try:
    from database.db_utils import (
        database_exists,
        initialize_database,
        load_sample_data,
    )
    JSON_FILE = CONFIG['DATABASE_JSON']
except ModuleNotFoundError as e:
    print(f"Error importing database utilities: {e}")
    sys.exit(1)

# Import user service
try:
    from app.services.user_service import get_full_user_data
    print("User service imported successfully.")
except ModuleNotFoundError as e:
    print(f"Error importing user service: {e}")
    sys.exit(1)



def main():
    """Punto de entrada principal de la aplicación."""
    print(f"Starting {CONFIG['APP_NAME']} in {'DEBUG' if CONFIG['DEBUG'] else 'PRODUCTION'} mode.")

    # Check if the database exists, and initialize if necessary
    if not database_exists():
        print("Database does not exist. Creating...")
        initialize_database()
        print("Database created successfully.")
    else:
        print("Database exists. Ensuring all tables are initialized...")
        initialize_database()

    # Load sample data
    print("Loading sample data...")
    load_sample_data(JSON_FILE)
    print("Sample data loaded successfully.")

    # Example of fetching and displaying a user's full data
    user_id = 1  # Replace with dynamic input if needed
    try:
        print(f"Fetching full data for user ID: {user_id}")
        user_data = get_full_user_data(user_id)
        print(f"User data for ID {user_id}: {user_data}")
    except Exception as e:
        print(f"Error fetching user data: {e}")

    print("Application setup complete.")


if __name__ == "__main__":
    main()
