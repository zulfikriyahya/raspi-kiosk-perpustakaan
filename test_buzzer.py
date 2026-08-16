"""Test buzzer standalone - pastikan wiring & GPIO benar sebelum integrasi."""

import RPi.GPIO as GPIO
import time

PIN = 18  # GPIO18 (pin fisik 12)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

try:
    for i in range(3):
        GPIO.output(PIN, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(PIN, GPIO.LOW)
        time.sleep(0.3)
    print("Selesai")
finally:
    GPIO.cleanup()
