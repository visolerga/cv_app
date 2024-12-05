import sqlite3
import os
import json
from config.config import get_config

CONFIG = get_config()

def get_connection():
    """Crea y devuelve una conexión a la base de datos."""
    return sqlite3.connect(CONFIG["DATABASE_FILE"])

def initialize_database():
    """Inicializa la base de datos creando todas las tablas necesarias."""
    connection = get_connection()
    cursor = connection.cursor()

    # Esquema de la base de datos
    schema = """
    CREATE TABLE IF NOT EXISTS users (
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
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    CREATE TABLE IF NOT EXISTS skills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        source_type TEXT CHECK (source_type IN ('job', 'course')),
        source_id INTEGER,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        company TEXT NOT NULL,
        role TEXT NOT NULL,
        start_date TEXT NOT NULL,
        end_date TEXT,
        description TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        institution TEXT,
        completion_date TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        description TEXT,
        url TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    CREATE TABLE IF NOT EXISTS education (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        degree TEXT NOT NULL,
        institution TEXT NOT NULL,
        start_date TEXT NOT NULL,
        end_date TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    """
    cursor.executescript(schema)
    connection.commit()
    connection.close()

def load_sample_data(json_file):
    """Carga datos de ejemplo desde un archivo JSON."""
    with open(json_file, "r") as file:
        data = json.load(file)

    connection = get_connection()
    cursor = connection.cursor()

    # Cargar datos en la tabla users
    for user in data["users"]:
        cursor.execute("""
            INSERT INTO users (name, email, phone, address)
            VALUES (?, ?, ?, ?)
        """, (user["name"], user["email"], user["phone"], user["address"]))

        user_id = cursor.lastrowid

        # Cargar social_links
        for social_link in user.get("social_links", []):
            cursor.execute("""
                INSERT INTO social_links (user_id, platform, url)
                VALUES (?, ?, ?)
            """, (user_id, social_link["platform"], social_link["url"]))

        # Cargar skills
        for skill in user.get("skills", []):
            cursor.execute("""
                INSERT INTO skills (name, source_type, source_id, user_id)
                VALUES (?, ?, ?, ?)
            """, (skill["skill_name"], skill["source_type"], skill.get("source_id", None), user_id))

        # Cargar jobs
        for job in user.get("jobs", []):
            cursor.execute("""
                INSERT INTO jobs (user_id, company, role, start_date, end_date, description)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (user_id, job["company"], job["role"], job["start_date"], job.get("end_date"), job.get("description")))

        # Cargar courses
        for course in user.get("courses", []):
            cursor.execute("""
                INSERT INTO courses (user_id, title, institution, completion_date)
                VALUES (?, ?, ?, ?)
            """, (user_id, course["title"], course.get("institution"), course.get("completion_date")))

        # Cargar projects
        for project in user.get("projects", []):
            cursor.execute("""
                INSERT INTO projects (user_id, title, description, url)
                VALUES (?, ?, ?, ?)
            """, (user_id, project["title"], project.get("description"), project.get("url")))

        # Cargar education
        for education in user.get("education", []):
            cursor.execute("""
                INSERT INTO education (user_id, degree, institution, start_date, end_date)
                VALUES (?, ?, ?, ?, ?)
            """, (user_id, education["degree"], education["institution"], education["start_date"], education.get("end_date")))

    connection.commit()
    connection.close()

if __name__ == "__main__":
    initialize_database()
    load_sample_data("path/to/sample_data.json")
