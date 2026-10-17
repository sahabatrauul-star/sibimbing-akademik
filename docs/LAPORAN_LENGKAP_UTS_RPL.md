# LAPORAN LENGKAP PROYEK UJIAN TENGAH SEMESTER (UTS)
## REKAYASA PERANGKAT LUNAK (GANJIL 2026/2027)

---

* **Judul Proyek:** Sistem Penjadwalan dan Monitoring Bimbingan Akademik (SiBimbing)
* **Program Studi:** D3 Teknik Komputer
* **Kelas:** D3TK24A1
* **Nama Mahasiswa:** Raoul
* **NIM:** 240104004
* **Dosen Pengampu:** Novemy Triyandari N, SE, MM / Dosen RPL UDB
* **Tanggal Pengerjaan:** Oktober 2026

---

## DAFTAR ISI
1. [TAHAP 1: Identifikasi Masalah & Persiapan Proyek](#tahap-1--identifikasi-masalah-dan-persiapan-proyek)
2. [TAHAP 2: Version Control Menggunakan Git](#tahap-2--version-control-menggunakan-git)
3. [TAHAP 3: Pengelolaan Proyek Menggunakan GitHub](#tahap-3--pengelolaan-proyek-menggunakan-github)
4. [TAHAP 4: Perencanaan Pengembangan dengan SDLC](#tahap-4--perencanaan-pengembangan-dengan-sdlc)
5. [TAHAP 5: Analisis Kebutuhan Perangkat Lunak](#tahap-5--analisis-kebutuhan-perangkat-lunak)
6. [TAHAP 6: Pemodelan Sistem & Perancangan Basis Data](#tahap-6--pemodelan-sistem-dan-perancangan-basis-data)
7. [Lampiran: Skema Basis Data SQL (DDL)](#lampiran-skema-basis-data-sql-ddl)

---

## TAHAP 1 — Identifikasi Masalah dan Persiapan Proyek

### 1.1 Latar Belakang Masalah
Bimbingan akademik dan tugas akhir/skripsi merupakan tahapan penting dalam proses pembelajaran di perguruan tinggi. Namun, proses penjadwalan bimbingan tatap muka selama ini sebagian besar masih dilakukan secara manual dan informal melalui aplikasi pengirim pesan instan (WhatsApp/Telegram). 

Praktik ini menimbulkan berbagai kendala nyata di lingkungan kampus:
- **Pesan Tenggelam dan Terabaikan:** Banyaknya chat yang masuk ke ponsel dosen membuat permohonan bimbingan mahasiswa terlewat atau lambat dibalas.
- **Bentrok Jadwal Temu (*Schedule Clashing*):** Tidak tersedianya jadwal ketersediaan waktu dosen yang dapat diakses secara publik dan real-time menyebabkan beberapa mahasiswa datang bersamaan pada waktu yang sama.
- **Hilangnya Rekam Jejak Revisi (*No Historical Logbook*):** Catatan revisi yang dicatat di kartu bimbingan fisik konvensional rentan hilang, kotor, atau tertinggal, sehingga evaluasi kesinambungan bimbingan sulit dipantau secara objektif.

Oleh karena itu, sistem berbasis web **SiBimbing** dirancang untuk mendigitalkan dan mengotomasi proses penjadwalan janji temu serta pencatatan logbook revisi secara terstruktur.

### 1.2 Rumusan Masalah
1. Bagaimana mengelola slot ketersediaan waktu dosen pembimbing secara transparan agar terhindar dari jadwal bentrok?
2. Bagaimana memfasilitasi mahasiswa dalam mengajukan permohonan bimbingan beserta topik bahasan secara praktis?
3. Bagaimana membangun sistem monitoring evaluasi logbook revisi yang dapat diakses oleh mahasiswa, dosen pembimbing, dan koordinator program studi?

### 1.3 Tujuan Proyek
1. Mengembangkan sistem informasi berbasis web yang mengotomasi reservasi slot jadwal bimbingan dosen.
2. Mencegah terjadinya *double booking* melalui validasi sisa kuota slot secara otomatis.
3. Menyediakan rekam jejak digital (*e-logbook*) untuk mendokumentasikan progres bab dan revisi mahasiswa.
4. Memudahkan program studi dalam memvalidasi keaktifan bimbingan sebagai prasyarat pendaftaran ujian sidang akhir.

### 1.4 Target Pengguna Sistem (*User Persona*)
1. **Mahasiswa:** Melihat slot ketersediaan waktu dosen, mengajukan reservasi jadwal bimbingan, mengisi topik bahasan, dan memantau catatan revisi dosen.
2. **Dosen Pembimbing:** Membuka dan mengelola slot waktu bimbingan, meninjau permohonan mahasiswa (menerima/menolak), serta mengisi catatan evaluasi revisi pada e-logbook.
3. **Admin / Koordinator Akademik:** Mengelola master data pengguna serta memantau rekapitulasi progres kelayakan sidang seluruh mahasiswa.

### 1.5 Implementasi Prototipe Logika Bisnis (`index.php`)
Sesuai arahan tugas, telah dibuat file `index.php` yang memuat informasi identitas proyek dan contoh logika validasi pemesanan slot waktu bimbingan dengan aturan: jika kuota bimbingan pada slot waktu yang dipilih adalah 0, sistem menolak pengajuan; jika kuota > 0, sistem menerima dan mengunci jadwal bimbingan.

---

## TAHAP 2 — Version Control Menggunakan Git

### 2.1 Konfigurasi `.gitignore`
File `.gitignore` disiapkan untuk memastikan file build, dependensi, dan environment sensitif tidak terunggah ke repositori:
```gitignore
/vendor/
/node_modules/
.env
config.local.php
*.log
.vscode/
.idea/
.DS_Store
Thumbs.db
```

### 2.2 Skenario 5 Commit yang Bermakna
Repositori lokal dikelola dengan 5 commit bermakna yang mencerminkan tahapan rekayasa perangkat lunak:
1. `chore: inisialisasi repositori Git dan konfigurasi .gitignore`
2. `docs: tambahkan identifikasi masalah, latar belakang, dan tujuan sistem (Tahap 1)`
3. `feat: implementasi halaman informasi proyek dan logika validasi slot bimbingan pada index.php`
4. `docs: susun perencanaan SDLC Waterfall, project charter, dan analisis kebutuhan MoSCoW (Tahap 4 & 5)`
5. `design: tambahkan pemodelan diagram konteks, kamus data, dan skema SQL basis data (Tahap 6)`

### 2.3 Riwayat Perubahan (`git log`)
Hasil perintah `git log --oneline --graph` menunjukkan riwayat commit yang runut dan jelas.

### 2.4 Demonstrasi Pemulihan File (`git restore`)
Jika terjadi perubahan yang salah pada file kode sumber yang belum di-commit:
```bash
# Cek perubahan
git status
# Pulihkan file ke kondisi commit terakhir
git restore index.php
# Status kembali bersih (working tree clean)
```

---

## TAHAP 3 — Pengelolaan Proyek Menggunakan GitHub

### 3.1 Penautan Remote Repository
Repositori lokal dihubungkan ke GitHub dengan perintah:
```bash
git branch -M main
git remote add origin https://github.com/raoulaswar/sibimbing-akademik.git
git push -u origin main
```

### 3.2 Pembuatan Feature Branch dan Pull Request (PR)
1. Membuat branch baru untuk fitur bimbingan:
   ```bash
   git checkout -b feature/modul-penjadwalan
   ```
2. Mengembangkan fitur baru, commit, dan push ke remote branch:
   ```bash
   git push origin feature/modul-penjadwalan
   ```
3. Membuat **Pull Request** di GitHub dari branch `feature/modul-penjadwalan` ke branch `main`, kemudian melakukan review dan merge.

### 3.3 Simulasi Konflik Git dan Penyelesaiannya
- **Penyebab Konflik:** Terjadi ketika dua branch berbeda mengedit baris kode yang sama pada file `index.php` secara bersamaan.
- **Penyelesaian:** Git menandai baris konflik dengan `<<<<<<< HEAD`, `=======`, dan `>>>>>>>`. Pengembang melakukan resolusi secara manual dengan memilih baris yang valid, menghapus penanda konflik, lalu melakukan commit penggabungan (*merge commit*).

---

## TAHAP 4 — Perencanaan Pengembangan dengan SDLC

### 4.1 Project Charter
- **Nama Proyek:** SiBimbing
- **Permasalahan Utama:** Ketiadaan platform penjadwalan bimbingan mandiri dan pencatatan riwayat revisi yang terintegrasi.
- **Tujuan:** Mengotomasi pemesanan jadwal bimbingan dan menyediakan kartu kendali bimbingan digital (*digital logbook*).
- **Ruang Lingkup (Scope):** Autentikasi multi-user, kelola ketersediaan waktu dosen, reservasi jadwal mahasiswa, persetujuan dosen, pencatatan revisi logbook, dan laporan rekapitulasi.
- **Analisis Risiko & Mitigasi:**
  - *Risiko double-booking:* Diminimalisir dengan *atomic transaction locking* pada basis data.
  - *Risiko keterlambatan konfirmasi dosen:* Diterapkan sistem auto-reschedule bila H-1 belum direspon.

### 4.2 Pemilihan Model SDLC: Waterfall
Model SDLC yang dipilih adalah **Waterfall Model** dengan pertimbangan:
1. Alur administrasi bimbingan akademik di kampus memiliki Standar Operasional Prosedur (SOP) baku yang stabil dan tidak berubah-ubah.
2. Sangat cocok untuk proyek evaluasi akademik UTS karena setiap tahapan menghasilkan artefak dokumen yang terstruktur dan mudah diaudit.
3. Menjamin kualitas desain arsitektur data selesai secara tuntas sebelum tahap pengkodean penuh dimulai.

---

## TAHAP 5 — Analisis Kebutuhan Perangkat Lunak

### 5.1 Stakeholder
- **Mahasiswa:** Mengajukan bimbingan dan melihat feedback revisi.
- **Dosen Pembimbing:** Mengatur jadwal ketersediaan, menyetujui janji, dan mengisi logbook.
- **Koordinator Prodi / Admin:** Memantau ketercapaian target minimal bimbingan untuk kelayakan sidang tugas akhir.

### 5.2 Kebutuhan Fungsional (Functional Requirements)
- **FR-01:** Autentikasi login multi-role (Mahasiswa, Dosen, Admin).
- **FR-02:** Pengelolaan slot jadwal ketersediaan waktu bimbingan oleh Dosen.
- **FR-03:** Pencarian dan filter slot waktu dosen yang masih kosong.
- **FR-04:** Pengajuan reservasi bimbingan oleh Mahasiswa dengan validasi sisa kuota.
- **FR-05:** Persetujuan atau penolakan jadwal oleh Dosen Pembimbing.
- **FR-06:** Pencatatan ringkasan revisi dan status kelayakan progres bab di e-logbook.
- **FR-07:** Tampilan kartu kontrol histori bimbingan digital bagi Mahasiswa.
- **FR-08:** Rekapitulasi laporan keaktifan bimbingan untuk syarat sidang.

### 5.3 Prioritas Kebutuhan (MoSCoW)
- **Must Have:** FR-01 (Login), FR-02 (Slot Jadwal), FR-04 (Pengajuan Booking), FR-05 (Persetujuan Dosen), FR-06 (Catatan Logbook).
- **Should Have:** FR-03 (Filter Jadwal), FR-07 (Kartu Kontrol), FR-08 (Laporan Rekap).
- **Could Have:** Notifikasi email/WhatsApp dan fitur upload file draft lampiran.
- **Won't Have:** Video call conference bawaan dan tanda tangan digital kriptografis.

---

## TAHAP 6 — Pemodelan Sistem dan Perancangan Basis Data

### 6.1 Alur Proses Bisnis
1. Dosen menginput slot jadwal ketersediaan waktu ke sistem.
2. Mahasiswa melihat jadwal kosong, memilih slot, dan mengajukan janji temu beserta topik bahasan.
3. Dosen menerima notifikasi dan memberikan konfirmasi persetujuan.
4. Bimbingan dilaksanakan, lalu dosen menginputkan catatan evaluasi revisi pada logbook bimbingan.
5. Sistem menyimpan histori kartu kontrol bimbingan mahasiswa dan menghitung akumulasi kehadiran untuk syarat sidang.

### 6.2 Context Diagram (DFD Level 0)
Sistem SiBimbing berinteraksi dengan tiga entitas eksternal:
- **Mahasiswa:** Mengirim data akun, permohonan booking, dan topik bahasan; menerima info slot kosong, status konfirmasi, dan catatan revisi logbook.
- **Dosen Pembimbing:** Mengirim data slot ketersediaan, konfirmasi booking, dan catatan evaluasi logbook; menerima notifikasi permohonan bimbingan dan kartu kontrol mahasiswa.
- **Koordinator / Admin:** Mengirim manajemen data master; menerima laporan rekapitulasi progres bimbingan mahasiswa.

### 6.3 Kamus Data (*Data Dictionary*) Singkat
- **`users`:** `id` (PK), `username` (NIM/NIDN), `password` (Hash), `role` (admin/dosen/mahasiswa).
- **`dosen`:** `id` (PK), `user_id` (FK), `nidn`, `nama_lengkap`, `gelar`, `email`, `no_hp`.
- **`mahasiswa`:** `id` (PK), `user_id` (FK), `nim`, `nama_lengkap`, `program_studi`, `dosen_pembimbing_id` (FK), `judul_tugas_akhir`.
- **`jadwal_slot`:** `id` (PK), `dosen_id` (FK), `tanggal`, `jam_mulai`, `jam_selesai`, `kuota_mhs`, `sisa_kuota`, `ruangan_lokasi`, `status_slot`.
- **`bimbingan_booking`:** `id` (PK), `kode_booking`, `slot_id` (FK), `mahasiswa_id` (FK), `topik_bahasan`, `status_booking`.
- **`logbook_bimbingan`:** `id` (PK), `booking_id` (FK), `catatan_revisi`, `progres_bab`, `status_kelayakan`, `tanggal_bimbingan`.

---

## LAMPIRAN: Skema Basis Data SQL (DDL)
File skema lengkap tersedia pada repositori di direktori `database/schema.sql`.

```sql
CREATE DATABASE IF NOT EXISTS sibimbing_db;
USE sibimbing_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'dosen', 'mahasiswa') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE dosen (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    nidn VARCHAR(20) UNIQUE NOT NULL,
    nama_lengkap VARCHAR(100) NOT NULL,
    gelar VARCHAR(30) NOT NULL,
    email VARCHAR(100) NOT NULL,
    no_hp VARCHAR(20) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE mahasiswa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    nim VARCHAR(20) UNIQUE NOT NULL,
    nama_lengkap VARCHAR(100) NOT NULL,
    program_studi VARCHAR(50) DEFAULT 'D3 Teknik Komputer',
    dosen_pembimbing_id INT NULL,
    judul_tugas_akhir TEXT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (dosen_pembimbing_id) REFERENCES dosen(id) ON DELETE SET NULL
);

CREATE TABLE jadwal_slot (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dosen_id INT NOT NULL,
    tanggal DATE NOT NULL,
    jam_mulai TIME NOT NULL,
    jam_selesai TIME NOT NULL,
    kuota_mhs INT DEFAULT 1,
    sisa_kuota INT DEFAULT 1,
    ruangan_lokasi VARCHAR(100) DEFAULT 'Ruang Dosen Lab Komputer',
    status_slot ENUM('tersedia', 'penuh', 'dibatalkan') DEFAULT 'tersedia',
    FOREIGN KEY (dosen_id) REFERENCES dosen(id) ON DELETE CASCADE
);

CREATE TABLE bimbingan_booking (
    id INT AUTO_INCREMENT PRIMARY KEY,
    kode_booking VARCHAR(30) UNIQUE NOT NULL,
    slot_id INT NOT NULL,
    mahasiswa_id INT NOT NULL,
    topik_bahasan TEXT NOT NULL,
    status_booking ENUM('menunggu', 'disetujui', 'ditolak', 'selesai') DEFAULT 'menunggu',
    alasan_penolakan TEXT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (slot_id) REFERENCES jadwal_slot(id) ON DELETE CASCADE,
    FOREIGN KEY (mahasiswa_id) REFERENCES mahasiswa(id) ON DELETE CASCADE
);

CREATE TABLE logbook_bimbingan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT UNIQUE NOT NULL,
    catatan_revisi TEXT NOT NULL,
    progres_bab VARCHAR(50) NOT NULL,
    status_kelayakan ENUM('revisi', 'lanjut_bab_berikutnya', 'acc_sidang') NOT NULL,
    tanggal_bimbingan DATETIME NOT NULL,
    FOREIGN KEY (booking_id) REFERENCES bimbingan_booking(id) ON DELETE CASCADE
);
```

---
*Laporan ini disusun secara mandiri dan sistematis untuk memenuhi Ujian Tengah Semester (UTS) Rekayasa Perangkat Lunak Tahun Akademik 2026/2027.*
