#!/bin/bash
# Instalasi otomatis RFID Kiosk Sirkulasi
# Jalankan dengan: bash install.sh

set -e

echo "=== RFID Kiosk Sirkulasi - Instalasi ==="

echo "[1/9] Update sistem..."
sudo apt update
sudo apt upgrade -y

echo "[2/9] Install dependensi..."
sudo apt install -y python3-pip python3-dev chromium-browser xdotool unclutter

echo "[3/9] Install library Python..."
pip3 install mfrc522 spidev RPi.GPIO gpiozero

echo "[4/9] Enable SPI..."
sudo raspi-config nonint do_spi 0

echo "[5/9] Setup autostart kiosk browser..."
mkdir -p ~/.config/lxsession/LXDE-pi
cp autostart ~/.config/lxsession/LXDE-pi/autostart

echo "[6/9] Setup systemd service RFID kiosk..."
sudo cp rfid-kiosk.service /etc/systemd/system/rfid-kiosk.service
sudo systemctl daemon-reload
sudo systemctl enable rfid-kiosk.service

echo "[7/9] Setup systemd service tombol restart (tahan 5 detik)..."
sudo cp button-control.service /etc/systemd/system/button-control.service
sudo systemctl daemon-reload
sudo systemctl enable button-control.service

echo "[8/9] Setup izin restart tanpa password..."
echo "zulfikriyahya ALL=(ALL) NOPASSWD: /sbin/reboot" | sudo tee -a /etc/sudoers.d/button-control
sudo chmod 0440 /etc/sudoers.d/button-control

echo "[9/9] (Opsional) Tambahkan config-additions.txt ke /boot/config.txt jika perlu HDMI stabilization"
echo ""
echo "=== Instalasi selesai ==="
echo "Silakan reboot: sudo reboot"
