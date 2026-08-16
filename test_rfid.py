"""Test sederhana baca kartu RFID menggunakan SimpleMFRC522."""

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("Tempelkan kartu/tag RFID...")
    id, text = reader.read()
    print("ID:", id)
    print("Text:", text)
finally:
    GPIO.cleanup()
