#!/usr/bin/python

import psycopg2
import rstr
import random

conn = psycopg2.connect(
        host="localhost",
        database="parkir",
        user="postgres"
        )
cur = conn.cursor()

plat_lst = ["A", "B", "D", "E", "F", "G", "H", "K", "L", "M", "N", "S", "T", "AA", "AB", "AD"]

plat_awal = "".join(random.choices(plat_lst))
dummy_data = rstr.xeger(r'[A-Z1-9]{4,5} [A-Z]{1,2}')
plat_nomor = plat_awal + " " + dummy_data 
jenis = ["roda 2", "roda 4"]

for i in range(10000):
    plat_awal = "".join(random.choices(plat_lst))
    dummy_data = rstr.xeger(r'[A-Z1-9]{4,5} [A-Z]{1,2}')
    plat_nomor = str(plat_awal + " " + dummy_data )
    jenis_kendaraan  = "".join(random.choices(jenis))
    cur.execute("INSERT INTO kendaraan(plat_nomor, jenis_kendaraan) VALUES (%s, %s) ON CONFLICT DO NOTHING", (plat_nomor, jenis_kendaraan,))

conn.commit()

cur.close()
conn.close()
