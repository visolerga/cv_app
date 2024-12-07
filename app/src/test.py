# app/src/test_imports.py

import os
import sys

# Asegúrate de que el directorio base esté en la ruta de Python
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if base_dir not in sys.path:
    sys.path.append(base_dir)

# try:
#     from app.services.user_service import get_full_user_data
#     print("User service imported successfully.")
# except ModuleNotFoundError as e:
#     print(f"Error importing user service: {e}")

try:
    from services.contact_service import get_contact_by_id
    print("Contact service imported successfully.")
except ModuleNotFoundError as e:
    print(f"Error importing contact service: {e}")
