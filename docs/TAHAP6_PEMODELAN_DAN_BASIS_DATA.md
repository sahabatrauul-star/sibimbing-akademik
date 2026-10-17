# TAHAP 6 — Pemodelan Sistem dan Perancangan Basis Data

**Mata Kuliah:** Rekayasa Perangkat Lunak  
**Proyek:** SiBimbing (Sistem Penjadwalan dan Monitoring Bimbingan Akademik)  
**Pengembang:** Raoul (NIM: 240104004)

---

## 6.1 Alur Proses Bisnis Bimbingan Akademik

Proses bisnis sistem SiBimbing dirancang melalui 5 tahapan utama:
1. **Inisialisasi Ketersediaan Jadwal:** Dosen pembimbing masuk ke sistem dan menginputkan tanggal, jam mulai, jam selesai, ruangan, dan kuota mahasiswa yang dapat diterima pada hari tersebut.
2. **Pemesanan Jadwal Bimbingan:** Mahasiswa login, memilih dosen pembimbing, melihat daftar slot waktu yang masih berstatus `tersedia`, lalu mengisi topik bahasan yang ingin dikonsultasikan. Sistem secara otomatis memverifikasi kuota dan mengunci slot.
3. **Verifikasi & Notifikasi:** Dosen meninjau ajuan bimbingan yang masuk. Dosen dapat menyetujui (*Approve*) atau menolak (*Reject* dengan menyertakan alasan). Mahasiswa menerima pembaruan status pada dashboard.
4. **Pelaksanaan Sesi & Pencatatan Logbook:** Bimbingan berlangsung sesuai jadwal. Setelah sesi berakhir, dosen membuka modul logbook untuk menuliskan ringkasan arahan revisi, progres bab (misal: Bab 1, Bab 2, dll.), serta rekomendasi kelayakan (*Revisi* / *Lanjut Bab* / *ACC Sidang*).
5. **Pemantauan & Rekapitulasi Progres:** Riwayat logbook tersimpan secara permanen pada rekam akademik mahasiswa. Admin/Koordinator program studi dapat memantau akumulasi total pertemuan untuk menentukan kelayakan mendaftar ujian sidang tugas akhir.

---

## 6.2 Context Diagram (Diagram Konteks / DFD Level 0)

Diagram Konteks memodelkan batasan sistem (*system boundary*) dan interaksi aliran data antara sistem SiBimbing dengan entitas eksternal:

```text
       +-------------------------------------------------------+
       |                                                       |
       |  ENTITAS: MAHASISWA                                   |
       |      |                                                |
       |      |-- 1. Data Login (NIM & Password)               |
       |      |-- 2. Permohonan Booking Slot Jadwal            |
       |      |-- 3. Data Topik Bahasan & Berkas Draft         |
       |      |                                                |
       |      |<-- A. Informasi Slot Waktu Dosen Tersedia      |
       |      |<-- B. Status Konfirmasi Booking (Disetujui/Ditolak)
       |      |<-- C. Kartu Logbook Riwayat Catatan Revisi     |
       |      |                                                |
       +------|------------------------------------------------+
              |
              v
   +===============================================================+
   |                                                               |
   |                  SISTEM INFORMASI SiBimbing                   |
   |        (Penjadwalan & Monitoring Bimbingan Akademik)          |
   |                                                               |
   +===============================================================+
              ^                                         ^
              |                                         |
       +------|-----------------------+   +-------------|-----------------------+
       |      |                       |   |             |                       |
       |  ENTITAS: DOSEN PEMBIMBING   |   |  ENTITAS: KOORDINATOR / ADMIN       |
       |      |                       |   |             |                       |
       |      |-- 1. Data Login Dosen |   |             |-- 1. Data Login Admin |
       |      |-- 2. Input Slot Jadwal|   |             |-- 2. Manajemen Master |
       |      |-- 3. Konfirmasi Booking                 |      User & Dosen     |
       |      |-- 4. Input Logbook &  |   |             |-- 3. Filter Rekapitulasi
       |      |      Catatan Evaluasi |   |             |      Syarat Sidang    |
       |      |                       |   |             |                       |
       |      |<-- A. Notifikasi Ajuan|   |             |<-- A. Laporan Progres |
       |      |<-- B. Profil Mahasiswa+-----------------+    Bimbingan Global   |
       +------------------------------+
```

---

## 6.3 Data Flow Diagram (DFD) Level 1

Pada DFD Level 1, sistem SiBimbing diuraikan ke dalam 4 proses fungsional utama:

1. **Proses 1.0 (Autentikasi & Manajemen Pengguna):**
   - Menerima input kredensial dari Mahasiswa, Dosen, dan Admin.
   - Melakukan verifikasi ke data store `users`.
   - Mengembalikan session data pengguna yang valid.
