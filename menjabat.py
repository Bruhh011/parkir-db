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

for i in range(10):
    cur.execute("SELECT id_petugas FROM petugas ORDER BY RANDOM() LIMIT 1;")
    rand_petugas = cur.fetchone()[0]
    cur.execute("SELECT id_jabatan FROM jabatan ORDER BY RANDOM() LIMIT 1;")
    rand_jabatan = cur.fetchone()[0]
    cur.execute("INSERT INTO menjabat(id_petugas, id_jabatan) VALUES (%s, %s) ON CONFLICT DO NOTHING", (rand_petugas, rand_jabatan,))


conn.commit()

cur.close()
conn.close()
