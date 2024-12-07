# app/services/contact_service.py
from app.models.contact_model import ContactModel
from app.database.db_utils import get_connection

def get_contact_by_id(contact_id):
    """Obtiene los datos de contacto de un usuario por su ID."""
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM contact WHERE id = ?", (contact_id,))
    row = cursor.fetchone()
    connection.close()
    if row:
        return ContactModel(*row)
    return None
