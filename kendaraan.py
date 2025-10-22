#!/usr/bin/python

import psycopg2
import rstr
import random
from db_utils import db_con, db_close

random.seed(1000)

conn, cur = db_con()

plat_lst = ["A", "B", "D", "E", "F", "G", "H", "K", "L", "M", "N", "S", "T", "AA", "AB", "AD"]

jenis = ["roda 2", "roda 4"]

for i in range(10000):
    plat_awal = "".join(random.choices(plat_lst))
    dummy_data = rstr.xeger(r'[1-9]{4} [A-Z]{1,2}')
    plat_nomor = str(plat_awal + " " + dummy_data )
    jenis_kendaraan  = "".join(random.choices(jenis))
    cur.execute("INSERT INTO kendaraan(plat_nomor, jenis_kendaraan) VALUES (%s, %s) ON CONFLICT DO NOTHING", (plat_nomor, jenis_kendaraan,))


db_close(conn, cur)
