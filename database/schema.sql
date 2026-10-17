-- ==========================================================
-- SISTEM PENJADWALAN DAN MONITORING BIMBINGAN AKADEMIK (SiBimbing)
-- File: database/schema.sql
-- Mata Kuliah: Rekayasa Perangkat Lunak (D3 Teknik Komputer 24A1)
-- Pengembang : Raoul (NIM: 240104004)
-- ==========================================================

CREATE DATABASE IF NOT EXISTS sibimbing_db;
USE sibimbing_db;

-- 1. TABEL PENGGUNA (USERS)
-- Menyimpan kredensial autentikasi seluruh entitas pengguna
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,      -- NIM untuk mahasiswa, NIDN untuk dosen, Username untuk admin
    password VARCHAR(255) NOT NULL,             -- Hash Bcrypt
    role ENUM('admin', 'dosen', 'mahasiswa') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_user_role (role)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2. TABEL DOSEN
-- Menyimpan data profil spesifik dosen pembimbing
CREATE TABLE IF NOT EXISTS dosen (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    nidn VARCHAR(20) UNIQUE NOT NULL,
    nama_lengkap VARCHAR(100) NOT NULL,
    gelar VARCHAR(30) NOT NULL,
    email VARCHAR(100) NOT NULL,
    no_hp VARCHAR(20) NOT NULL,
    kuota_maksimal_mhs INT DEFAULT 10,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 3. TABEL MAHASISWA
-- Menyimpan profil mahasiswa beserta relasi dosen pembimbing
CREATE TABLE IF NOT EXISTS mahasiswa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    nim VARCHAR(20) UNIQUE NOT NULL,
    nama_lengkap VARCHAR(100) NOT NULL,
    program_studi VARCHAR(50) DEFAULT 'D3 Teknik Komputer',
    angkatan VARCHAR(10) DEFAULT '2024',
    dosen_pembimbing_id INT NULL,
    judul_tugas_akhir TEXT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (dosen_pembimbing_id) REFERENCES dosen(id) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 4. TABEL SLOT JADWAL DOSEN (JADWAL_SLOT)
-- Ketersediaan waktu bimbingan yang dibuka oleh dosen
CREATE TABLE IF NOT EXISTS jadwal_slot (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dosen_id INT NOT NULL,
    tanggal DATE NOT NULL,
    jam_mulai TIME NOT NULL,
    jam_selesai TIME NOT NULL,
    kuota_mhs INT DEFAULT 1,
    sisa_kuota INT DEFAULT 1,
    ruangan_lokasi VARCHAR(100) DEFAULT 'Ruang Dosen Lab Komputer',
    status_slot ENUM('tersedia', 'penuh', 'dibatalkan') DEFAULT 'tersedia',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (dosen_id) REFERENCES dosen(id) ON DELETE CASCADE,
    INDEX idx_slot_dosen_tgl (dosen_id, tanggal)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 5. TABEL PEMESANAN / BOOKING BIMBINGAN (BIMBINGAN_BOOKING)
-- Transaksi reservasi janji temu bimbingan oleh mahasiswa
CREATE TABLE IF NOT EXISTS bimbingan_booking (
    id INT AUTO_INCREMENT PRIMARY KEY,
    kode_booking VARCHAR(30) UNIQUE NOT NULL,  -- Contoh: BOOK-202610-001
    slot_id INT NOT NULL,
    mahasiswa_id INT NOT NULL,
    topik_bahasan TEXT NOT NULL,
    file_draft_url VARCHAR(255) NULL,
    status_booking ENUM('menunggu', 'disetujui', 'ditolak', 'selesai') DEFAULT 'menunggu',
    alasan_penolakan TEXT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (slot_id) REFERENCES jadwal_slot(id) ON DELETE CASCADE,
    FOREIGN KEY (mahasiswa_id) REFERENCES mahasiswa(id) ON DELETE CASCADE,
    INDEX idx_booking_status (status_booking)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 6. TABEL LOGBOOK & REKAM MONITORING (LOGBOOK_BIMBINGAN)
-- Mencatat feedback dosen dan riwayat progres revisi akademik
CREATE TABLE IF NOT EXISTS logbook_bimbingan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT UNIQUE NOT NULL,
    catatan_revisi TEXT NOT NULL,
    progres_bab VARCHAR(50) NOT NULL,          -- Contoh: Bab 1 Pendahuluan, Bab 3 Desain Sistem
    status_kelayakan ENUM('revisi', 'lanjut_bab_berikutnya', 'acc_sidang') NOT NULL,
    tanggal_bimbingan DATETIME NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES bimbingan_booking(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==========================================================
-- DATA DUMMY AWAL (SEEDER) UNTUK PENGUJIAN
-- ==========================================================

-- Insert Users (Password default dummy: password123)
INSERT INTO users (id, username, password, role) VALUES
(1, 'admin', '$2y$10$Q7uD3Wq1234567890abcdef...', 'admin'),
(2, '0612088001', '$2y$10$Q7uD3Wq1234567890abcdef...', 'dosen'),
(3, '240104004', '$2y$10$Q7uD3Wq1234567890abcdef...', 'mahasiswa');

-- Insert Dosen
INSERT INTO dosen (id, user_id, nidn, nama_lengkap, gelar, email, no_hp, kuota_maksimal_mhs) VALUES
(1, 2, '0612088001', 'Dr. Ir. Handoko', 'M.T.', 'handoko@udb.ac.id', '081234567890', 10);

-- Insert Mahasiswa
INSERT INTO mahasiswa (id, user_id, nim, nama_lengkap, program_studi, angkatan, dosen_pembimbing_id, judul_tugas_akhir) VALUES
(1, 3, '240104004', 'Raoul', 'D3 Teknik Komputer', '2024', 1, 'Rancang Bangun Sistem Penjadwalan dan Monitoring Bimbingan Akademik');

-- Insert Slot Jadwal Dosen
INSERT INTO jadwal_slot (id, dosen_id, tanggal, jam_mulai, jam_selesai, kuota_mhs, sisa_kuota, ruangan_lokasi, status_slot) VALUES
(1, 1, '2026-10-20', '09:00:00', '10:00:00', 2, 2, 'Ruang Dosen TI Lab 4', 'tersedia'),
(2, 1, '2026-10-20', '10:30:00', '11:30:00', 1, 0, 'Ruang Dosen TI Lab 4', 'penuh');
