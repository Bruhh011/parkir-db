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

rand_num = [random.randint(1,10) for _ in range(10)]

rand_num_lst = rand_num
mid = len(rand_num) // 2
pintu_masuk_lst = rand_num_lst[:mid]
pintu_keluar_lst = rand_num_lst[mid:]

for x in range(5):
    pintu_masuk = pintu_masuk_lst[x]
    no_tempat_masuk = random.randint(1,100)
    cur.execute("INSERT INTO pintu(no_pintu, jenis_pintu, no_tempat) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING", (pintu_masuk, "masuk", no_tempat_masuk,))


for y in range(5):
    pintu_keluar = pintu_keluar_lst[y]
    no_tempat_keluar = random.randint(1,100)
    cur.execute("INSERT INTO pintu(no_pintu, jenis_pintu, no_tempat) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING", (pintu_masuk, "keluar", no_tempat_keluar,))



conn.commit()

cur.close()
conn.close()

