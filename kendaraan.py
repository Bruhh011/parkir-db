#!/usr/bin/python

import psycopg2
import rstr
import random
from db_utils import db_con, db_close

random.seed(1000)

conn, cur = db_con()

plat_lst = ["A", "B", "D", "E", "F", "G", "H", "K", "L", "M", "N", "S", "T", "AA", "AB", "AD"]
jenis = ["roda 2", "roda 4"]

target_count = 10000
inserted = 0
seen = set()  

while inserted < target_count:
    
    plat_awal = random.choice(plat_lst)
    dummy_data = rstr.xeger(r'[1-9]{4} [A-Z]{1,2}')
    plat_nomor = f"{plat_awal} {dummy_data}"
    jenis_kendaraan = random.choice(jenis)

    
    if plat_nomor in seen:
        continue

    try:
        cur.execute(
            "INSERT INTO kendaraan(plat_nomor, jenis_kendaraan) VALUES (%s, %s) ON CONFLICT DO NOTHING",
            (plat_nomor, jenis_kendaraan)
        )
        if cur.rowcount > 0:  
            seen.add(plat_nomor)
            inserted += 1
    except Exception as e:
        conn.rollback()


db_close(conn, cur)

