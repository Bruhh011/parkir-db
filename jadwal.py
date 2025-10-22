#!/usr/bin/python

import psycopg2
import rstr
import random
from datetime import datetime, timedelta
from db_utils import db_con, db_close

random.seed(1000)

conn, cur = db_con()

def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

start_date = datetime(2021,1,1)
end_date = datetime(2025, 10, 30)

for i in range(100):
    cur.execute("SELECT no_pintu FROM pintu ORDER BY RANDOM() LIMIT 1;")
    rand_no_pintu = cur.fetchone()[0]
    cur.execute("SELECT no_tempat FROM lokasi ORDER BY RANDOM() LIMIT 1;")
    rand_no_tempat = cur.fetchone()[0]
    cur.execute("SELECT id_petugas FROM petugas ORDER BY RANDOM() LIMIT 1;")
    rand_petugas = cur.fetchone()[0]
    cur.execute("SELECT plat_nomor FROM kendaraan ORDER BY RANDOM() LIMIT 1;")
    rand_plat = cur.fetchone()[0]
    cur.execute("SELECT jenis_kendaraan FROM kendaraan WHERE plat_nomor = %s;", (rand_plat,))
    rand_jenis_kend = cur.fetchone()[0]
    if rand_jenis_kend == "roda 2":
        rand_bayar = "3000"
    elif rand_jenis_kend == "roda 4":
        rand_bayar = "5000"
    rand_date = random_date(start_date, end_date).date()
    rand_jam_masuk = rstr.xeger(r'[7-9]:[0-5][0-9]')
    rand_jam_keluar = rstr.xeger(r'[1][0-2]:[0-5][0-9]')
    cur.execute("INSERT INTO jadwal(no_struk, tanggal, jam_masuk,jam_keluar, id_petugas, plat_nomor, bayar, no_pintu, no_tempat) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING", (i, rand_date,  rand_jam_masuk, rand_jam_keluar, rand_petugas, rand_plat, rand_bayar, rand_no_pintu, rand_no_tempat,))


db_close(conn, cur)
