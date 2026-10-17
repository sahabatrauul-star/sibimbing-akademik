# TAHAP 1 — Identifikasi Masalah dan Persiapan Proyek

**Mata Kuliah:** Rekayasa Perangkat Lunak  
**Program Studi / Kelas:** D3 Teknik Komputer / D3TK24A1  
**Nama Mahasiswa:** Raoul  
**NIM:** 240104004  
**Judul Proyek:** Sistem Penjadwalan dan Monitoring Bimbingan Akademik (SiBimbing)

---

## 1.1 Latar Belakang Masalah
Bimbingan akademik dan bimbingan Tugas Akhir (TA) merupakan tahapan krusial dalam perjalanan studi mahasiswa diploma maupun sarjana. Selama ini, koordinasi jadwal temu bimbingan antara dosen pembimbing dan mahasiswa masih mengandalkan saluran komunikasi personal non-formal seperti pesan WhatsApp atau Telegram. 

Metode konvensional ini kerap menimbulkan sejumlah kendala:
1. **Pesan Tenggelam & Lambat Direspon:** Banyaknya pesan yang masuk ke nomor pribadi dosen menyebabkan permohonan bimbingan mahasiswa terlewat.
2. **Jadwal Bentrok (*Clashing*):** Tidak adanya kalender ketersediaan dosen yang terpusat menyebabkan beberapa mahasiswa datang di jam yang sama atau mendatangi ruangan saat dosen sedang mengajar atau bertugas di luar kampus.
3. **Catatan Bimbingan Tercecer (*Lost Feedback*):** Lembar catatan fisik (kartu bimbingan kertas) rentan hilang, rusak, atau lupa dibawa, sehingga riwayat revisi dan arahan bimbingan sebelumnya tidak terpantau secara berkesinambungan.

Oleh karena itu, diperlukan sebuah perangkat lunak berbasis web bernama **SiBimbing** untuk mengotomasi pengelolaan jadwal temu serta mendokumentasikan logbook bimbingan secara digital dan terstruktur.

---

## 1.2 Rumusan Masalah
1. Bagaimana merancang sistem yang dapat menampilkan slot ketersediaan waktu dosen pembimbing secara real-time untuk mencegah jadwal bentrok?
2. Bagaimana memfasilitasi mahasiswa dalam mengajukan janji bimbingan dan mengunggah draft bahasan secara transparan?
3. Bagaimana membangun fitur pencatatan logbook revisi digital yang dapat diakses oleh mahasiswa, dosen pembimbing, dan koordinator akademik?

---

## 1.3 Tujuan Proyek
1. Mengembangkan sistem informasi berbasis web untuk penjadwalan bimbingan yang teratur dan transparan.
2. Menyediakan modul reservasi slot bimbingan dengan validasi kuota otomatis.
3. Membangun sistem monitoring logbook revisi akademik guna memantau progres tugas akhir mahasiswa secara akuntabel.
4. Memudahkan pihak program studi dalam merekapitulasi frekuensi bimbingan sebagai syarat pendaftaran sidang.

---

## 1.4 Sasaran Pengguna Sistem (*User Persona*)
1. **Mahasiswa:**
   - Melihat slot ketersediaan waktu dosen pembimbing.
   - Mengajukan reservasi jadwal bimbingan dengan menyertakan topik bahasan.
   - Melihat riwayat arahan revisi dari dosen di logbook digital.
2. **Dosen Pembimbing:**
   - Mengelola dan membuka slot waktu bimbingan sesuai jam kerja/ketersediaan.
   - Mengonfirmasi (menerima/menolak) pengajuan jadwal bimbingan.
   - Memberikan catatan evaluasi revisi dan menentukan kelayakan progres bab mahasiswa.
3. **Admin / Koordinator Akademik:**
   - Mengelola data master pengguna (dosen dan mahasiswa).
   - Memantau rekapitulasi keaktifan bimbingan seluruh mahasiswa sebagai prasyarat ujian sidang.

---

## 1.5 Implementasi Prototipe Logika Sistem (`index.php`)
Sebagai pemenuhan Tahap 1, telah dibangun halaman PHP sederhana `index.php` yang memuat:
1. Header informasi resmi proyek, identitas pengembang, dan status tahapan SDLC.
2. Tabel dinamis ketersediaan slot waktu bimbingan dosen beserta sisa kuota.
3. Formulir pengajuan bimbingan interaktif (Nama, NIM, Pilihan Slot Dosen, dan Topik).
4. **Logika Bisnis PHP:**
   - Validasi kelengkapan data masukan.
   - Pengecekan sisa kuota slot dosen. Jika kuota = 0, sistem otomatis memberikan status **"DITOLAK (SLOT PENUH)"**. Jika kuota > 0, sistem memberikan status **"DISETUJUI (SLOT TERKUNCI)"**.
