#!/usr/bin/python

import psycopg2
import rstr
import random
from db_utils import db_con, db_close

random.seed(1000)

conn, cur = db_con()

jabatan = [
        (0, "direktur utama", "akses penuh ke seluruh sistem", 15000000),
        (1, "manajer operasional", "akses ke laporan dan data operasional", 10000000),
        (2, "supervisor lapangan", "akses data parkir harian", 5500000),
        (3, "admin sistem", "akses konfigurasi sistem dan pengguna", 6000000),
        (4, "petugas parkir1", "akses input dan pembayaran kendaraan keluar", 3500000),
        (5, "petugas parkir2", "akses input dan pembayaran keluar", 3500000),
        (6, "keamanan", "akses laporan keamanan area parkir", 4000000),
        (7, "teknisi sistem", "akses pemeliharaan dan sistem", 5500000),
        (8, "customer service", "akses data pelanggan dan komplain", 5000000),
        (9, "kepala shift", "akses data shift dan laporan harian", 6500000)
        ]

for i, j, k, l in jabatan:
    cur.execute("INSERT INTO jabatan(id_jabatan, nama_jabatan, hak_akses, gaji_Pokok) VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING", (i, j, k, l,))

db_close(conn, cur)
