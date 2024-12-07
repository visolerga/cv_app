import sqlite3
import os
import json
from config.config import get_config

CONFIG = get_config()

def get_connection():
    """Crea y devuelve una conexión a la base de datos."""
    return sqlite3.connect(CONFIG["DATABASE_FILE"])

def database_exists():
    """Verifica si la base de datos ya existe."""
    return os.path.exists(CONFIG["DATABASE_FILE"])

def table_exists(table_name):
    """Verifica si una tabla existe en la base de datos."""
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT name FROM sqlite_master WHERE type='table' AND name=?
    """, (table_name,))
    result = cursor.fetchone()
    connection.close()
    return result is not None

def initialize_database():
    """Inicializa la base de datos creando las tablas faltantes."""
    connection = get_connection()
    cursor = connection.cursor()

    # Esquema de la base de datos
    schema = """
    CREATE TABLE IF NOT EXISTS contact (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        address TEXT
    );
    CREATE TABLE IF NOT EXISTS social_links (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        platform TEXT NOT NULL,
        url TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES contact(id)
    );
    CREATE TABLE IF NOT EXISTS skills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        source_type TEXT CHECK (source_type IN ('job', 'course')),
        source_id INTEGER,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES contact(id)
    );
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        company TEXT NOT NULL,
        role TEXT NOT NULL,
        start_date TEXT NOT NULL,
        end_date TEXT,
        description TEXT,
        FOREIGN KEY (user_id) REFERENCES contact(id)
    );
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        institution TEXT,
        completion_date TEXT,
        FOREIGN KEY (user_id) REFERENCES contact(id)
    );
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        description TEXT,
        url TEXT,
        FOREIGN KEY (user_id) REFERENCES contact(id)
    );
    CREATE TABLE IF NOT EXISTS education (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        degree TEXT NOT NULL,
        institution TEXT NOT NULL,
        start_date TEXT NOT NULL,
        end_date TEXT,
        FOREIGN KEY (user_id) REFERENCES contact(id)
    );
    """
    cursor.executescript(schema)
    connection.commit()
    connection.close()

def load_sample_data(json_file):
    """
    Carga datos de ejemplo desde un archivo JSON solo si las tablas dependientes están vacías.
    
    Parámetros:
    - json_file: Ruta del archivo JSON que contiene los datos de ejemplo.
    """
    connection = get_connection()  # Establece una conexión con la base de datos
    cursor = connection.cursor()

    # Verificar si la tabla `contact` está vacía
    cursor.execute("SELECT COUNT(*) FROM contact")
    if cursor.fetchone()[0] > 0:
        print("La base de datos ya tiene datos. No se cargará de nuevo el JSON.")
        connection.close()
        return  # Finaliza la ejecución si ya hay datos en `contact`

    # Abrir y cargar los datos del archivo JSON
    with open(json_file, "r") as file:
        data = json.load(file)

    # Iterar sobre cada usuario en el JSON
    for user_data in data["users"]:
        user = user_data["contact"]

        # Insertar los datos de contacto en la tabla `contact`
        cursor.execute("""
            INSERT INTO contact (name, email, phone, address)
            VALUES (?, ?, ?, ?)
        """, (user["name"], user["email"], user["phone"], user["address"]))
        
        # Obtener el ID del usuario recién creado
        user_id = cursor.lastrowid

        # Insertar habilidades asociadas al usuario
        for skill in user_data.get("skills", []):
            cursor.execute("""
                INSERT INTO skills (name, source_type, source_id, user_id)
                VALUES (?, ?, ?, ?)
            """, (skill["skill_name"], skill["source"], skill.get("source_id", None), user_id))

        # Insertar enlaces sociales asociados al usuario
        for social_link in user_data.get("social_links", []):
            cursor.execute("""
                INSERT INTO social_links (user_id, platform, url)
                VALUES (?, ?, ?)
            """, (user_id, social_link["platform"], social_link["url"]))

        # Insertar experiencias laborales asociadas al usuario
        for job in user_data.get("jobs", []):
            cursor.execute("""
                INSERT INTO jobs (user_id, company, role, start_date, end_date, description)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (user_id, job["company"], job["role"], job["start_date"], job.get("end_date", None), job["description"]))

        # Insertar cursos asociados al usuario
        for course in user_data.get("courses", []):
            cursor.execute("""
                INSERT INTO courses (user_id, title, institution, completion_date)
                VALUES (?, ?, ?, ?)
            """, (user_id, course["title"], course.get("institution", None), course.get("completion_date", None)))

        # Insertar proyectos asociados al usuario
        for project in user_data.get("projects", []):
            cursor.execute("""
                INSERT INTO projects (user_id, title, description, url)
                VALUES (?, ?, ?, ?)
            """, (user_id, project["title"], project["description"], project.get("url", None)))

        # Insertar educación asociada al usuario
        for education in user_data.get("education", []):
            cursor.execute("""
                INSERT INTO education (user_id, degree, institution, start_date, end_date)
                VALUES (?, ?, ?, ?, ?)
            """, (user_id, education["degree"], education["institution"], education["start_date"], education.get("end_date", None)))

    # Confirmar los cambios realizados en la base de datos
    connection.commit()
    connection.close()