2. **Proses 2.0 (Pengelolaan Ketersediaan Slot Jadwal):**
   - Menerima input ketersediaan waktu dan kuota dari Dosen.
   - Menyimpan dan memperbarui data slot ke data store `jadwal_slot`.
   - Mengirimkan daftar jadwal aktif ke modul pencarian mahasiswa.
3. **Proses 3.0 (Reservasi & Verifikasi Jadwal Bimbingan):**
   - Menerima pemilihan slot dan topik konsultasi dari Mahasiswa.
   - Memeriksa sisa kuota pada `jadwal_slot`. Jika tersedia, sistem mencatat reservasi ke `bimbingan_booking` dan memperbarui kuota.
   - Mengirimkan data ajuan ke Dosen untuk konfirmasi (*Approved/Rejected*).
4. **Proses 4.0 (Pencatatan Logbook & Rekapitulasi Progres):**
   - Menerima input catatan revisi, progres bab, dan kelayakan dari Dosen.
   - Menyimpan hasil ke data store `logbook_bimbingan`.
   - Menghasilkan kartu kontrol bimbingan untuk Mahasiswa dan laporan rekapitulasi kelayakan sidang untuk Admin.

---

## 6.4 Kamus Data (*Data Dictionary*)

Berikut adalah spesifikasi detail atribut untuk setiap tabel basis data dalam sistem:

### 1. Tabel: `users`
* **Deskripsi:** Menyimpan kredensial autentikasi seluruh pengguna sistem.
* **Primary Key:** `id`
* **Atribut:**
  - `id` : INT(11), Auto Increment, Not Null &rarr; ID unik pengguna.
  - `username` : VARCHAR(50), Unique, Not Null &rarr; NIM (Mahasiswa), NIDN (Dosen), atau nama akun (Admin).
  - `password` : VARCHAR(255), Not Null &rarr; Kata sandi terenkripsi Bcrypt.
  - `role` : ENUM('admin', 'dosen', 'mahasiswa'), Not Null &rarr; Peran hak akses.
  - `created_at` : TIMESTAMP, Default CURRENT_TIMESTAMP &rarr; Waktu pendaftaran akun.
  - `updated_at` : TIMESTAMP, Default CURRENT_TIMESTAMP ON UPDATE &rarr; Waktu pembaruan akun.

### 2. Tabel: `dosen`
* **Deskripsi:** Menyimpan data biodata dosen pembimbing.
* **Primary Key:** `id`
* **Foreign Key:** `user_id` &rarr; Relasi ke `users(id)`
* **Atribut:**
  - `id` : INT(11), Auto Increment, Not Null &rarr; ID unik dosen.
  - `user_id` : INT(11), Not Null &rarr; ID akun login terkait.
  - `nidn` : VARCHAR(20), Unique, Not Null &rarr; Nomor Induk Dosen Nasional.
  - `nama_lengkap` : VARCHAR(100), Not Null &rarr; Nama dosen tanpa gelar.
  - `gelar` : VARCHAR(30), Not Null &rarr; Gelar akademis dosen.
  - `email` : VARCHAR(100), Not Null &rarr; Alamat email resmi dosen.
  - `no_hp` : VARCHAR(20), Not Null &rarr; Kontak WhatsApp/telepon dosen.
  - `kuota_maksimal_mhs` : INT(11), Default 10 &rarr; Batas maksimal mahasiswa yang dibimbing.

### 3. Tabel: `mahasiswa`
* **Deskripsi:** Menyimpan data akademik mahasiswa dan dosen pembimbingnya.
* **Primary Key:** `id`
* **Foreign Key:** `user_id` &rarr; `users(id)`, `dosen_pembimbing_id` &rarr; `dosen(id)`
* **Atribut:**
  - `id` : INT(11), Auto Increment, Not Null &rarr; ID unik mahasiswa.
  - `user_id` : INT(11), Not Null &rarr; ID akun login terkait.
  - `nim` : VARCHAR(20), Unique, Not Null &rarr; Nomor Induk Mahasiswa.
  - `nama_lengkap` : VARCHAR(100), Not Null &rarr; Nama lengkap mahasiswa.
  - `program_studi` : VARCHAR(50), Not Null &rarr; Program studi mahasiswa.
  - `angkatan` : VARCHAR(10), Not Null &rarr; Tahun angkatan kuliah.
  - `dosen_pembimbing_id` : INT(11), Nullable &rarr; ID dosen pembimbing utama.
  - `judul_tugas_akhir` : TEXT, Nullable &rarr; Rencana judul tugas akhir / skripsi.

