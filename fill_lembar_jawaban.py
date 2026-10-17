import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
import shutil

src_template = "C:/Users/asus/AppData/Local/hermes/cache/documents/doc_a00c468f9b7d_Lembar_Jawaban_UTS_RPL-Proyek_Mandiri.docx"
output_docx = "C:/Users/asus/sibimbing-akademik/Lembar_Jawaban_UTS_RPL_Raoul_240104004.docx"

shutil.copyfile(src_template, output_docx)
doc = docx.Document(output_docx)

def set_cell(cell, text, bold=False, color=None, font_size=10):
    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(font_size)
    run.font.bold = bold
    if color:
        run.font.color.rgb = color

def set_image_cell(cell, image_path, caption, width=Inches(5.2)):
    cell.text = ""
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    run.add_picture(image_path, width=width)
    p2 = cell.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r2 = p2.add_run(caption)
    r2.font.name = "Calibri"
    r2.font.size = Pt(9)
    r2.font.italic = True
    r2.font.color.rgb = RGBColor(100, 116, 139)

# ==========================================
# Table 0: Identitas dan Topik Proyek
# ==========================================
t0 = doc.tables[0]
set_cell(t0.rows[0].cells[1], "Raoul", bold=True)
set_cell(t0.rows[1].cells[1], "240104004", bold=True)
set_cell(t0.rows[2].cells[1], "D3 Teknik Komputer / D3TK24A1 (Semester Ganjil 2026/2027)")
set_cell(t0.rows[3].cells[1], "SiBimbing - Sistem Penjadwalan dan Monitoring Bimbingan Akademik", bold=True)
set_cell(t0.rows[4].cells[1], "Otomasi reservasi slot jadwal bimbingan dosen untuk mencegah bentrok jadwal dan pencatatan riwayat revisi digital (e-logbook) tugas akhir secara terstruktur.")
set_cell(t0.rows[5].cells[1], "https://github.com/sahabatrauul-star/sibimbing-akademik", bold=True, color=RGBColor(37, 99, 235))

# ==========================================
# Table 2: 1.1 Gambaran Permasalahan
# ==========================================
t2 = doc.tables[2]
set_cell(t2.rows[0].cells[1], "Proses koordinasi janji bimbingan akademik dan tugas akhir selama ini masih dilakukan secara manual dan informal melalui aplikasi pesan pribadi (WhatsApp/Telegram). Mahasiswa kesulitan mengetahui waktu luang dosen pembimbing secara pasti, pesan pengajuan jadwal kerap tertumpuk atau lambat direspon, sering terjadi jadwal bentrok antar-mahasiswa, serta lembar bimbingan fisik konvensional rentan tercecer atau hilang.")
set_cell(t2.rows[1].cells[1], "Belum adanya sistem informasi terpusat yang mempublikasikan slot waktu bimbingan dosen secara real-time, serta proses monitoring catatan revisi bimbingan akademik masih mengandalkan kartu kendali berbasis kertas fisik.")
set_cell(t2.rows[2].cells[1], "Mahasiswa sering mendatangi kampus saat dosen sedang tidak berada di ruangan atau sedang mengajar, terjadinya antrean panjang bimbingan pada waktu yang sama, serta riwayat revisi tugas akhir tidak terdokumentasi rapi sehingga menyulitkan evaluasi progres kelayakan sidang tugas akhir.")
set_cell(t2.rows[3].cells[1], "Membangun sistem informasi web SiBimbing untuk mengotomasi pendaftaran jadwal bimbingan akademik secara transparan, menerapkan validasi sisa kuota slot secara otomatis guna mencegah jadwal bertabrakan, serta menyediakan e-logbook catatan revisi bimbingan digital.")
set_cell(t2.rows[4].cells[1], "1. Mahasiswa: Melihat ketersediaan jadwal, mengajukan reservasi slot bimbingan, mengisi topik bahasan, dan memantau evaluasi logbook revisi.\n2. Dosen Pembimbing: Membuka dan mengelola slot waktu, meninjau permohonan bimbingan (menerima/menolak), serta mengisi catatan logbook bimbingan.\n3. Koordinator / Admin: Mengelola data master serta memantau rekapitulasi keaktifan bimbingan sebagai syarat pendaftaran sidang akhir.")

