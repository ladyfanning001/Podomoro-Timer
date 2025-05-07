# Pomodoro Timer

![Pomodoro Timer Screenshot](screenshots/pomodoro_screenshot.png)

## 📝 Deskripsi
Pomodoro Timer adalah aplikasi manajemen waktu berbasis teknik Pomodoro yang dibuat dengan Python dan Pygame. Aplikasi ini membantu meningkatkan produktivitas dengan membagi waktu kerja menjadi interval fokus yang diselingi dengan istirahat pendek.

## ✨ Fitur
- ⏱️ Timer 25 menit untuk sesi fokus (Pomodoro)
- 🧘‍♀️ Timer 5 menit untuk istirahat pendek (Short Break)
- 🏖️ Timer 15 menit untuk istirahat panjang (Long Break)
- 🔄 Perpindahan otomatis dari sesi fokus ke istirahat dan sebaliknya
- 🔊 Notifikasi suara saat timer selesai
- 📊 Statistik sesi fokus dan total waktu fokus
- 🌈 Tampilan UI yang berbeda untuk setiap mode timer

## 🚀 Cara Menggunakan

### Prasyarat
- Python 3.6 atau lebih baru
- Pygame

### Instalasi
1. Clone repository ini
   ```bash
   git clone https://github.com/yourusername/pomodoro-timer.git
   cd pomodoro-timer
   ```

2. Install dependensi
   ```bash
   pip install pygame
   ```

3. Jalankan aplikasi
   ```bash
   python main.py
   ```

### Penggunaan
- Klik tombol **START** untuk memulai timer
- Klik tombol **STOP** untuk menghentikan timer sementara
- Pilih mode dengan mengklik tombol **Pomodoro**, **Short Break**, atau **Long Break**
- Aplikasi akan otomatis beralih dari sesi fokus ke istirahat pendek
- Setelah 4 sesi fokus, aplikasi akan otomatis memberikan istirahat panjang
- Tampilan statistik akan menunjukkan jumlah sesi fokus yang telah diselesaikan dan total waktu fokus

## 📁 Struktur Proyek
```
pomodoro-timer/
├── main.py           # File utama aplikasi
├── button.py         # Kelas untuk komponen tombol
├── assets/           # Folder untuk semua aset
│   ├── backdrop.jpg  # Gambar latar belakang
│   ├── button.png    # Gambar tombol
│   ├── notification.wav  # Suara notifikasi
│   └── ArialRoundedMTBold.ttf  # Font untuk teks
└── screenshots/      # Screenshot aplikasi untuk dokumentasi
```

## 🛠️ Teknik Pomodoro
Teknik Pomodoro adalah metode manajemen waktu yang dikembangkan oleh Francesco Cirillo pada akhir 1980-an. Teknik ini menggunakan timer untuk membagi pekerjaan menjadi interval fokus (biasanya 25 menit) yang diselingi dengan istirahat pendek.

Siklus dasar:
1. Bekerja dengan fokus selama 25 menit
2. Istirahat selama 5 menit
3. Ulangi langkah 1-2 sebanyak 4 kali
4. Setelah 4 siklus, ambil istirahat panjang selama 15-30 menit

## 🎮 Kontrol Kustom
Anda dapat menyesuaikan durasi timer dengan mengubah variabel berikut di `main.py`:
```python
POMODORO_LENGTH = 1500  # 25 menit dalam detik
SHORT_BREAK_LENGTH = 300  # 5 menit dalam detik
LONG_BREAK_LENGTH = 600  # 10 menit dalam detik
```
