#!/usr/bin/python

import psycopg2
import rstr
import random
from db_utils import db_con, db_close

random.seed(1000)

conn, cur = db_con()

hak_akses = "Lorem ipsum dolor sit amet"

for i in range(10):
    nama_jabatan = str("jabatan" + rstr.xeger(r'[0-1][0-9]'))
    gaji_pokok = rstr.xeger(r'[3-5][0-9]00000')
    cur.execute("INSERT INTO jabatan(id_jabatan, nama_jabatan, hak_akses, gaji_Pokok) VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING", (i, nama_jabatan, hak_akses, gaji_pokok,))

db_close(conn, cur)
