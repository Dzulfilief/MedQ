# 🩺 MedQ – Simulasi Antrean Klinik

**MedQ** adalah aplikasi web sederhana untuk mensimulasikan antrean pasien di sebuah klinik.  
Dibuat dengan **Flask (Python)** dan bisa dijalankan di mana saja menggunakan **Docker**.

---

## ✨ Fitur Utama
✅ Input jumlah pasien, durasi pemeriksaan, jam mulai, dan jumlah layanan (dokter/poli)  
✅ Simulasi antrean dengan jadwal otomatis (mulai & selesai)  
✅ Dukungan multi layanan (Poli A, B, C, dst)  
✅ Tombol Reset, Tambah Pasien, Cetak Jadwal  
✅ Template tambahan:
- `index.html` → Halaman utama simulasi
- `cetak.html` → Tampilan cetak jadwal
- `riwayat.html` → (opsional) halaman riwayat

---

## 📦 Teknologi
- **Backend**: Flask (Python)
- **Database**: SQLite (`antri.db`)
- **Frontend**: HTML + Bootstrap 5
- **Container**: Docker

---

## 🚀 Menjalankan Aplikasi

### 1. Build Docker Image
Jalankan di folder project:
```bash
docker build -t medq .
```
2️⃣ Jalankan Container
Setelah build berhasil:

bash
Copy
Edit
docker run -p 5000:5000 medq
3️⃣ Akses Aplikasi
Buka browser dan akses:

arduino
Copy
Edit
http://localhost:5000
4️⃣ Berhentiin Container (opsional)
Kalau mau stop container:

bash
Copy
Edit
docker ps           # cek ID container
docker stop <ID_CONTAINER>
📂 Struktur Folder
arduino
Copy
Edit
.
├── app.py              # main Flask app
├── db.py               # modul database (SQLite)
├── antri.db            # database lokal (TIDAK PERLU di-push ke GitHub)
├── requirements.txt    # daftar library Python
├── Dockerfile          # konfigurasi Docker
├── README.md           # dokumentasi project
└── templates/          # folder template HTML
    ├── index.html
    ├── cetak.html
    └── riwayat.html
⚠️ Catatan Penting
✅ antri.db adalah file database lokal yang otomatis dibuat saat aplikasi berjalan.
Tidak perlu di-upload atau di-download dari GitHub. Pastikan sudah masuk ke .gitignore.

✅ Pastikan Docker sudah terinstal di komputermu.

🏷 Lisensi
Proyek ini dibuat untuk keperluan pembelajaran dan tugas kuliah.
Silakan gunakan dan modifikasi sesuai kebutuhan. ✨