# ==========================================
# Table 3: 1.2 Persiapan Lingkungan Kerja
# ==========================================
t3 = doc.tables[3]
set_cell(t3.rows[1].cells[1], "sibimbing-akademik/\n├── api/ (index.php, jadwal.php)\n├── database/ (schema.sql)\n├── docs/ (TAHAP1 s/d TAHAP6, LAPORAN_LENGKAP.md, images/)\n├── index.php, jadwal.php, vercel.json, .gitignore, README.md")
set_cell(t3.rows[2].cells[1], "PHP v8.2.12 (CLI) lokal, dan deployment Serverless PHP Runtime (vercel-php) aktif pada: https://sibimbing-akademik.vercel.app")
set_cell(t3.rows[3].cells[1], "Visual Studio Code (Editor kode sumber), Git Bash v2.53 (Version Control), GitHub CLI v2.102, MySQL / MariaDB (Basis data), Browser Google Chrome / Edge.")

# ==========================================
# Table 4: Bukti Halaman PHP Berjalan
# ==========================================
t4 = doc.tables[4]
set_image_cell(t4.rows[1].cells[0], "C:/Users/asus/sibimbing-akademik/docs/images/screenshot_app_home.png", "Gambar 1.1: Tampilan antarmuka prototipe SiBimbing yang telah aktif berjalan pada https://sibimbing-akademik.vercel.app, dilengkapi simulasi validasi kuota slot bimbingan.")

# ==========================================
# Table 5: 2.1 Persiapan Repository
# ==========================================
t5 = doc.tables[5]
set_cell(t5.rows[0].cells[1], "C:\\Users\\asus\\sibimbing-akademik (Branch: main)")
set_cell(t5.rows[1].cells[1], "/vendor/, /node_modules/, .env, config.local.php, *.log, .vscode/, .idea/, .DS_Store, Thumbs.db, .vercel")

# ==========================================
# Table 6: 2.2 Riwayat Commit
# ==========================================
t6 = doc.tables[6]
commits = [
    ("chore: inisialisasi repositori Git dan konfigurasi .gitignore (Tahap 2)", "Pembuatan berkas konfigurasi .gitignore dan file dokumentasi utama README.md."),
    ("feat: tambahkan identifikasi masalah dan implementasi prototipe PHP (Tahap 1)", "Pembuatan dokumen TAHAP1_IDENTIFIKASI_MASALAH.md serta pengkodean antarmuka dan logika validasi kuota pada index.php."),
    ("docs: susun perencanaan SDLC Waterfall dan Project Charter lengkap (Tahap 4)", "Penyusunan Project Charter (masalah, tujuan, batasan ruang lingkup, risiko) dan justifikasi pemilihan model Waterfall."),
    ("docs: analisis kebutuhan fungsional, non-fungsional, dan prioritas MoSCoW (Tahap 5)", "Identifikasi stakeholder, perumusan 8 Kebutuhan Fungsional (FR-01 s/d FR-08), NFR, dan matriks prioritas MoSCoW."),
    ("design: pemodelan proses bisnis, diagram konteks, kamus data, dan DDL basis data (Tahap 6)", "Pemodelan proses bisnis bimbingan, Context Diagram DFD Level 0, DFD Level 1, kamus data, dan skema SQL database/schema.sql.")
]
for idx, (msg, desc) in enumerate(commits, start=1):
    set_cell(t6.rows[idx].cells[1], msg, bold=True)
    set_cell(t6.rows[idx].cells[2], desc)

# ==========================================
# Table 7: 2.3 Pemeriksaan dan Pemulihan Perubahan
# ==========================================
t7 = doc.tables[7]
set_cell(t7.rows[0].cells[1], "git status (memeriksa kondisi working tree dan staging) dan git log --oneline --graph --decorate (melihat riwayat commit grafis).")
set_cell(t7.rows[1].cells[1], "File index.php (dilakukan perubahan baris uji coba yang sengaja dibuat keliru).")
set_cell(t7.rows[2].cells[1], "git restore index.php")
set_cell(t7.rows[3].cells[1], "Sebelum perintah restore, file index.php terdeteksi berstatus 'modified' pada working tree. Setelah perintah git restore index.php dijalankan, seluruh modifikasi yang belum di-commit dibatalkan dan status kembali bersih ('nothing to commit, working tree clean').")

