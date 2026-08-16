# Panduan Setup Lengkap

## 1. Flash Raspberry Pi OS
Gunakan Raspberry Pi Imager (https://www.raspberrypi.com/software/), 
pilih **Raspberry Pi OS 32-bit (armhf)** untuk kompatibilitas terbaik 
dengan Pi 3B+.

## 2. Wiring
Lihat diagram di README.md — pastikan MFRC522 di 3.3V (JANGAN 5V).

## 3. Instalasi Software

### Otomatis
```bash
git clone <gist-url> rfid-kiosk
cd rfid-kiosk
chmod +x install.sh
bash install.sh
```

### Manual
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-dev chromium-browser xdotool unclutter -y
pip3 install mfrc522 spidev RPi.GPIO gpiozero
sudo raspi-config nonint do_spi 0
```

## 4. Setup Kiosk Browser
```bash
mkdir -p ~/.config/lxsession/LXDE-pi
cp autostart ~/.config/lxsession/LXDE-pi/autostart
```

## 5. Setup Auto-start Service RFID
```bash
sudo cp rfid-kiosk.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable rfid-kiosk.service
sudo systemctl start rfid-kiosk.service
```

## 6. Setup Tombol Restart (tahan 5 detik)

Salin script dan service:
```bash
sudo cp button-control.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable button-control.service
sudo systemctl start button-control.service
```

Beri izin restart tanpa password:
```bash
sudo visudo
```
Tambahkan baris:
zulfikriyahya ALL=(ALL) NOPASSWD: /sbin/reboot

> Catatan: kemampuan **boot otomatis dari kondisi mati** dengan tekan 
> tombol sebentar adalah fitur hardware bawaan GPIO3 — tidak perlu 
> overlay atau konfigurasi tambahan di `/boot/config.txt`.

## 7. (Opsional) HDMI stabilization
Kalau ada masalah kedip layar terkait HDMI, tambahkan isi dari
`config-additions.txt` ke:
```bash
sudo nano /boot/config.txt
```

## 8. Cek GPU memory split
```bash
sudo raspi-config
```
→ Performance Options → GPU Memory → set ke 16

## 9. Cek Compositor
```bash
sudo raspi-config
```
→ Advanced Options → Compositor → Disable

## 10. Reboot dan Test
```bash
sudo reboot
```

## Testing
```bash
python3 test_buzzer.py       # test buzzer
python3 test_uid_format.py   # verifikasi format UID sama dengan Arduino
python3 test_rfid.py         # test baca kartu sederhana
```

Testing tombol:
- Tahan tombol fisik 5 detik saat Pi menyala → sistem harus restart
- Matikan Pi (`sudo systemctl poweroff` atau cabut listrik lalu 
  hubungkan kembali), tekan tombol sebentar → Pi harus boot otomatis


