#!/usr/bin/python

import psycopg2
import rstr
import random
from db_utils import db_con, db_close

random.seed(1000)

conn, cur = db_con()

ketersediaan_lst = ["kosong", "ditempati"]

for i in range(100):
    lantai = random.randint(1,3)
    ketersediaan = "".join(random.choices(ketersediaan_lst))
    cur.execute("INSERT INTO lokasi(lantai, no_tempat, ketersediaan) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING", (lantai, i + 1, ketersediaan,))


db_close(conn, cur)
