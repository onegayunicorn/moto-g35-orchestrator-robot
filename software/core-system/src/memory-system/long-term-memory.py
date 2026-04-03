import sqlite3
import time

class LongTermMemory:
    def __init__(self, db_path="memory.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS episodic_memory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp REAL,
                    event_type TEXT,
                    description TEXT,
                    context TEXT
                )
            """)
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS semantic_memory (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    concept TEXT,
                    knowledge TEXT
                )
            """)

    def store_episode(self, event_type, description, context):
        with self.conn:
            self.conn.execute("""
                INSERT INTO episodic_memory (timestamp, event_type, description, context)
                VALUES (?, ?, ?, ?)
            """, (time.time(), event_type, description, context))

    def query_episodes(self, keyword):
        with self.conn:
            cursor = self.conn.execute("""
                SELECT * FROM episodic_memory WHERE description LIKE ?
            """, (f'%{keyword}%',))
            return cursor.fetchall()\n