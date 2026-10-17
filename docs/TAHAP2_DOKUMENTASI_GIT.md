# TAHAP 2 — Version Control Menggunakan Git

**Mata Kuliah:** Rekayasa Perangkat Lunak  
**Proyek:** SiBimbing (Sistem Penjadwalan dan Monitoring Bimbingan Akademik)  
**Pengembang:** Raoul (NIM: 240104004)

---

## 2.1 Inisialisasi Repositori dan Konfigurasi `.gitignore`

Inisialisasi repositori Git lokal dilakukan menggunakan perintah:
```bash
git init
git branch -M main
```

File `.gitignore` dibuat untuk menyaring file dependensi, log, file sistem operasi, dan file konfigurasi lokal agar tidak terunggah:

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

---

## 2.2 Riwayat Minimal 5 Commit yang Bermakna

Repositori dikelola dengan pesan commit terstruktur mengikuti konvensi *Conventional Commits*:

1. **Commit 1:**
   - **Hash:** `ef64f6a`
   - **Pesan:** `chore: inisialisasi repositori Git dan konfigurasi .gitignore (Tahap 2)`
   - **Cakupan:** Pembuatan file dasar repositori `.gitignore` dan `README.md`.
2. **Commit 2:**
   - **Hash:** `b807505`
   - **Pesan:** `feat: tambahkan identifikasi masalah dan implementasi prototipe PHP (Tahap 1)`
   - **Cakupan:** Pembuatan file `docs/TAHAP1_IDENTIFIKASI_MASALAH.md` dan file prototipe `index.php`.
3. **Commit 3:**
   - **Hash:** `e40908b`
   - **Pesan:** `docs: susun perencanaan SDLC Waterfall dan Project Charter lengkap (Tahap 4)`
   - **Cakupan:** Pembuatan dokumen charter proyek, ruang lingkup, analisis risiko, dan justifikasi model Waterfall.
4. **Commit 4:**
   - **Hash:** `15f1f58`
   - **Pesan:** `docs: analisis kebutuhan fungsional, non-fungsional, dan prioritas MoSCoW (Tahap 5)`
   - **Cakupan:** Spesifikasi stakeholder, daftar kebutuhan FR-01 s/d FR-08, NFR, dan matriks prioritas MoSCoW.
5. **Commit 5:**
   - **Hash:** `f6d0bac`
   - **Pesan:** `design: pemodelan proses bisnis, diagram konteks, kamus data, dan DDL basis data (Tahap 6)`
   - **Cakupan:** Pemodelan proses bisnis, Context Diagram DFD Level 0, DFD Level 1, kamus data, dan skema SQL `database/schema.sql`.

---

## 2.3 Dokumentasi Riwayat Perubahan (`git log`)

Eksekusi perintah grafis log:
```bash
git log --oneline --graph --decorate
```

**Hasil Keluaran Terminal Real:**
```text
* f6d0bac (HEAD -> main) design: pemodelan proses bisnis, diagram konteks, kamus data, dan DDL basis data (Tahap 6)
* 15f1f58 docs: analisis kebutuhan fungsional, non-fungsional, dan prioritas MoSCoW (Tahap 5)
* e40908b docs: susun perencanaan SDLC Waterfall dan Project Charter lengkap (Tahap 4)
* b807505 feat: tambahkan identifikasi masalah dan implementasi prototipe PHP (Tahap 1)
* ef64f6a chore: inisialisasi repositori Git dan konfigurasi .gitignore (Tahap 2)
```

---

## 2.4 Demonstrasi Pemulihan Perubahan Menggunakan `git restore`

Perintah `git restore` digunakan untuk membatalkan perubahan yang belum di-stage pada direktori kerja (*working directory*) kembali ke kondisi commit terakhir.

### Skenario Pengujian:
1. **Langkah 1: Menambahkan modifikasi yang tidak diinginkan pada `index.php`**
   ```bash
   echo "// Baris uji coba kesalahan edit oleh developer" >> index.php
   ```
2. **Langkah 2: Memeriksa status repositori**
   ```bash
   git status
   ```
   *Output terminal:*
   ```text
   On branch main
   Changes not staged for commit:
     (use "git add <file>..." to update what will be committed)
     (use "git restore <file>..." to discard changes in working directory)
           modified:   index.php
   ```
3. **Langkah 3: Menjalankan pemulihan file menggunakan `git restore`**
   ```bash
   git restore index.php
   ```
4. **Langkah 4: Memverifikasi kembali status direktori kerja**
   ```bash
   git status
   ```
   *Output terminal:*
   ```text
   On branch main
   nothing to commit, working tree clean
   ```
**Kesimpulan Demonstrasi:** File `index.php` berhasil dipulihkan secara instan ke kondisi commit bersih tanpa merusak riwayat git.
