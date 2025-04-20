from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Initialize Database
def init_db():
    conn = sqlite3.connect('patients.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        gender TEXT,
        medicine_name TEXT,
        schedule TEXT,
        doctor_name TEXT,
        caretaker_contact TEXT
    )''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('patients.db')
    c = conn.cursor()
    c.execute("SELECT * FROM patients")
    data = c.fetchall()
    conn.close()
    return render_template('index.html', patients=data)

@app.route('/add', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        medicine = request.form['medicine']
        schedule = request.form['schedule']
        doctor = request.form['doctor']
        caretaker = request.form['caretaker']

        conn = sqlite3.connect('patients.db')
        c = conn.cursor()
        c.execute("INSERT INTO patients (name, age, gender, medicine_name, schedule, doctor_name, caretaker_contact) VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (name, age, gender, medicine, schedule, doctor, caretaker))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('add_patient.html')

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
