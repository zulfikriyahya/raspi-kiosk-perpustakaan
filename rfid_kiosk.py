"""
RFID Kiosk Sirkulasi - Raspberry Pi 3B+
Membaca kartu RFID (MFRC522) dan auto-type ID ke browser kiosk.
Format UID: 10 digit zero-padded, kompatibel dengan versi Arduino/ESP32.
"""

import RPi.GPIO as GPIO
from mfrc522 import MFRC522
import subprocess
import time

# ==== Konfigurasi ====
BUZZER_PIN = 18  # GPIO18 (pin fisik 12)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.output(BUZZER_PIN, GPIO.LOW)

reader = MFRC522()


def beep(duration=0.12):
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(BUZZER_PIN, GPIO.LOW)


def beep_startup():
    beep(0.08)
    time.sleep(0.06)
    beep(0.08)


def uid_to_10digit(uid_bytes):
    """
    Replikasi logika dari kode Arduino:
    uidValue = byte[3]<<24 | byte[2]<<16 | byte[1]<<8 | byte[0]
    diformat ke 10 digit dengan leading zero.
    """
    if len(uid_bytes) >= 4:
        uid_value = (
            (uid_bytes[3] << 24)
            | (uid_bytes[2] << 16)
            | (uid_bytes[1] << 8)
            | uid_bytes[0]
        )
    else:
        uid_value = (uid_bytes[0] << 8) | uid_bytes[1]
    return f"{uid_value:010d}"


def ketik_ke_browser(teks):
    subprocess.run(["xdotool", "type", "--delay", "50", str(teks)])
    time.sleep(0.2)
    subprocess.run(["xdotool", "key", "Return"])


def proses_kartu(id_str):
    beep()
    time.sleep(0.1)  # jeda kecil, hindari lonjakan beban daya bersamaan
    ketik_ke_browser(id_str)


def main():
    print("RFID Reader siap. Tempelkan kartu...")
    beep_startup()

    while True:
        (status, TagType) = reader.MFRC522_Request(reader.PICC_REQIDL)

        if status == reader.MI_OK:
            (status, uid) = reader.MFRC522_Anticoll()

            if status == reader.MI_OK:
                id_str = uid_to_10digit(uid)
                print(f"Kartu terbaca: {id_str}")
                proses_kartu(id_str)
                time.sleep(1.5)  # jeda anti double-read

        time.sleep(0.05)  # cegah CPU 100% (penting untuk performa)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram dihentikan.")
    finally:
        GPIO.cleanup()
