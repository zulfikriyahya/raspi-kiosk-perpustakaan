# Troubleshooting

## Buzzer tidak berbunyi
- Cek nomor pin fisik vs BCM dengan `pinout`
- Pastikan GND buzzer terhubung
- Cek jenis buzzer: active (langsung bunyi) vs passive (butuh PWM)

## Warning "channel already in use"
Tambahkan `GPIO.setwarnings(False)` sebelum `GPIO.setmode()`, dan selalu
panggil `GPIO.cleanup()` di blok `finally`.

## Sistem lag / CPU 100%
Cek dengan `htop`. Kalau proses Python RFID di 99%+ CPU terus-menerus,
pastikan ada `time.sleep(0.05)` di akhir loop polling RFID.

## SD Card lambat
Test kecepatan tulis:
```bash
sudo dd if=/dev/zero of=testfile bs=1M count=512 oflag=direct
rm testfile
```
Kalau di bawah ~10 MB/s, pertimbangkan ganti SD Card ke kelas A1/A2.

## Layar kedip-kedip (terutama saat tap kartu)
Kemungkinan besar **undervoltage**. Cek:
```bash
vcgencmd get_throttled
vcgencmd measure_temp
vcgencmd measure_volts
```

Kalau `throttled` bukan `0x0`:
- Ganti ke adaptor resmi 5V/2.5A
- Gunakan kabel USB berkualitas (bukan kabel murah/panjang)
- Tambahkan heatsink kalau suhu > 60°C

## Suhu tinggi (>60°C)
Tambahkan heatsink pasif. Throttling suhu Raspberry Pi mulai di ~80°C.

## GPIO fisik vs BCM tertukar
Selalu cek dengan:
```bash
pinout
```
Pin fisik #12 = GPIO18 (BCM), BUKAN GPIO12.
