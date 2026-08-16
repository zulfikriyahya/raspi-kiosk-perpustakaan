"""
Kontrol tombol fisik:
- Pi mati -> tekan sebentar -> boot otomatis (bawaan hardware GPIO3)
- Pi menyala -> tahan tombol 5 detik -> restart
"""

from gpiozero import Button
from signal import pause
import subprocess

BUTTON_PIN = 3          # GPIO3 (Pin fisik 5)
HOLD_SECONDS = 5        # durasi tahan untuk restart

button = Button(BUTTON_PIN, pull_up=True, hold_time=HOLD_SECONDS)


def restart_pi():
    print(f"Tombol ditahan {HOLD_SECONDS} detik — restart sistem...")
    subprocess.run(["sudo", "reboot"])


button.when_held = restart_pi

print(f"Menunggu tombol ditahan {HOLD_SECONDS} detik untuk restart...")
pause()
