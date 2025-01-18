import sqlite3
from sqlite3 import Error
from datetime import datetime

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_file)
            self.cursor = self.connection.cursor()
        except Error as e:
            raise ConnectionError(f"Failed to open database: {e}")

    def close(self):
        if self.connection:
            self.connection.close()

    def create_table(self):
        if not self.cursor:
            raise ConnectionError("Database connection is not available.")
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score REAL NOT NULL CHECK(score >= 0 AND score <= 100),
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        self.connection.commit()

    def insert_score(self, problem, score):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.cursor.execute(
            """
            INSERT INTO scores (name, score, timestamp)
            VALUES (?, ?, ?)
            """,
            (problem, score, timestamp),
        )
        self.connection.commit()

    def get_scores(self):
        self.cursor.execute("SELECT * FROM scores")
        return self.cursor.fetchall()
    
    def delete_score(self, id):
        self.cursor.execute("DELETE FROM scores WHERE id=?", (id,))
        self.connection.commit()

    def __del__(self):
        self.close()
