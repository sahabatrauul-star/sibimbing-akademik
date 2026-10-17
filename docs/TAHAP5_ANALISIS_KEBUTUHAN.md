# TAHAP 5 — Analisis Kebutuhan Perangkat Lunak

**Mata Kuliah:** Rekayasa Perangkat Lunak  
**Proyek:** SiBimbing (Sistem Penjadwalan dan Monitoring Bimbingan Akademik)  
**Pengembang:** Raoul (NIM: 240104004)

---

## 5.1 Identifikasi Stakeholders
Stakeholder adalah individu atau pihak yang terlibat dan terpengaruh langsung oleh penerapan sistem SiBimbing:

| No | Stakeholder | Peran & Tanggung Jawab dalam Sistem |
|---|---|---|
| 1 | **Mahasiswa** | Mengakses sistem untuk melihat jadwal ketersediaan dosen, memesan slot waktu bimbingan, mengisi topik bahasan/bab, mengunggah berkas rancangan, dan membaca riwayat catatan evaluasi revisi. |
| 2 | **Dosen Pembimbing** | Menentukan slot hari, jam, dan kuota bimbingan; meninjau ajuan janji temu mahasiswa (menerima/menolak); serta menginputkan evaluasi catatan revisi pada logbook setelah sesi bimbingan selesai. |
| 3 | **Koordinator Tugas Akhir / Admin Prodi** | Mengelola data master mahasiswa dan dosen, menetapkan relasi dosen pembimbing per mahasiswa, serta mengekspor laporan rekapitulasi progres bimbingan untuk kelayakan sidang tugas akhir. |

---

## 5.2 Kebutuhan Fungsional (*Functional Requirements - FR*)

| Kode Kebutuhan | Nama Kebutuhan | Deskripsi Alur & Logika Sistem |
|---|---|---|
| **FR-01** | Autentikasi Multi-User | Sistem harus mampu memvalidasi kredensial login pengguna (username & password) dan mengarahkan ke dashboard yang sesuai (Mahasiswa, Dosen, Admin). |
| **FR-02** | Manajemen Slot Jadwal | Dosen dapat membuat, mengubah, dan membatalkan slot waktu bimbingan (tanggal, jam mulai, jam selesai, kuota mahasiswa, ruangan). |
| **FR-03** | Pencarian & Filter Jadwal | Mahasiswa dapat mencari dan memfilter slot waktu bimbingan berdasarkan nama dosen pembimbing dan rentang tanggal. |
| **FR-04** | Pengajuan Reservasi Jadwal | Mahasiswa dapat memilih slot yang berstatus *tersedia*, mengisi topik bahasan, dan mengajukan janji bimbingan. Sistem otomatis mengurangi kuota slot. |
| **FR-05** | Konfirmasi Bimbingan oleh Dosen | Dosen dapat menyetujui (*Approve*) atau menolak (*Reject* disertai alasan penolakan) permohonan bimbingan yang diajukan mahasiswa. |
| **FR-06** | Pengelolaan E-Logbook Bimbingan | Setelah sesi bimbingan selesai, dosen menginput catatan hasil bimbingan, progres bab (Bab 1/2/3/Alat), dan status kelayakan (*Revisi* / *Lanjut Bab* / *ACC Sidang*). |
| **FR-07** | Kartu Kontrol Digital Mahasiswa | Mahasiswa dapat melihat histori kronologis seluruh sesi bimbingan yang telah disetujui dan dinilai oleh dosen pembimbing. |
| **FR-08** | Laporan Rekapitulasi Akademik | Admin dan dosen dapat menghasilkan rekapitulasi jumlah bimbingan mahasiswa (misal: syarat minimal 8 kali bimbingan sebelum sidang akhir). |

---

## 5.3 Kebutuhan Non-Fungsional (*Non-Functional Requirements - NFR*)

1. **Keamanan (*Security*):**
   - Kata sandi pengguna harus dienkripsi menggunakan algoritma hashing standar industri (Bcrypt).
   - Mencegah serangan *SQL Injection* menggunakan Prepared Statements dan *Cross-Site Scripting (XSS)* dengan escaping data output.
2. **Kinerja (*Performance*):**
   - Waktu respon halaman untuk pencarian jadwal dan submit booking tidak boleh melebihi 2 detik pada koneksi internet standar.
3. **Ketersediaan (*Availability*):**
   - Sistem dapat diakses 24/7 melalui peramban web modern (Google Chrome, Mozilla Firefox, Microsoft Edge, Safari) tanpa membutuhkan instalasi aplikasi tambahan.
4. **Keandalan & Integritas (*Reliability & Integrity*):**
   - Sistem menerapkan mekanisme transaksi basis data (*ACID Transaction*) saat pemilihan slot jadwal guna menjamin kuota tidak terambil ganda (*anti-concurrency conflict*).

---

## 5.4 Penentuan Prioritas Kebutuhan (Metode MoSCoW)

Untuk memfasilitasi pengembangan bertahap dan memastikan fungsionalitas inti selesai tepat waktu, kebutuhan fungsional dikelompokkan dengan metode MoSCoW:

### 1. Must Have (Wajib Ada — Kritis untuk Keberhasilan Sistem)
* **FR-01:** Autentikasi Pengguna berdasarkan peran.
* **FR-02:** Pembuatan slot jadwal ketersediaan waktu oleh Dosen.
* **FR-04:** Pengajuan reservasi bimbingan dengan validasi kuota oleh Mahasiswa.
* **FR-05:** Fitur persetujuan / penolakan jadwal oleh Dosen.
* **FR-06:** Pencatatan logbook revisi dan progres bimbingan.

### 2. Should Have (Penting tapi ada solusi alternatif sementara)
* **FR-03:** Fitur filter dan pencarian jadwal bimbingan.
* **FR-07:** Tampilan kartu kendali bimbingan digital terpadu bagi Mahasiswa.
* **FR-08:** Rekapitulasi frekuensi bimbingan untuk syarat sidang.

### 3. Could Have (Fitur pelengkap jika sumber daya dan waktu memungkinkan)
* Notifikasi email atau WhatsApp Gateway otomatis saat status bimbingan berubah.
* Fitur upload lampiran berkas draft laporan (format .pdf / .docx) ke penyimpanan server.
* Kalender interaktif grafis (*interactive visual calendar*).

### 4. Won't Have (Ditunda ke versi masa depan / *Future Release*)
* Fitur ruang tatap muka video conference bawaan (*built-in WebRTC video call*).
* Fitur integrasi tanda tangan digital kriptografi berbasis sertifikat Balai Sertifikasi Elektronik (BSrE).
