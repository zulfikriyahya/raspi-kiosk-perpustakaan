# RFID Kiosk Sirkulasi Perpustakaan — Raspberry Pi 3B+

Sistem RFID reader terintegrasi dengan kiosk browser untuk sirkulasi 
perpustakaan MTsN 1 Pandeglang.

## Hardware
- Raspberry Pi 3B+ (Broadcom BCM2837B0, Quad-core ARM Cortex-A53 1.4GHz)
- RFID Reader MFRC522
- Buzzer aktif
- Push button (untuk shutdown/boot)
- Power supply resmi 5V/2.5A (WAJIB — hindari undervoltage)

## Wiring

### MFRC522 → Raspberry Pi
| Pin MFRC522 | Pin Fisik Pi | GPIO (BCM) |
|---|---|---|
| SDA (SS) | 24 | GPIO8 (CE0) |
| SCK      | 23 | GPIO11 |
| MOSI     | 19 | GPIO10 |
| MISO     | 21 | GPIO9 |
| RST      | 22 | GPIO25 |
| 3.3V     | 1  | 3.3V |
| GND      | 6  | GND |

⚠️ MFRC522 wajib 3.3V, JANGAN sambungkan ke 5V.

### Buzzer → Raspberry Pi
| Buzzer | Pin Fisik | GPIO (BCM) |
|---|---|---|
| Signal (+) | 12 | GPIO18 |
| GND (-)    | GND terdekat | GND |

### Push Button (Shutdown/Boot) → Raspberry Pi
| Button | Pin Fisik | GPIO (BCM) |
|---|---|---|
| Kaki 1 | 5 | GPIO3 |
| Kaki 2 | GND terdekat | GND |

## Format Output ID Kartu
10 digit, zero-padded, dari 4 byte pertama UID kartu (little-endian),
kompatibel dengan implementasi Arduino/ESP32 project sejenis.

## Instalasi

Lihat `install.sh` untuk setup otomatis, atau ikuti langkah manual di
`SETUP.md`.

## Struktur File
- `rfid_kiosk.py` — script utama pembaca RFID + auto-type ke browser
- `test_rfid.py` — script test baca kartu sederhana
- `test_uid_format.py` — verifikasi format UID sama dengan versi Arduino
- `test_buzzer.py` — test buzzer standalone
- `rfid-kiosk.service` — systemd service untuk auto-start
- `autostart` — konfigurasi kiosk browser (LXDE)
- `config-additions.txt` — baris tambahan untuk /boot/config.txt
- `install.sh` — script instalasi otomatis
- `SETUP.md` — panduan setup lengkap step-by-step
- `TROUBLESHOOTING.md` — solusi masalah umum (lag, undervoltage, dll)

## Author
zulfikriyahya — MTsN 1 Pandeglang
