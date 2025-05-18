import sqlite3
from datetime import datetime

DB_NAME = 'messages.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_message(role, content):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    timestamp = datetime.utcnow().isoformat()
    cursor.execute('INSERT INTO messages (role, content, created_at) VALUES (?, ?, ?)',
                   (str(role), str(content), timestamp))
    conn.commit()
    conn.close()

def get_latest_messages(n):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT role, content, created_at
        FROM messages
        ORDER BY created_at DESC
        LIMIT ?
    ''', (n,))
    rows = cursor.fetchall()
    conn.close()
    return [{'role': row[0], 'content': row[1], 'created_at': row[2]} for row in rows]


def truncate_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM messages')
    conn.commit()
    conn.close()