# ==========================================
# Table 8: Bukti Riwayat Commit dan Pemulihan
# ==========================================
t8 = doc.tables[8]
set_image_cell(t8.rows[1].cells[0], "C:/Users/asus/sibimbing-akademik/docs/images/git_commit_restore.png", "Gambar 2.1: Bukti riwayat commit terstruktur (git log) dan demonstrasi pembatalan perubahan tidak sah menggunakan perintah git restore index.php.")

# ==========================================
# Table 9: 3.1 Pengelolaan Repository Jarak Jauh
# ==========================================
t9 = doc.tables[9]
set_cell(t9.rows[0].cells[1], "https://github.com/sahabatrauul-star/sibimbing-akademik", bold=True, color=RGBColor(37, 99, 235))
set_cell(t9.rows[1].cells[1], "main", bold=True)
set_cell(t9.rows[2].cells[1], "feature/modul-penjadwalan (dan feature/tambah-kontak-dosen)", bold=True)
set_cell(t9.rows[3].cells[1], "https://github.com/sahabatrauul-star/sibimbing-akademik/pull/1", bold=True, color=RGBColor(37, 99, 235))

# ==========================================
# Table 10: 3.2 Ringkasan Perubahan
# ==========================================
t10 = doc.tables[10]
set_cell(t10.rows[0].cells[1], "Mengembangkan modul baru ketersediaan jadwal dosen pembimbing (jadwal.php) dan informasi kontak pada branch terpisah agar tidak mengganggu branch main yang stabil.")
set_cell(t10.rows[1].cells[1], "Penambahan antarmuka jadwal dosen pembimbing, rincian bidang keahlian, hari ketersediaan, serta tautan kontak WhatsApp dosen. Diperiksa melalui peninjauan perubahan kode (diff review) dan pengujian tautan navigasi.")
set_cell(t10.rows[2].cells[1], "Pull Request #1 berstatus MERGED (berhasil digabungkan secara utuh ke branch main di GitHub).")

# ==========================================
# Table 11: 3.3 Simulasi dan Penyelesaian Konflik
# ==========================================
t11 = doc.tables[11]
set_cell(t11.rows[1].cells[1], "Branch main dan branch feature secara bersamaan mengubah baris yang persis sama pada file README.md dengan nilai teks informasi dosen yang berbeda.")
set_cell(t11.rows[2].cells[1], "Pengembang membuka file README.md, menghapus conflict markers (<<<<<<<, =======, >>>>>>>), menetapkan baris resmi yang disepakati, lalu melakukan git add README.md dan commit penggabungan.")
set_cell(t11.rows[3].cells[1], "Terbentuk satu merge commit baru (489f0bb) yang menyatukan kedua cabang secara mulus tanpa kehilangan riwayat kerja.")

# ==========================================
# Table 12: Bukti Feature Branch, Pull Request, dan Konflik
# ==========================================
t12 = doc.tables[12]
set_image_cell(t12.rows[1].cells[0], "C:/Users/asus/sibimbing-akademik/docs/images/screenshot_github_pr.png", "Gambar 3.1: Bukti repositori GitHub resmi SiBimbing dan Pull Request #1 yang telah berhasil di-merge ke branch main.")

# ==========================================
# Table 13: 4.1 Ringkasan Project Charter
# ==========================================
t13 = doc.tables[13]
set_cell(t13.rows[0].cells[1], "Ketiadaan sistem terpusat untuk penjadwalan bimbingan dosen dan tidak adanya dokumentasi logbook revisi akademik yang transparan.")
set_cell(t13.rows[1].cells[1], "Membangun aplikasi web untuk reservasi slot jadwal bimbingan dosen secara mandiri tanpa bentrok, serta mendokumentasikan logbook evaluasi revisi tugas akhir secara digital.")
set_cell(t13.rows[2].cells[1], "Mahasiswa, Dosen Pembimbing, dan Koordinator Tugas Akhir / Admin Program Studi.")
set_cell(t13.rows[3].cells[1], "Autentikasi multi-user, kelola ketersediaan slot dosen, pencarian dan pengajuan jadwal bimbingan, verifikasi persetujuan dosen, pencatatan logbook revisi bab, dan rekapitulasi progres.")
set_cell(t13.rows[4].cells[1], "Pembayaran biaya bimbingan/SPP, integrasi video conference otomatis, dan tanda tangan digital bersertifikat kriptografi eksternal.")
set_cell(t13.rows[5].cells[1], "Potensi keterlambatan respon dosen (dimitigasi batas konfirmasi otomatis H-1) dan risiko double booking (dimitigasi locking transaction pada basis data).")
set_cell(t13.rows[6].cells[1], "Aplikasi web SiBimbing berbasis PHP, skema basis data MySQL relasional, berkas dokumentasi SDLC lengkap, dan live hosting cloud Vercel.")

