# pill_reminder.py
import sqlite3
from datetime import datetime
import time

from gpio_alerts import alert, cleanup
from oled_display import show_message

DB_PATH = "patients.db"  # Or your database file name

def get_due_reminders():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    now = datetime.now()
    current_time = now.strftime("%H:%M")

    cursor.execute("SELECT name, medicine_name, schedule FROM patients")
    reminders = cursor.fetchall()

    due_list = []
    for name, medicine_name, schedule in reminders:
        if schedule == current_time:
            due_list.append((name, medicine_name))

    conn.close()
    return due_list

def run_reminder_loop():
    print("[INFO] Pill reminder system is running...")
    try:
        while True:
            due = get_due_reminders()
            if due:
                for name, medicine_name in due:
                    message = f"Time to take:\n{medicine_name}"
                    print(f"[ALERT] For {name}: {message}")
                    show_message(message)
                    alert(duration=5)
                    show_message("Reminder sent!")
                    time.sleep(60)  # Avoid retriggering in the same minute
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n[INFO] Stopping reminder system.")
    finally:
        cleanup()

if __name__ == "__main__":
    run_reminder_loop()
