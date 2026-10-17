# TAHAP 4 — Perencanaan Pengembangan dengan SDLC

**Mata Kuliah:** Rekayasa Perangkat Lunak  
**Proyek:** SiBimbing (Sistem Penjadwalan dan Monitoring Bimbingan Akademik)  
**Pengembang:** Raoul (NIM: 240104004)

---

## 4.1 Project Charter

| Komponen Charter | Uraian Lengkap |
|---|---|
| **Nama Proyek** | SiBimbing (Sistem Penjadwalan dan Monitoring Bimbingan Akademik Berbasis Web) |
| **Deskripsi Masalah** | Pengaturan janji temu bimbingan tugas akhir selama ini tidak terpusat, mengandalkan pesan chat pribadi yang sering tenggelam, mengakibatkan bentrok jadwal bimbingan dan tidak adanya dokumentasi logbook revisi yang dapat dipertanggungjawabkan. |
| **Tujuan Proyek** | Menyediakan platform web terpadu untuk otomasi reservasi slot jadwal bimbingan dosen, memvalidasi kuota dan bentrok waktu secara sistematis, serta menyediakan catatan digital evaluasi/revisi (*e-logbook*). |
| **Sasaran Pengguna** | 1. Mahasiswa D3 Teknik Komputer.<br>2. Dosen Pembimbing Akademik & Tugas Akhir.<br>3. Admin / Koordinator Tugas Akhir Program Studi. |
| **Ruang Lingkup (In-Scope)** | • Manajemen autentikasi berbasis multi-role (Mahasiswa, Dosen, Admin).<br>• Manajemen master slot jadwal ketersediaan waktu oleh Dosen.<br>• Fitur pencarian dan pengajuan jadwal bimbingan oleh Mahasiswa.<br>• Fitur verifikasi (Approve/Reject) jadwal bimbingan oleh Dosen.<br>• Fitur pencatatan logbook revisi, status kelayakan bab, dan rekapitulasi keaktifan bimbingan. |
| **Batasan (Out-of-Scope)** | • Pembayaran administrasi bimbingan / SPP.<br>• Integrasi video conference otomatis (Zoom/GMeet live stream API).<br>• Tanda tangan digital bersertifikat kriptografi (disimpan sebagai status persetujuan sistem). |
| **Analisis Risiko & Mitigasi** | 1. **Risiko:** Dosen tidak sempat membuka sistem untuk membalas ajuan.<br>&bull; **Mitigasi:** Batas waktu konfirmasi otomatis (*auto-reschedule*) 24 jam sebelum jadwal berlangsung.<br>2. **Risiko:** Terjadinya *double-booking* pada detik yang sama oleh dua mahasiswa.<br>&bull; **Mitigasi:** Penerapan *database transaction locking* dan pengecekan sisa kuota pada level server.<br>3. **Risiko:** Kehilangan data logbook revisi.<br>&bull; **Mitigasi:** Penerapan backup basis data otomatis berkala (*cron database dump*). |

---

## 4.2 Pemilihan Model SDLC dan Alasan Pemilihannya

Untuk pengembangan sistem **SiBimbing**, model SDLC yang dipilih adalah **Waterfall Model** (Sekuensial Linier).

### Alasan Pemilihan Model Waterfall:
1. **Kebutuhan Sistem Sangat Jelas dan Baku (*Stable Requirements*):**
   Alur kerja proses bimbingan akademik di perguruan tinggi sudah memiliki regulasi dan Standar Operasional Prosedur (SOP) akademik yang pasti (Dosen membuka waktu &rarr; Mahasiswa mendaftar &rarr; Bimbingan dilaksanakan &rarr; Catatan revisi diisi). Tidak ada perubahan mendasar pada aturan bisnis selama pengembangan.
2. **Kesesuaian Karakter Proyek Akademik (UTS/UAS):**
   Model Waterfall menekankan dokumentasi yang terstruktur pada setiap tahapan (analisis kebutuhan, perancangan arsitektur, desain basis data, implementasi kode, pengujian). Hal ini sangat ideal untuk evaluasi akademik karena penguji dapat menilai kualitas setiap artefak dokumen secara runtut.
3. **Pengelolaan Kualitas & Kontrol (*Quality Assurance Gate*):**
   Setiap fase memiliki titik persetujuan (*milestone approval*) yang jelas sebelum melangkah ke fase berikutnya. Dengan demikian, perancangan database dan diagram konteks dapat dipastikan matang sebelum menulis kode program lengkap, meminimalisir kesalahan perancangan ulang (*cost of rework*).

### Tahapan Penerapan Waterfall pada SiBimbing:
```text
[1. Requirements Analysis]  ==> Mengidentifikasi kebutuhan fungsional & non-fungsional
          │
          ▼
   [2. System Design]       ==> Merancang Context Diagram, DFD, & Skema Basis Data SQL
          │
          ▼
 [3. Implementation (Coding)]==> Membangun modul backend PHP & frontend interface
          │
          ▼
    [4. Testing (QA)]       ==> Pengujian logika slot bimbingan & validasi sistem
          │
          ▼
  [5. Deployment & Maint.]  ==> Publikasi sistem ke hosting & pemeliharaan server
```
