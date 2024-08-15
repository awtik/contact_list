import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("\contacts.db")
        self.c = self.conn.cursor()
    def create(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY, name TEXT, number TEXT)''')
    def insert(self, name, number):
        self.c.execute(f"INSERT INTO users (name, number) VALUES ('{name}', '{number}')")
        self.conn.commit()
    def get_contacts(self):
        contacts = self.c.execute(f"SELECT * FROM users")
        return contacts
    def remove_contact(self, name):
        self.c.execute(f"DELETE FROM users WHERE name = '{name}'")
        self.conn.commit()
    def edit_contact_name(self, nowName, newName):
        self.c.execute(f"UPDATE users SET name = '{newName}' WHERE name = '{nowName}'")
        self.conn.commit()
    def edit_contact_number(self, number, name):
        self.c.execute(f"UPDATE users SET number = '{number}' WHERE name = '{name}'")
        self.conn.commit()
    def close_conn(self):
        self.conn.close()