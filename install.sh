#!/bin/bash
# Instalasi otomatis RFID Kiosk Sirkulasi
# Jalankan dengan: bash install.sh

set -e

echo "=== RFID Kiosk Sirkulasi - Instalasi ==="

echo "[1/7] Update sistem..."
sudo apt update
sudo apt upgrade -y

echo "[2/7] Install dependensi..."
sudo apt install -y python3-pip python3-dev chromium-browser xdotool unclutter

echo "[3/7] Install library Python..."
pip3 install mfrc522 spidev RPi.GPIO

echo "[4/7] Enable SPI..."
sudo raspi-config nonint do_spi 0

echo "[5/7] Setup autostart kiosk browser..."
mkdir -p ~/.config/lxsession/LXDE-pi
cp autostart ~/.config/lxsession/LXDE-pi/autostart

echo "[6/7] Setup systemd service..."
sudo cp rfid-kiosk.service /etc/systemd/system/rfid-kiosk.service
sudo systemctl daemon-reload
sudo systemctl enable rfid-kiosk.service

echo "[7/7] Tambahkan konfigurasi shutdown button ke /boot/config.txt"
echo "Silakan tambahkan manual isi dari config-additions.txt ke /boot/config.txt"
echo ""
echo "=== Instalasi selesai ==="
echo "Silakan reboot: sudo reboot"