# ==========================================
# Table 14: 4.2 Pemilihan Model Pengembangan
# ==========================================
t14 = doc.tables[14]
set_cell(t14.rows[0].cells[1], "Waterfall Model (Sekuensial Linier)", bold=True)
set_cell(t14.rows[1].cells[1], "1. Kebutuhan sistem bimbingan akademik telah jelas, terstandarisasi, dan mengacu pada SOP akademik kampus yang stabil.\n2. Karakter proyek UTS memerlukan dokumentasi terstruktur di setiap fase sehingga mudah diaudit dan dievaluasi dosen.\n3. Memastikan analisis kebutuhan dan perancangan basis data selesai tuntas sebelum tahap pengkodean penuh guna meminimalisir pengerjaan ulang (rework).")

# ==========================================
# Table 15: 4.3 Rencana Tahapan Pengembangan
# ==========================================
t15 = doc.tables[15]
t15_data = [
    ("1", "Analisis Kebutuhan (Requirements Analysis)", "Dokumen spesifikasi FR/NFR, analisis stakeholder, dan matriks prioritas MoSCoW."),
    ("2", "Perancangan Sistem & Basis Data (Design)", "Alur proses bisnis, Context Diagram DFD Level 0, DFD Level 1, Kamus Data, dan file DDL schema.sql."),
    ("3", "Implementasi Pemrograman (Implementation)", "Kode program antarmuka web, modul logika bisnis validasi kuota slot bimbingan PHP."),
    ("4", "Pengujian & Publikasi (Testing & Deployment)", "Uji validasi kuota slot bimbingan dan peluncuran sistem ke server cloud hosting Vercel.")
]
for idx, (no, step, res) in enumerate(t15_data, start=1):
    set_cell(t15.rows[idx].cells[0], no)
    set_cell(t15.rows[idx].cells[1], step, bold=True)
    set_cell(t15.rows[idx].cells[2], res)

# ==========================================
# Table 16: Diagram Alur SDLC
# ==========================================
t16 = doc.tables[16]
set_image_cell(t16.rows[1].cells[0], "C:/Users/asus/sibimbing-akademik/docs/images/diagram_sdlc_waterfall.png", "Gambar 4.1: Diagram Alur Pengembangan Sistem Menggunakan Model Waterfall (Sekuensial Linier) pada Proyek SiBimbing.")

# ==========================================
# Table 17: 5.1 Pihak yang Berkepentingan
# ==========================================
t17 = doc.tables[17]
t17_data = [
    ("1", "Mahasiswa", "Melihat slot ketersediaan dosen, mengajukan janji bimbingan dan topik bahasan, melihat status persetujuan, membaca catatan revisi di logbook."),
    ("2", "Dosen Pembimbing", "Mengatur slot waktu bimbingan dan kuota, menyetujui/menolak ajuan bimbingan, mengisi catatan evaluasi revisi dan kelayakan bab."),
    ("3", "Admin / Koordinator Prodi", "Mengelola master data akun dan penetapan pembimbing, memantau rekapitulasi keaktifan bimbingan untuk syarat sidang.")
]
for idx, (no, role, duty) in enumerate(t17_data, start=1):
    set_cell(t17.rows[idx].cells[0], no)
    set_cell(t17.rows[idx].cells[1], role, bold=True)
    set_cell(t17.rows[idx].cells[2], duty)

