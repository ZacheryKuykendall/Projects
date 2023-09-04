import sqlite3

def create_connection():
    conn = sqlite3.connect("crm.db")
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
                       id INTEGER PRIMARY KEY,
                       first_name TEXT NOT NULL,
                       last_name TEXT NOT NULL,
                       company TEXT,
                       email TEXT,
                       phone TEXT,
                       has_website TEXT
                    )''')
    conn.commit()

def add_contact(conn, contact):
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO contacts(first_name, last_name, company, email, phone, has_website)
                      VALUES(?,?,?,?,?,?)''', contact)
    conn.commit()

def get_all_contacts(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    return cursor.fetchall()

def setup_db():
    conn = create_connection()
    create_table(conn)
    conn.close()

if __name__ == "__main__":
    setup_db()
