#!/usr/bin/python

import psycopg2
import rstr
import random
from db_utils import db_con, db_close

random.seed(1000)

conn, cur = db_con()

menjabat = [
        (0, 9),
        (1, 8),
        (2, 7),
        (3, 6),
        (4, 5),
        (5, 4),
        (6, 3),
        (7, 2),
        (8, 1),
        (9, 0)
        ]

for i, j in menjabat:
    cur.execute("INSERT INTO menjabat(id_petugas, id_jabatan) VALUES (%s, %s) ON CONFLICT DO NOTHING", (i, j,))

db_close(conn, cur)