# ==========================================
# Table 18: 5.2 Pertanyaan Penggalian Kebutuhan
# ==========================================
t18 = doc.tables[18]
t18_data = [
    ("1", "Bagaimana mahasiswa saat ini mengetahui waktu luang dosen pembimbing?", "Mahasiswa bertanya langsung via chat WhatsApp pribadi, yang sering lambat direspon atau bentrok dengan jadwal mengajar dosen (Temuan)."),
    ("2", "Apa kendala jika dua mahasiswa datang bimbingan pada waktu yang sama?", "Terjadi antrean panjang di ruang dosen dan sesi bimbingan menjadi terburu-buru/kurang mendalam (Temuan)."),
    ("3", "Berapa kuota maksimal mahasiswa yang ideal dalam satu sesi bimbingan?", "Rata-rata 1 sampai 3 mahasiswa per sesi agar dosen fokus menelaah laporan (Asumsi)."),
    ("4", "Informasi apa yang wajib diisi mahasiswa saat mengajukan jadwal bimbingan?", "Nama, NIM, pilihan slot dosen, topik bahasan konsultasi, dan draft bab (Temuan)."),
    ("5", "Bagaimana dosen memberikan konfirmasi kehadiran bimbingan?", "Dosen dapat menyetujui atau menolak (disertai alasan) melalui tombol dashboard sistem (Asumsi)."),
    ("6", "Bagaimana catatan revisi dan arahan bimbingan didokumentasikan?", "Selama ini dicatat pada kartu fisik manual yang rentan hilang atau rusak (Temuan)."),
    ("7", "Siapa saja yang berhak melihat histori catatan logbook bimbingan?", "Mahasiswa bersangkutan, dosen pembimbing terkait, dan koordinator prodi (Temuan)."),
    ("8", "Berapa frekuensi bimbingan minimal agar mahasiswa layak maju sidang?", "Mahasiswa wajib menuntaskan minimal 8 kali bimbingan terverifikasi sebelum sidang (Temuan SOP Akademik).")
]
for idx, (no, q, f) in enumerate(t18_data, start=1):
    set_cell(t18.rows[idx].cells[0], no)
    set_cell(t18.rows[idx].cells[1], q, bold=True)
    set_cell(t18.rows[idx].cells[2], f)

# ==========================================
# Table 19: 5.3 Kebutuhan Fungsional (FR)
# ==========================================
t19 = doc.tables[19]
t19_data = [
    ("FR-01", "Sistem harus mampu memvalidasi kredensial login pengguna sesuai hak akses peran (Mahasiswa, Dosen, Admin).", "Must"),
    ("FR-02", "Sistem harus menyediakan antarmuka bagi dosen untuk membuat, mengubah, dan membatalkan slot waktu bimbingan.", "Must"),
    ("FR-03", "Sistem harus memfasilitasi mahasiswa dalam mencari dan memfilter slot waktu dosen yang masih berstatus tersedia.", "Should"),
    ("FR-04", "Sistem harus memproses reservasi jadwal bimbingan oleh mahasiswa dengan validasi kuota otomatis.", "Must"),
    ("FR-05", "Sistem harus memungkinkan dosen menyetujui (approve) atau menolak (reject) janji bimbingan yang diajukan.", "Must"),
    ("FR-06", "Sistem harus menyediakan modul e-logbook bagi dosen untuk menginput catatan revisi dan status progres bab.", "Must")
]
for idx, (code, req, prio) in enumerate(t19_data, start=1):
    set_cell(t19.rows[idx].cells[0], code, bold=True)
    set_cell(t19.rows[idx].cells[1], req)
    set_cell(t19.rows[idx].cells[2], prio, bold=True)

