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

ketersediaan_lst = ["kosong", "ditempati"]

for i in range(100):
    lantai = random.randint(1,3)
    ketersediaan = "".join(random.choices(ketersediaan_lst))
    cur.execute("INSERT INTO lokasi(lantai, no_tempat, ketersediaan) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING", (lantai, i, ketersediaan,))

conn.commit()
cur.close()
conn.close()

