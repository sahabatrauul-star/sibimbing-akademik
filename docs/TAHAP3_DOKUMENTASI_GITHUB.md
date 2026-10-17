# TAHAP 3 — Pengelolaan Proyek Menggunakan GitHub

**Mata Kuliah:** Rekayasa Perangkat Lunak  
**Proyek:** SiBimbing (Sistem Penjadwalan dan Monitoring Bimbingan Akademik)  
**Pengembang:** Raoul (NIM: 240104004)

---

## 3.1 Menghubungkan Repositori Lokal ke GitHub

Untuk mendokumentasikan seluruh pekerjaan secara online, repositori lokal dihubungkan ke GitHub dengan langkah-langkah berikut:

1. Membuat repositori baru di GitHub dengan nama: `sibimbing-akademik`.
2. Menyetel branch utama menjadi `main`:
   ```bash
   git branch -M main
   ```
3. Menambahkan remote URL GitHub:
   ```bash
   git remote add origin https://github.com/raoulaswar/sibimbing-akademik.git
   ```
4. Melakukan push seluruh histori commit lokal ke branch `main`:
   ```bash
   git push -u origin main
   ```

---

## 3.2 Pembuatan Feature Branch, Push, dan Pull Request (PR)

Dalam metodologi pengembangan perangkat lunak modern, penambahan modul baru wajib dilakukan pada branch terpisah (*feature branch*) guna menjaga kestabilan kode di branch `main`.

### Langkah Pembuatan Feature Branch:
1. **Membuat dan berpindah ke branch fitur baru:**
   ```bash
   git checkout -b feature/modul-penjadwalan
   ```
2. **Mengembangkan modul antarmuka jadwal dosen (`jadwal.php`):**
   ```bash
   git add jadwal.php
   git commit -m "feat: tambahkan halaman jadwal ketersediaan dosen (feature/modul-penjadwalan)"
   ```
3. **Mendorong (*push*) branch fitur ke repositori GitHub:**
   ```bash
   git push origin feature/modul-penjadwalan
   ```

### Alur Pull Request (PR) di GitHub:
1. Membuka halaman repositori di GitHub.
2. Memilih tombol **Compare & pull request** untuk branch `feature/modul-penjadwalan`.
3. Mengisi judul PR: `feat: Integrasi Modul Tampilan Jadwal Dosen Pembimbing`.
4. Mengisi deskripsi PR:
   > *Pull request ini menambahkan antarmuka baru `jadwal.php` untuk menampilkan daftar dosen pembimbing, bidang keahlian, dan jadwal ketersediaan waktu bimbingan.*
5. Meninjau perubahan kode (*diff review*) dan menyetujui penggabungan via **Merge pull request** ke branch `main`.

---

## 3.3 Simulasi Konflik Git dan Dokumentasi Penyelesaiannya

Konflik Git (*merge conflict*) terjadi ketika dua branch berbeda mengubah baris yang sama pada file yang sama dengan konten berbeda sebelum proses penggabungan.

### 1. Skenario Pemicu Konflik:
- **Pada branch `feature/modul-penjadwalan`:**
  Dilakukan modifikasi baris informasi dosen di `README.md` menjadi:
  `**Dosen Pengampu:** Novemy Triyandari N, SE, MM [Feature Branch Update v1.1.0]`
  dan di-commit dengan pesan: `chore(feature): update informasi versi pada branch feature`.

- **Pada branch `main`:**
  Secara bersamaan pada baris yang persis sama, diubah menjadi:
  `**Dosen Pengampu:** Novemy Triyandari N, SE, MM [Main Branch Update v1.0.1]`
  dan di-commit dengan pesan: `chore(main): update informasi versi pada branch main`.

### 2. Terjadinya Konflik Saat Penggabungan:
Ketika dilakukan perintah penggabungan branch:
```bash
git checkout main
git merge feature/modul-penjadwalan
```

**Hasil Keluaran Terminal:**
```text
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

### 3. Tampilan Penanda Konflik (*Conflict Markers*) di File:
Ketika file `README.md` dibuka, Git menandai baris yang bertabrakan dengan format:
```text
<<<<<<< HEAD
**Dosen Pengampu:** Novemy Triyandari N, SE, MM [Main Branch Update v1.0.1]  
=======
**Dosen Pengampu:** Novemy Triyandari N, SE, MM [Feature Branch Update v1.1.0]  
>>>>>>> feature/modul-penjadwalan
```

### 4. Langkah Penyelesaian Konflik:
1. Pengembang membuka file `README.md` dan mendiskusikan nilai final yang disepakati.
2. Menghapus penanda konflik (`<<<<<<< HEAD`, `=======`, `>>>>>>>`) dan menetapkan teks resmi:
   ```markdown
   **Dosen Pengampu:** Novemy Triyandari N, SE, MM / Tim Dosen RPL UDB
   ```
3. Menandai file sebagai selesai diselesaikan (*resolved*):
   ```bash
   git add README.md
   ```
4. Melakukan commit penyelesaian penggabungan (*merge commit*):
   ```bash
   git commit -m "merge: selesaikan konflik versi pada README.md dan gabungkan feature/modul-penjadwalan ke main"
   ```

### 5. Bukti Riwayat Git Graph Setelah Merge Berhasil:
```text
*   489f0bb (HEAD -> main) merge: selesaikan konflik versi pada README.md dan gabungkan feature/modul-penjadwalan ke main
|\  
| * cbface3 (feature/modul-penjadwalan) chore(feature): update informasi versi pada branch feature
| * f2e2d0c feat: tambahkan halaman jadwal ketersediaan dosen (feature/modul-penjadwalan)
* | 1542cf5 chore(main): update informasi versi pada branch main
|/  
* 6044b73 docs: tambahkan dokumentasi riwayat git dan pembuktian git restore (Tahap 2)
* f6d0bac design: pemodelan proses bisnis, diagram konteks, kamus data, dan DDL basis data (Tahap 6)
* 15f1f58 docs: analisis kebutuhan fungsional, non-fungsional, dan prioritas MoSCoW (Tahap 5)
* e40908b docs: susun perencanaan SDLC Waterfall dan Project Charter lengkap (Tahap 4)
* b807505 feat: tambahkan identifikasi masalah dan implementasi prototipe PHP (Tahap 1)
* ef64f6a chore: inisialisasi repositori Git dan konfigurasi .gitignore (Tahap 2)
```

**Kesimpulan:** Simulasi konflik berhasil dipicu, ditangani secara sistematis, dan digabungkan kembali ke branch `main` tanpa kehilangan riwayat kerja.