# ==========================================
# Table 20: 5.4 Kebutuhan Nonfungsional (NFR)
# ==========================================
t20 = doc.tables[20]
t20_data = [
    ("NFR-01", "Keamanan (Security): Kata sandi pengguna wajib di-hash dengan algoritma Bcrypt dan query SQL menggunakan prepared statements untuk mencegah SQL Injection.", "Pengujian penetrasi form dan audit hash basis data."),
    ("NFR-02", "Kinerja (Performance): Waktu muat halaman dan proses submit reservasi slot bimbingan tidak melebihi 2 detik pada koneksi internet normal.", "Pengujian waktu respon jaringan (Network tab browser)."),
    ("NFR-03", "Kompatibilitas Peramban (Compatibility): Tampilan antarmuka sistem web responsif dan bebas bug tampilan pada browser Chrome, Firefox, dan Edge.", "Pengujian lintas peramban (Cross-browser test).")
]
for idx, (code, measure, test) in enumerate(t20_data, start=1):
    set_cell(t20.rows[idx].cells[0], code, bold=True)
    set_cell(t20.rows[idx].cells[1], measure)
    set_cell(t20.rows[idx].cells[2], test)

# ==========================================
# Table 21: 5.5 Kriteria Penerimaan (AC)
# ==========================================
t21 = doc.tables[21]
t21_data = [
    ("AC-01", "Kondisi: Mahasiswa memilih slot bimbingan yang sisa kuotanya > 0 dan menekan tombol kirim.", "Sistem menyimpan permohonan booking dengan status 'DISETUJUI / MENUNGGU', dan sisa kuota slot berkurang secara otomatis."),
    ("AC-02", "Kondisi: Mahasiswa mencoba memesan slot bimbingan yang sisa kuotanya 0 (penuh).", "Sistem menolak transaksi dan menampilkan pesan peringatan 'DITOLAK (SLOT PENUH)' serta meminta mahasiswa memilih slot lain."),
    ("AC-03", "Kondisi: Dosen menginputkan catatan evaluasi bimbingan dan memilih status kelayakan pada logbook.", "Data catatan revisi tersimpan pada tabel logbook dan langsung tampil pada kartu kendali bimbingan mahasiswa.")
]
for idx, (code, cond, exp) in enumerate(t21_data, start=1):
    set_cell(t21.rows[idx].cells[0], code, bold=True)
    set_cell(t21.rows[idx].cells[1], cond)
    set_cell(t21.rows[idx].cells[2], exp)

# ==========================================
# Table 22: 5.6 Batasan dan Prioritas Pelaksanaan
# ==========================================
t22 = doc.tables[22]
set_cell(t22.rows[0].cells[1], "Autentikasi multi-user, manajemen slot ketersediaan dosen, reservasi bimbingan dengan validasi kuota, verifikasi bimbingan dosen, dan modul logbook catatan revisi.")
set_cell(t22.rows[1].cells[1], "Notifikasi otomatis via WhatsApp Gateway/Email, upload berkas draft naskah (.pdf/.docx), dan kalender interaktif visual.")
set_cell(t22.rows[2].cells[1], "Tidak mencakup transaksi pembayaran administrasi/kuliah, tidak menyediakan video call conference bawaan, dan verifikasi dosen disimpan sebagai status sistem (tanpa tanda tangan digital kriptografi pihak ketiga).")

# ==========================================
# Table 23: 6.1 Alur Proses Bisnis
# ==========================================
t23 = doc.tables[23]
t23_data = [
    ("1", "Dosen pembimbing masuk ke sistem dan menginputkan jadwal ketersediaan waktu bimbingan beserta kuota mahasiswa.", "Jadwal slot waktu aktif berstatus 'tersedia' tersimpan di sistem."),
    ("2", "Mahasiswa memilih dosen pembimbing, menyeleksi slot waktu kosong, dan mengisi topik bahasan.", "Sistem memverifikasi kuota: jika tersedia, sistem mencatat booking bimbingan dan mengunci kuota."),
    ("3", "Dosen meninjau permohonan bimbingan yang masuk dan memberikan keputusan konfirmasi.", "Keputusan status bimbingan menjadi 'disetujui' atau 'ditolak' (disertai alasan penolakan)."),
    ("4", "Sesi bimbingan dilaksanakan, lalu dosen menginputkan catatan evaluasi revisi dan progres bab ke modul logbook.", "Rekam logbook tersimpan dan akumulasi keaktifan bimbingan mahasiswa diperbarui untuk syarat pendaftaran sidang.")
]
for idx, (no, act, out) in enumerate(t23_data, start=1):
    set_cell(t23.rows[idx].cells[0], no)
    set_cell(t23.rows[idx].cells[1], act)
    set_cell(t23.rows[idx].cells[2], out)

