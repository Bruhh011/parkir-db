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

rand_num_lst = random.sample(range(0, 11), 10)
mid = len(rand_num_lst) // 2
pintu_masuk_lst = rand_num_lst[:mid]
pintu_keluar_lst = rand_num_lst[mid:]

for x in range(5):
    pintu_masuk = pintu_masuk_lst[x]
    no_tempat_masuk = random.randint(1,100)
    cur.execute("INSERT INTO pintu(no_pintu, jenis_pintu, no_tempat) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING", (pintu_masuk, "masuk", no_tempat_masuk,))


for y in range(5):
    pintu_keluar = pintu_keluar_lst[y]
    no_tempat_keluar = random.randint(1,100)
    cur.execute("INSERT INTO pintu(no_pintu, jenis_pintu, no_tempat) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING", (pintu_keluar, "keluar", no_tempat_keluar,))



conn.commit()

cur.close()
conn.close()

