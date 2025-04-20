import sqlite3

DB_NAME = 'patients.db'

# Create table if it doesn't exist
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        medicine_name TEXT,
        schedule TEXT,
        doctor_name TEXT,
        caretaker_contact TEXT
    )''')
    conn.commit()
    conn.close()

# Add a new patient
def add_patient(name, age, gender, medicine_name, schedule, doctor_name, caretaker_contact):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO patients (name, age, gender, medicine_name, schedule, doctor_name, caretaker_contact) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (name, age, gender, medicine_name, schedule, doctor_name, caretaker_contact))
    conn.commit()
    conn.close()

# Fetch all patient reminders
def get_patient_reminders():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT name, schedule FROM patients")
    data = c.fetchall()
    conn.close()
    return data

# Get all patient data (if needed)
def get_all_patients():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM patients")
    data = c.fetchall()
    conn.close()
    return data
