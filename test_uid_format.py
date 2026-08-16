"""
Verifikasi format UID Python sama dengan versi Arduino/ESP32.
Tempelkan kartu yang sama di kedua sisi, bandingkan hasilnya.
"""

from mfrc522 import MFRC522
import RPi.GPIO as GPIO

reader = MFRC522()

print("Tempelkan kartu...")
try:
    while True:
        (status, TagType) = reader.MFRC522_Request(reader.PICC_REQIDL)
        if status == reader.MI_OK:
            (status, uid) = reader.MFRC522_Anticoll()
            if status == reader.MI_OK:
                print("Raw UID bytes:", uid)
                uid_value = (
                    (uid[3] << 24) | (uid[2] << 16) | (uid[1] << 8) | uid[0]
                )
                print("Formatted:", f"{uid_value:010d}")
                break
finally:
    GPIO.cleanup()

