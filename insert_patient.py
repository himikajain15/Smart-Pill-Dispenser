import sqlite3

# Connect to the database
conn = sqlite3.connect("patients.db")
cursor = conn.cursor()

# List of patients to add
patients = [
    ("Devendra", 65, "Male", "Paracetamol", "00:12", "Dr. John", "9876543210"),
    ("Ishika", 70, "Female", "Ibuprofen", "00:08", "Dr. Sarah", "9123456780"),
    ("Himika", 60, "Female", "Aspirin", "00:05", "Dr. Mike", "9988776655"),
    ("Shraddha", 72, "Female", "Metformin", "00:15", "Dr. Emma", "8899001122"),
    ("DVDDD", 75, "Male", "Metformin", "00:16", "Dr. Emma", "8899001122")
]

# Insert each patient
cursor.executemany("""
    INSERT INTO patients (
        name,
        age,
        gender,
        medicine_name,
        schedule,
        doctor_name,
        caretaker_contact
    ) VALUES (?, ?, ?, ?, ?, ?, ?)
""", patients)

# Commit and close
conn.commit()
conn.close()

print("[✔] All patients added successfully.")
