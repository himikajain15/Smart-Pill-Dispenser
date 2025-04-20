# alert_system.py
import RPi.GPIO as GPIO
import time

# GPIO Pins
LED_PIN = 17
BUZZER_PIN = 27

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

def alert(duration=5):
    print("[INFO] Activating alert system...")
    GPIO.output(LED_PIN, GPIO.HIGH)
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.output(BUZZER_PIN, GPIO.LOW)
    print("[INFO] Alert deactivated.")

def cleanup():
    GPIO.cleanup()

if __name__ == "__main__":
    try:
        alert(duration=5)
    finally:
        cleanup()
