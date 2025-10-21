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

keterangan_template = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

for i in range(100):
    cur.execute("SELECT no_struk FROM jadwal ORDER BY RANDOM() LIMIT 1;")
    rand_struk = cur.fetchone()[0]
    cur.execute("INSERT INTO insiden(id_rekaman, keterangan, no_struk) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING", (i, keterangan_template, rand_struk,))


conn.commit()

cur.close()
conn.close()