# ==========================================
# Table 24: 6.2 Daftar Entitas Basis Data
# ==========================================
t24 = doc.tables[24]
t24_data = [
    ("users", "id", "-", "Menyimpan data kredensial akun autentikasi seluruh pengguna (admin, dosen, mahasiswa)."),
    ("dosen", "id", "user_id", "Menyimpan data profil biodata dan kontak dosen pembimbing."),
    ("mahasiswa", "id", "user_id, dosen_pembimbing_id", "Menyimpan data akademik mahasiswa dan dosen pembimbing tugas akhir."),
    ("jadwal_slot", "id", "dosen_id", "Menyimpan daftar slot waktu ketersediaan bimbingan dosen dan sisa kuota."),
    ("bimbingan_booking", "id", "slot_id, mahasiswa_id", "Mencatat transaksi permohonan reservasi bimbingan oleh mahasiswa.")
]
for idx, (tbl, pk, fk, fn) in enumerate(t24_data, start=1):
    set_cell(t24.rows[idx].cells[0], tbl, bold=True)
    set_cell(t24.rows[idx].cells[1], pk)
    set_cell(t24.rows[idx].cells[2], fk)
    set_cell(t24.rows[idx].cells[3], fn)

# ==========================================
# Table 25: Relasi Antarentitas
# ==========================================
t25 = doc.tables[25]
t25_data = [
    ("users - dosen", "1:1", "Setiap satu akun user bertipe dosen terhubung tepat ke satu data biodata dosen."),
    ("users - mahasiswa", "1:1", "Setiap satu akun user bertipe mahasiswa terhubung tepat ke satu data biodata mahasiswa."),
    ("dosen - mahasiswa", "1:N", "Satu dosen pembimbing dapat membimbing banyak mahasiswa tugas akhir."),
    ("dosen - jadwal_slot", "1:N", "Satu dosen dapat membuka banyak slot ketersediaan waktu bimbingan.")
]
for idx, (rel, card, desc) in enumerate(t25_data, start=1):
    set_cell(t25.rows[idx].cells[0], rel, bold=True)
    set_cell(t25.rows[idx].cells[1], card, bold=True)
    set_cell(t25.rows[idx].cells[2], desc)

# ==========================================
# Table 26: 6.3 Kamus Data
# ==========================================
t26 = doc.tables[26]
t26_data = [
    ("users", "id", "INT (PK, Auto Inc)", "Identifikator unik akun pengguna."),
    ("users", "username", "VARCHAR(50)", "NIM / NIDN pengguna, bernilai unik dan tidak boleh kosong."),
    ("jadwal_slot", "id", "INT (PK, Auto Inc)", "Identifikator unik slot ketersediaan bimbingan."),
    ("jadwal_slot", "kuota_mhs", "INT", "Kapasitas maksimal mahasiswa dalam satu sesi bimbingan."),
    ("bimbingan_booking", "kode_booking", "VARCHAR(30)", "Kode referensi unik transaksi reservasi bimbingan."),
    ("bimbingan_booking", "status_booking", "ENUM", "Status reservasi ('menunggu', 'disetujui', 'ditolak', 'selesai')."),
    ("logbook_bimbingan", "catatan_revisi", "TEXT", "Catatan arahan evaluasi dan perbaikan dari dosen pembimbing.")
]
for idx, (tbl, attr, typ, inf) in enumerate(t26_data, start=1):
    set_cell(t26.rows[idx].cells[0], tbl, bold=True)
    set_cell(t26.rows[idx].cells[1], attr)
    set_cell(t26.rows[idx].cells[2], typ)
    set_cell(t26.rows[idx].cells[3], inf)

# ==========================================
# Table 27: 7.1 Berkas Rancangan yang Dilampirkan
# ==========================================
t27 = doc.tables[27]
set_cell(t27.rows[1].cells[1], "https://github.com/sahabatrauul-star/sibimbing-akademik", bold=True, color=RGBColor(37, 99, 235))
set_cell(t27.rows[2].cells[1], "https://sibimbing-akademik.vercel.app", bold=True, color=RGBColor(37, 99, 235))

doc.save(output_docx)
print("Lembar Jawaban UTS RPL successfully generated and saved to:", output_docx)