### 4. Tabel: `jadwal_slot`
* **Deskripsi:** Menyimpan waktu ketersediaan bimbingan yang dibuka dosen.
* **Primary Key:** `id`
* **Foreign Key:** `dosen_id` &rarr; `dosen(id)`
* **Atribut:**
  - `id` : INT(11), Auto Increment, Not Null &rarr; ID unik slot jadwal.
  - `dosen_id` : INT(11), Not Null &rarr; ID dosen pemilik slot.
  - `tanggal` : DATE, Not Null &rarr; Tanggal bimbingan.
  - `jam_mulai` : TIME, Not Null &rarr; Waktu mulai bimbingan.
  - `jam_selesai` : TIME, Not Null &rarr; Waktu selesai bimbingan.
  - `kuota_mhs` : INT(11), Default 1 &rarr; Kapasitas kuota mahasiswa untuk sesi tersebut.
  - `sisa_kuota` : INT(11), Default 1 &rarr; Sisa kuota yang belum terisi.
  - `ruangan_lokasi` : VARCHAR(100), Not Null &rarr; Ruangan atau tautan tatap muka online.
  - `status_slot` : ENUM('tersedia', 'penuh', 'dibatalkan'), Default 'tersedia'.

### 5. Tabel: `bimbingan_booking`
* **Deskripsi:** Menyimpan transaksi permohonan bimbingan oleh mahasiswa.
* **Primary Key:** `id`
* **Foreign Key:** `slot_id` &rarr; `jadwal_slot(id)`, `mahasiswa_id` &rarr; `mahasiswa(id)`
* **Atribut:**
  - `id` : INT(11), Auto Increment, Not Null &rarr; ID transaksi booking.
  - `kode_booking` : VARCHAR(30), Unique, Not Null &rarr; Kode referensi booking unik.
  - `slot_id` : INT(11), Not Null &rarr; ID slot jadwal yang dipilih.
  - `mahasiswa_id` : INT(11), Not Null &rarr; ID mahasiswa yang mengajukan.
  - `topik_bahasan` : TEXT, Not Null &rarr; Rincian materi/bab yang ingin dibimbingkan.
  - `file_draft_url` : VARCHAR(255), Nullable &rarr; URL/path file berkas laporan yang diunggah.
  - `status_booking` : ENUM('menunggu', 'disetujui', 'ditolak', 'selesai'), Default 'menunggu'.
  - `alasan_penolakan`: TEXT, Nullable &rarr; Alasan jika ajuan ditolak dosen.
  - `created_at` : TIMESTAMP, Default CURRENT_TIMESTAMP.

### 6. Tabel: `logbook_bimbingan`
* **Deskripsi:** Menyimpan rekam evaluasi dan catatan arahan revisi bimbingan.
* **Primary Key:** `id`
* **Foreign Key:** `booking_id` &rarr; `bimbingan_booking(id)`
* **Atribut:**
  - `id` : INT(11), Auto Increment, Not Null &rarr; ID unik logbook.
  - `booking_id` : INT(11), Unique, Not Null &rarr; ID booking bimbingan terkait.
  - `catatan_revisi` : TEXT, Not Null &rarr; Rincian catatan revisi dan arahan dosen.
  - `progres_bab` : VARCHAR(50), Not Null &rarr; Posisi capaian bab (Bab 1 / Bab 2 / Bab 3 / Bab 4 / Alat).
  - `status_kelayakan`: ENUM('revisi', 'lanjut_bab_berikutnya', 'acc_sidang'), Not Null.
  - `tanggal_bimbingan`: DATETIME, Not Null &rarr; Waktu realisasi bimbingan berlangsung.
  - `created_at` : TIMESTAMP, Default CURRENT_TIMESTAMP.

---

## 6.5 Rancangan Relasi Antar Tabel (Entity Relationship Diagram Summary)

```text
  [users] 1 ──── 1 [dosen] 1 ──── N [jadwal_slot] 1 ──── N [bimbingan_booking] 1 ──── 1 [logbook_bimbingan]
     │                │                                         │
     │                └──────────────── 1 (pembimbing)          │
     │                                         │                │
     └──────── 1 ──── 1 [mahasiswa] 1 ─────────┴────────────────┘
```
1. `users` berelasi 1:1 ke `dosen` atau `mahasiswa`.
2. Satu `dosen` dapat membimbing banyak `mahasiswa` (1:N) dan dapat membuka banyak `jadwal_slot` (1:N).
3. Satu `jadwal_slot` dapat dipesan melalui beberapa transaksi `bimbingan_booking` (1:N) sesuai batas kuota.
4. Setiap transaksi `bimbingan_booking` yang telah selesai memiliki tepat satu record `logbook_bimbingan` (1:1).
