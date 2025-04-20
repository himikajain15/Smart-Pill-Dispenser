# check_reminder.py
import time
from datetime import datetime
from database import get_all_reminders
from oled_display import show_message
from buzzer_led import turn_on_alerts
from weight_check import setup_loadcell, get_weight
from camera_motion import extract_frames, detect_hand_to_mouth_motion
from notify import notify_caretaker  # We'll create this

hx = setup_loadcell()

while True:
    now = datetime.now().strftime("%H:%M")
    reminders = get_all_reminders()

    for reminder in reminders:
        if reminder[5] == now:
            print(f"⏰ Reminder for {reminder[1]}: {reminder[4]}")
            show_message(f"Take medicine:\n{reminder[4]}")
            turn_on_alerts()

            # Wait for pill to be taken
            initial_weight = get_weight(hx)
            timeout = time.time() + 60  # Wait 1 min

            while time.time() < timeout:
                current_weight = get_weight(hx)
                if initial_weight - current_weight >= 1:
                    print("✅ Weight change detected.")
                    extract_frames("video.h264")
                    if detect_hand_to_mouth_motion():
                        show_message("Medicine taken")
                        notify_caretaker(reminder[7], "Pill taken", "frames/motion_detected.jpg")
                    else:
                        show_message("No hand motion!")
                    break
                time.sleep(2)
            else:
                show_message("Missed dose!")
                notify_caretaker(reminder[7], "Missed medicine dose!", None)
    time.sleep(30)
