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

hak_akses = "Lorem ipsum dolor sit amet"

for i in range(10):
    nama_jabatan = str("jabatan" + rstr.xeger(r'[0-1][0-9]'))
    gaji_pokok = rstr.xeger(r'[3-5][0-9]00000')
    cur.execute("INSERT INTO jabatan(id_jabatan, nama_jabatan, hak_akses, gaji_Pokok) VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING", (i, nama_jabatan, hak_akses, gaji_pokok,))


conn.commit()

cur.close()
conn.close()
