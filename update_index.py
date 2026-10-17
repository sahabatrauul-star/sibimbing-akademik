import os

php_code = """<?php
/**
 * SiBimbing - Sistem Penjadwalan dan Monitoring Bimbingan Akademik
 * Proyek Ujian Tengah Semester (UTS) Rekayasa Perangkat Lunak
 * Program Studi D3 Teknik Komputer - Kelas D3TK24A1
 * 
 * Pengembang : Raoul
 * NIM        : 240104004
 */

if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

// Data Info Proyek
$proyek = [
    'nama' => 'SiBimbing (Sistem Penjadwalan & Monitoring Bimbingan Akademik)',
    'mata_kuliah' => 'Rekayasa Perangkat Lunak',
    'prodi_kelas' => 'D3 Teknik Komputer / D3TK24A1',
    'pengembang' => 'Raoul (NIM: 240104004)',
    'versi' => '1.0.0-uts',
    'status' => 'Fase Analisis & Perancangan (UTS)'
];

// Data Dummy Ketersediaan Slot Dosen untuk Simulasi Logika Bisnis
$slotTersedia = [
    'SLOT-01' => ['dosen' => 'Dr. Ir. Handoko, M.T.', 'jam' => '09:00 - 10:00 WIB', 'kuota' => 2, 'hari' => 'Selasa'],
    'SLOT-02' => ['dosen' => 'Dr. Ir. Handoko, M.T.', 'jam' => '10:30 - 11:30 WIB', 'kuota' => 0, 'hari' => 'Selasa'], // kuota 0 untuk simulasi penolakan
    'SLOT-03' => ['dosen' => 'Novemy Triyandari N, SE, MM', 'jam' => '13:30 - 14:30 WIB', 'kuota' => 3, 'hari' => 'Rabu'],
    'SLOT-04' => ['dosen' => 'Novemy Triyandari N, SE, MM', 'jam' => '14:30 - 15:30 WIB', 'kuota' => 1, 'hari' => 'Rabu'],
];

// Penyimpanan Data Pengajuan / Pendaftar (Persistent File + Session Fallback)
$storageFile = sys_get_temp_dir() . '/sibimbing_records_v1.json';

$defaultPendaftar = [
    [
        'kode' => 'BOOK-001',
        'nama' => 'Budi Santoso',
        'nim' => '240104012',
        'dosen' => 'Dr. Ir. Handoko, M.T.',
        'jadwal' => 'Selasa, 09:00 - 10:00 WIB',
        'topik' => 'Revisi Bab 2 Landasan Teori Jaringan Sensor Nirkabel',
        'status' => 'DISETUJUI',
        'waktu' => '17 Okt 2026 08:30 WIB'
    ],
    [
        'kode' => 'BOOK-002',
        'nama' => 'Siti Nurhaliza',
        'nim' => '240104019',
        'dosen' => 'Novemy Triyandari N, SE, MM',
        'jadwal' => 'Rabu, 13:30 - 14:30 WIB',
        'topik' => 'Konsultasi Bab 3 Metodologi Penelitian & Pemodelan SDLC',
        'status' => 'MENUNGGU',
        'waktu' => '17 Okt 2026 09:15 WIB'
    ],
    [
        'kode' => 'BOOK-003',
        'nama' => 'Dimas Prasetyo',
        'nim' => '240104025',
        'dosen' => 'Dr. Ir. Handoko, M.T.',
        'jadwal' => 'Selasa, 10:30 - 11:30 WIB',
        'topik' => 'Pengajuan Proposal Judul Skripsi Smart Agriculture',
        'status' => 'DITOLAK (SLOT PENUH)',
        'waktu' => '17 Okt 2026 09:40 WIB'
    ]
];

// Muat data yang sudah tersimpan
if (file_exists($storageFile)) {
    $pendaftarList = json_decode(file_get_contents($storageFile), true);
    if (!is_array($pendaftarList)) {
        $pendaftarList = $defaultPendaftar;
    }
} elseif (isset($_SESSION['sibimbing_pendaftar']) && is_array($_SESSION['sibimbing_pendaftar'])) {
    $pendaftarList = $_SESSION['sibimbing_pendaftar'];
} else {
    $pendaftarList = $defaultPendaftar;
}

$pesanHasil = null;

// Logika Pemrosesan Form Bimbingan
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $namaMhs = trim($_POST['nama_mhs'] ?? '');
    $nimMhs = trim($_POST['nim_mhs'] ?? '');
    $slotPilihan = $_POST['slot_id'] ?? '';
    $topik = trim($_POST['topik_bimbingan'] ?? '');

    if (empty($namaMhs) || empty($nimMhs) || empty($slotPilihan) || empty($topik)) {
        $pesanHasil = [
            'tipe' => 'danger',
            'status' => 'GAGAL',
            'judul' => 'Validasi Input Gagal',
            'detail' => 'Harap lengkapi semua field formulir bimbingan!'
        ];
    } elseif (!isset($slotTersedia[$slotPilihan])) {
        $pesanHasil = [
            'tipe' => 'danger',
            'status' => 'GAGAL',
            'judul' => 'Slot Tidak Valid',
            'detail' => 'Slot bimbingan yang dipilih tidak ditemukan dalam sistem.'
        ];
    } else {
        $slot = $slotTersedia[$slotPilihan];
        // Aturan Bisnis RPL: Jika kuota <= 0 maka pengajuan ditolak secara otomatis
        if ($slot['kuota'] <= 0) {
            $statusFinal = 'DITOLAK (SLOT PENUH)';
            $pesanHasil = [
                'tipe' => 'warning',
                'status' => $statusFinal,
                'judul' => 'Reservasi Gagal Diproses',
                'detail' => "Maaf {$namaMhs} ({$nimMhs}), slot waktu {$slot['hari']}, {$slot['jam']} untuk Dosen {$slot['dosen']} sudah terisi penuh. Silakan pilih slot waktu lain."
            ];
        } else {
            $statusFinal = 'DISETUJUI';
            $pesanHasil = [
                'tipe' => 'success',
                'status' => 'DISETUJUI (SLOT TERKUNCI)',
                'judul' => 'Jadwal Bimbingan Berhasil Didaftarkan!',
                'detail' => "Bimbingan untuk {$namaMhs} ({$nimMhs}) dengan Dosen {$slot['dosen']} dijadwalkan pada hari {$slot['hari']}, {$slot['jam']}. Topik: '{$topik}'. Catatan revisi telah tercatat pada Logbook Monitoring di bawah."
            ];
        }

        // Tambahkan ke data pendaftar baru
        $newRecord = [
            'kode' => 'BOOK-' . str_pad(count($pendaftarList) + 1, 3, '0', STR_PAD_LEFT),
            'nama' => htmlspecialchars($namaMhs),
            'nim' => htmlspecialchars($nimMhs),
            'dosen' => htmlspecialchars($slot['dosen']),
            'jadwal' => htmlspecialchars($slot['hari']) . ', ' . htmlspecialchars($slot['jam']),
            'topik' => htmlspecialchars($topik),
            'status' => $statusFinal,
            'waktu' => date('d M Y H:i') . ' WIB'
        ];

        // Simpan di posisi teratas
        array_unshift($pendaftarList, $newRecord);
        @file_put_contents($storageFile, json_encode($pendaftarList, JSON_PRETTY_PRINT));
        $_SESSION['sibimbing_pendaftar'] = $pendaftarList;
    }
}
?>
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?= htmlspecialchars($proyek['nama']) ?></title>
    <style>
        :root {
            --bg-dark: #0f172a;
            --card-dark: #1e293b;
            --border-color: #334155;
            --primary: #6366f1;
            --primary-hover: #4f46e5;
            --text-light: #f8fafc;
            --text-muted: #94a3b8;
            --success: #10b981;
            --warning: #f59e0b;
            --danger: #ef4444;
            --info: #38bdf8;
        }
        * { box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
        body {
            background-color: var(--bg-dark);
            color: var(--text-light);
            margin: 0;
            padding: 30px 15px;
            display: flex;
            justify-content: center;
        }
        .container {
            width: 100%;
            max-width: 860px;
        }
        .header-box {
            background: linear-gradient(135deg, #1e1b4b, #312e81);
            border: 1px solid #4338ca;
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: 0 10px 25px -5px rgba(0,0,0,0.4);
        }
        .badge-header {
            display: inline-block;
            background: rgba(99, 102, 241, 0.25);
            border: 1px solid rgba(129, 140, 248, 0.4);
            color: #c7d2fe;
            padding: 4px 10px;
            border-radius: 9999px;
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 10px;
        }
        h1 { margin: 0 0 8px 0; font-size: 24px; color: #ffffff; }
        .meta-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 10px;
            font-size: 13px;
            color: #cbd5e1;
            margin-top: 15px;
            border-top: 1px solid rgba(255,255,255,0.1);
            padding-top: 12px;
        }
        .card {
            background: var(--card-dark);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        .card-title {
            margin-top: 0;
            font-size: 18px;
            color: #e2e8f0;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 12px;
            margin-bottom: 18px;
        }
        .alert {
            padding: 16px;
            border-radius: 12px;
            margin-bottom: 20px;
            font-size: 14px;
        }
        .alert-success { background: rgba(16, 185, 129, 0.15); border: 1px solid var(--success); color: #6ee7b7; }
        .alert-warning { background: rgba(245, 158, 11, 0.15); border: 1px solid var(--warning); color: #fde68a; }
        .alert-danger { background: rgba(239, 68, 68, 0.15); border: 1px solid var(--danger); color: #fca5a5; }
        .alert-title { font-weight: bold; margin-bottom: 4px; font-size: 15px; }

        .form-group { margin-bottom: 16px; }
        label { display: block; font-size: 13px; font-weight: 600; color: #cbd5e1; margin-bottom: 6px; }
        input, select, textarea {
            width: 100%;
            padding: 10px 14px;
            background: #0f172a;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            color: #fff;
            font-size: 14px;
            transition: border-color 0.2s;
        }
        input:focus, select:focus, textarea:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2);
        }
        .row { display: flex; gap: 14px; }
        .col { flex: 1; }
        button.btn-submit {
            background: var(--primary);
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 14px;
            cursor: pointer;
            width: 100%;
            transition: background 0.2s;
        }
        button.btn-submit:hover { background: var(--primary-hover); }

        table { width: 100%; border-collapse: collapse; font-size: 13px; }
        th, td { padding: 10px 12px; text-align: left; border-bottom: 1px solid var(--border-color); }
        th { color: var(--text-muted); font-weight: 600; }
        .badge-slot { padding: 3px 8px; border-radius: 6px; font-size: 11px; font-weight: 600; }
        .badge-slot.ready { background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.4); }
        .badge-slot.full { background: rgba(239, 68, 68, 0.2); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.4); }

        .badge-status { padding: 4px 8px; border-radius: 6px; font-size: 11px; font-weight: 700; display: inline-block; }
        .badge-status.acc { background: rgba(16, 185, 129, 0.2); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.4); }
        .badge-status.wait { background: rgba(56, 189, 248, 0.2); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.4); }
        .badge-status.rej { background: rgba(239, 68, 68, 0.2); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.4); }

        .nav-links { display: flex; gap: 10px; margin-bottom: 20px; }
        .nav-links a {
            background: #1e293b;
            color: #94a3b8;
            padding: 8px 16px;
            border-radius: 8px;
            text-decoration: none;
            font-size: 13px;
            font-weight: 600;
            border: 1px solid #334155;
            transition: all 0.2s;
        }
        .nav-links a.active, .nav-links a:hover {
            background: var(--primary);
            color: #fff;
            border-color: var(--primary);
        }

        footer { text-align: center; font-size: 12px; color: var(--text-muted); margin-top: 30px; }
    </style>
</head>
<body>

<div class="container">
    <!-- Header Informasi Proyek (Tahap 1) -->
    <div class="header-box">
        <span class="badge-header">UTS Rekayasa Perangkat Lunak 2026</span>
        <h1><?= htmlspecialchars($proyek['nama']) ?></h1>
        <div class="meta-grid">
            <div><strong>Mata Kuliah:</strong> <?= htmlspecialchars($proyek['mata_kuliah']) ?></div>
            <div><strong>Prodi/Kelas:</strong> <?= htmlspecialchars($proyek['prodi_kelas']) ?></div>
            <div><strong>Pengembang:</strong> <?= htmlspecialchars($proyek['pengembang']) ?></div>
            <div><strong>Versi/Status:</strong> <?= htmlspecialchars($proyek['versi']) ?> (<?= htmlspecialchars($proyek['status']) ?>)</div>
        </div>
    </div>

    <!-- Quick Navigation -->
    <div class="nav-links">
        <a href="#form-daftar" class="active">📝 Form Pendaftaran</a>
        <a href="#daftar-pendaftar">📋 Daftar Orang Yang Sudah Daftar (<?= count($pendaftarList) ?>)</a>
        <a href="jadwal.php">📅 Modul Jadwal Dosen</a>
    </div>

    <!-- Alert Hasil Simulasi Logika -->
    <?php if ($pesanHasil): ?>
        <div class="alert alert-<?= $pesanHasil['tipe'] ?>">
            <div class="alert-title">[<?= $pesanHasil['status'] ?>] <?= htmlspecialchars($pesanHasil['judul']) ?></div>
            <div><?= htmlspecialchars($pesanHasil['detail']) ?></div>
        </div>
    <?php endif; ?>

    <!-- Tabel Daftar Slot Dosen -->
    <div class="card">
        <h2 class="card-title">
            <span>📅 Jadwal Ketersediaan Slot Dosen Pembimbing</span>
            <span style="font-size: 12px; font-weight: normal; color: var(--text-muted);">Real-time Slot Control</span>
        </h2>
        <table>
            <thead>
                <tr>
                    <th>Kode</th>
                    <th>Dosen Pembimbing</th>
                    <th>Hari & Jam</th>
                    <th>Sisa Kuota</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($slotTersedia as $id => $slot): ?>
                    <tr>
                        <td><code><?= $id ?></code></td>
                        <td><?= htmlspecialchars($slot['dosen']) ?></td>
                        <td><?= htmlspecialchars($slot['hari']) ?>, <?= htmlspecialchars($slot['jam']) ?></td>
                        <td><?= $slot['kuota'] ?> Mahasiswa</td>
                        <td>
                            <?php if ($slot['kuota'] > 0): ?>
                                <span class="badge-slot ready">Tersedia</span>
                            <?php else: ?>
                                <span class="badge-slot full">Penuh</span>
                            <?php endif; ?>
                        </td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </div>

    <!-- Formulir Simulasi Pengajuan Bimbingan (Logika Tahap 1) -->
    <div class="card" id="form-daftar">
        <h2 class="card-title">📝 Form Pengajuan Janji Bimbingan Akademik</h2>
        <form method="POST" action="">
            <div class="row">
                <div class="col form-group">
                    <label>Nama Mahasiswa</label>
                    <input type="text" name="nama_mhs" required placeholder="Contoh: Raoul" value="Raoul">
                </div>
                <div class="col form-group">
                    <label>NIM Mahasiswa</label>
                    <input type="text" name="nim_mhs" required placeholder="Contoh: 240104004" value="240104004">
                </div>
            </div>

            <div class="form-group">
                <label>Pilih Slot Waktu Dosen Pembimbing</label>
                <select name="slot_id" required>
                    <option value="">-- Pilih Slot Bimbingan --</option>
                    <?php foreach ($slotTersedia as $id => $slot): ?>
                        <option value="<?= $id ?>">
                            [<?= $id ?>] <?= htmlspecialchars($slot['dosen']) ?> - <?= htmlspecialchars($slot['hari']) ?>, <?= htmlspecialchars($slot['jam']) ?> (Kuota: <?= $slot['kuota'] ?>)
                        </option>
                    <?php endforeach; ?>
                </select>
                <small style="color: var(--text-muted); font-size: 11px;">*Tips: Pilih SLOT-01 untuk uji status Diterima, atau SLOT-02 untuk uji penolakan kuota penuh (0).</small>
            </div>

            <div class="form-group">
                <label>Topik / Bahasan Bimbingan</label>
                <textarea name="topik_bimbingan" rows="3" required placeholder="Contoh: Diskusi Bab 3 Perancangan Basis Data dan Diagram Konteks SiBimbing"></textarea>
            </div>

            <button type="submit" class="btn-submit">Kirim Pengajuan Bimbingan</button>
        </form>
    </div>

    <!-- TABEL PENDAFTAR / MONITORING BIMBINGAN (LOGBOOK MAHASISWA) -->
    <div class="card" id="daftar-pendaftar">
        <h2 class="card-title">
            <span>📋 Daftar Riwayat Pengajuan & Monitoring Bimbingan Masuk</span>
            <span style="font-size: 12px; font-weight: normal; color: #38bdf8;">Total: <?= count($pendaftarList) ?> Mahasiswa</span>
        </h2>
        <p style="font-size: 12px; color: var(--text-muted); margin-top: -8px; margin-bottom: 16px;">
            Setiap mahasiswa yang mengisi formulir bimbingan di atas akan langsung tercatat dan dimonitoring di tabel ini secara otomatis.
        </p>

        <div style="overflow-x: auto;">
            <table>
                <thead>
                    <tr>
                        <th>No</th>
                        <th>Mahasiswa</th>
                        <th>Dosen Pembimbing</th>
                        <th>Jadwal Slot</th>
                        <th>Topik Konsultasi</th>
                        <th>Waktu Daftar</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    <?php foreach ($pendaftarList as $index => $row): ?>
                        <tr>
                            <td><?= $index + 1 ?></td>
                            <td>
                                <strong><?= $row['nama'] ?></strong><br>
                                <code style="color: #94a3b8;"><?= $row['nim'] ?></code>
                            </td>
                            <td><?= $row['dosen'] ?></td>
                            <td style="white-space: nowrap;"><?= $row['jadwal'] ?></td>
                            <td><span style="color: #cbd5e1;"><?= $row['topik'] ?></span></td>
                            <td style="font-size: 11px; color: #94a3b8; white-space: nowrap;"><?= $row['waktu'] ?></td>
                            <td>
                                <?php if (strpos($row['status'], 'DISETUJUI') !== false): ?>
                                    <span class="badge-status acc">DISETUJUI</span>
                                <?php elseif (strpos($row['status'], 'MENUNGGU') !== false): ?>
                                    <span class="badge-status wait">MENUNGGU</span>
                                <?php else: ?>
                                    <span class="badge-status rej">DITOLAK</span>
                                <?php endif; ?>
                            </td>
                        </tr>
                    <?php endforeach; ?>
                </tbody>
            </table>
        </div>
    </div>

    <footer>
        &copy; 2026 SiBimbing Project &bull; D3 Teknik Komputer Universitas Duta Bangsa Surakarta
    </footer>
</div>

</body>
</html>
"""

with open('C:/Users/asus/sibimbing-akademik/index.php', 'w', encoding='utf-8') as f:
    f.write(php_code)

with open('C:/Users/asus/sibimbing-akademik/api/index.php', 'w', encoding='utf-8') as f:
    f.write(php_code)

print("Updated index.php and api/index.php successfully")
