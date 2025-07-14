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
