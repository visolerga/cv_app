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

try:
    from database.db_utils import initialize_database, load_sample_data
    JSON_FILE = CONFIG['DATABASE_JSON']
    # CONFIG = get_config()
    # print(f"Running {CONFIG['APP_NAME']} version {CONFIG['VERSION']}")
    # print(f"Database file: {CONFIG['DATABASE_FILE']}")
except ModuleNotFoundError as e:
    print(f"Error importing configuration: {e}")
    sys.exit(1)
# from config.config import get_config
# from app.database.db_utils import initialize_database, load_sample_data

# # Configuración global
# CONFIG = get_config()

# Ruta al archivo JSON de ejemplo base_dir
# JSON_FILE = os.path.join(os.path.dirname(__file__), "../database/sample_data.json")
# JSON_FILE = os.path.join(base_dir, "/database/sample_data.json")
# JSON_FILE = os.path.join(CONFIG['DATABASE_DIR'], "/sample_data.json")

def main():
    """Punto de entrada principal de la aplicación."""
    print(f"Starting {CONFIG['APP_NAME']} in {'DEBUG' if CONFIG['DEBUG'] else 'PRODUCTION'} mode.")
    print(f"Database file: {CONFIG['DATABASE_FILE']}")

    print("Initializing database...")
    initialize_database()

    print("Loading sample data...")
    load_sample_data(JSON_FILE)
    print("Data loaded successfully.")

if __name__ == "__main__":
    main()
