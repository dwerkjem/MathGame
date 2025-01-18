import sqlite3
from sqlite3 import Error


class DataBase:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_file)
            self.cursor = self.conn.cursor()
        except Error as e:
            print(e)

    def close(self):
        if self.conn:
            self.conn.close()

    def create_table(self, table_name, columns):
        try:
            self.cursor.execute(f"CREATE TABLE {table_name} ({columns})")
        except Error as e:
            print(e)

    def insert(self, table_name, columns, values):
        try:
            self.cursor.execute(
                f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
            )
            self.conn.commit()
        except Error as e:
            print(e)

    def select(self, table_name, columns, condition):
        try:
            self.cursor.execute(f"SELECT {columns} FROM {table_name} WHERE {condition}")
            return self.cursor.fetchall()
        except Error as e:
            print(e)

    def update(self, table_name, columns, condition):
        try:
            self.cursor.execute(f"UPDATE {table_name} SET {columns} WHERE {condition}")
            self.conn.commit()
        except Error as e:
            print(e)

    def delete(self, table_name, condition):
        try:
            self.cursor.execute(f"DELETE FROM {table_name} WHERE {condition}")
            self.conn.commit()
        except Error as e:
            print(e)

    def test_health(self):
        try:
            self.cursor.execute("SELECT 1")
            return True
        except Error as e:
            print(e)
            return False


if __name__ == "__main__":
    db = DataBase("test.db")
    db.connect()
    db.test_health()
