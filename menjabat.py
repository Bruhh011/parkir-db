#!/usr/bin/python

import psycopg2
import rstr
import random
from db_utils import db_con, db_close

random.seed(1000)

conn, cur = db_con()

for i in range(10):
    cur.execute("SELECT id_petugas FROM petugas ORDER BY RANDOM() LIMIT 1;")
    rand_petugas = cur.fetchone()[0]
    cur.execute("SELECT id_jabatan FROM jabatan ORDER BY RANDOM() LIMIT 1;")
    rand_jabatan = cur.fetchone()[0]
    cur.execute("INSERT INTO menjabat(id_petugas, id_jabatan) VALUES (%s, %s) ON CONFLICT DO NOTHING", (rand_petugas, rand_jabatan,))

db_close(conn, cur)
