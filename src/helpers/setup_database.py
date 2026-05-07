import bcrypt
import sqlite3


def initialize_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT UNIQUE NOT NULL,
                   password_hash BLOB NOT NULL,
                   admin_level INTEGER DEFAULT 0
                   )
                """)
    conn.commit()
    conn.close()


def add_user(username: str, password: str, admin_level: int = 0):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)

    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password_hash, admin_level) VALUES (?, ?, ?)",
            (username, hashed, admin_level),
        )
        conn.commit()
    except sqlite3.IntegrityError:
        pass


def verify_user(username: str, password: str):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT password_hash, admin_level FROM users WHERE username = ?", (username,)
    )
    result = cursor.fetchone()
    conn.close()

    if result:
        stored_hash, admin_level = result
        if bcrypt.checkpw(password.encode("utf-8"), stored_hash):
            return True, admin_level
    return False, None
