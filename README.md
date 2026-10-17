# SiBimbing - Sistem Penjadwalan dan Monitoring Bimbingan Akademik

Proyek Ujian Tengah Semester (UTS) Ganjil T.A. 2026/2027  
**Mata Kuliah:** Rekayasa Perangkat Lunak  
**Program Studi:** D3 Teknik Komputer (D3TK24A1)  
**Pengembang:** Raoul (NIM: 240104004)  
**Dosen Pengampu:** Novemy Triyandari N, SE, MM / Tim Dosen RPL UDB

---

## 📌 Gambaran Umum Proyek
**SiBimbing** adalah sistem berbasis web yang dirancang untuk mengotomasi pengelolaan jadwal bimbingan akademik dan tugas akhir, mencegah bentrok jadwal (*schedule clashing*) antara dosen dan mahasiswa, serta mendokumentasikan catatan riwayat bimbingan (*digital logbook*) secara terstruktur dan transparan.

---

## 📂 Struktur Repositori
```text
sibimbing-akademik/
├── index.php                          # Halaman prototipe & simulasi logika validasi slot bimbingan (Tahap 1)
├── .gitignore                         # Konfigurasi file yang diabaikan oleh Git (Tahap 2)
├── README.md                          # Dokumentasi utama proyek
├── database/
│   └── schema.sql                     # Skema DDL basis data MySQL relasional (Tahap 6)
└── docs/
    ├── TAHAP1_IDENTIFIKASI_MASALAH.md # Latar belakang, perumusan masalah, tujuan, persona
    ├── TAHAP2_DOKUMENTASI_GIT.md      # Riwayat 5 commit, log grafis, dan pemulihan git restore
    ├── TAHAP3_DOKUMENTASI_GITHUB.md   # Feature branch, pull request, dan resolusi konflik
    ├── TAHAP4_PERENCANAAN_SDLC.md     # Project charter dan justifikasi Waterfall Model
    ├── TAHAP5_ANALISIS_KEBUTUHAN.md   # Functional Requirements, Non-Functional, dan MoSCoW
    ├── TAHAP6_PEMODELAN_DAN_BASIS_DATA.md # Proses bisnis, Context Diagram, DFD, Kamus Data
    └── LAPORAN_LENGKAP_UTS_RPL.md     # Laporan komprehensif siap cetak / pengumpulan e-learning
```

---

## 🚀 Panduan Menjalankan Prototipe PHP Lokal
Pastikan PHP sudah terinstal pada komputer Anda (PHP 7.4+ atau PHP 8.x):

1. Buka terminal pada folder proyek ini:
   ```bash
   cd C:\Users\asus\sibimbing-akademik
   ```
2. Jalankan built-in PHP development server:
   ```bash
   php -S localhost:8000
   ```
3. Buka peramban (browser) dan akses:
   👉 **http://localhost:8000**
4. Uji coba pengajuan bimbingan:
   - Pilih `SLOT-01` untuk melihat status **DISETUJUI (SLOT TERKUNCI)**.
   - Pilih `SLOT-02` untuk melihat status penolakan otomatis **DITOLAK (SLOT PENUH)** karena kuota = 0.

---

## 📋 Ringkasan Pemenuhan Rubrik Penilaian UTS

| Tahapan UTS | Bobot | Deskripsi Artefak yang Dihasilkan | Status |
|---|---|---|---|
| **Tahap 1 — Identifikasi Masalah & Persiapan** | 10% | Latar belakang, rumusan masalah, tujuan, target persona, dan file `index.php` interaktif. | ✅ Selesai |
| **Tahap 2 — Version Control Git** | 10% | File `.gitignore`, minimal 5 commit terstruktur, `git log`, dan demonstrasi `git restore`. | ✅ Selesai |
| **Tahap 3 — Pengelolaan Proyek GitHub** | 10% | Remote link GitHub, branch fitur, Pull Request, dan dokumentasi simulasi konflik. | ✅ Selesai |
| **Tahap 4 — Perencanaan SDLC** | 15% | Project Charter lengkap dan analisis justifikasi pemilihan model Waterfall. | ✅ Selesai |
| **Tahap 5 — Analisis Kebutuhan** | 25% | Pemetaan stakeholder, 8 Functional Requirements (FR), NFR, dan prioritas MoSCoW. | ✅ Selesai |
| **Tahap 6 — Pemodelan & Basis Data** | 30% | Alur proses bisnis, Context Diagram, DFD Level 1, Kamus Data, dan DDL `schema.sql`. | ✅ Selesai |
| **Total Bobot** | **100%** | **Seluruh materi terdokumentasi rapi di repositori ini** | **Siap Dinilai** |
