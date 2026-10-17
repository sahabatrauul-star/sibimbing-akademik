<?php
/**
 * Modul Jadwal Bimbingan - Feature Branch
 * SiBimbing - Sistem Penjadwalan & Monitoring Bimbingan Akademik
 */
$dosenList = [
    ['nama' => 'Dr. Ir. Handoko, M.T.', 'bidang' => 'Jaringan Komputer & IoT', 'hari' => 'Selasa & Kamis'],
    ['nama' => 'Novemy Triyandari N, SE, MM', 'bidang' => 'Manajemen Proyek & Etika Profesi', 'hari' => 'Rabu & Jumat'],
];
?>
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Jadwal Bimbingan Dosen - SiBimbing</title>
    <style>
        body { font-family: sans-serif; background: #0f172a; color: #f8fafc; padding: 30px; }
        .card { background: #1e293b; padding: 20px; border-radius: 12px; max-width: 600px; margin: auto; border: 1px solid #334155; }
        h2 { color: #818cf8; margin-top: 0; }
        ul { padding-left: 20px; }
        li { margin-bottom: 10px; }
        a { color: #38bdf8; text-decoration: none; }
    </style>
</head>
<body>
    <div class="card">
        <h2>Daftar Ketersediaan Dosen Pembimbing</h2>
        <ul>
            <?php foreach ($dosenList as $d): ?>
                <li>
                    <strong><?= htmlspecialchars($d['nama']) ?></strong><br>
                    <small>WhatsApp: 081234567890 | Keahlian: <?= htmlspecialchars($d['bidang']) ?> | Jadwal: <?= htmlspecialchars($d['hari']) ?></small>
                </li>
            <?php endforeach; ?>
        </ul>
        <p><a href="index.php">&larr; Kembali ke Form Pendaftaran</a></p>
    </div>
</body>
</html>
