#!/usr/bin/python

import psycopg2
import rstr
import random
from db_utils import db_con, db_close

random.seed(1000)

conn, cur = db_con()

keterangan_template_lst = ["Kehilangan komponen kendaraan", "kehilangan kendaraan", "kehilangan barang"]

for i in range(100):
    cur.execute("SELECT no_struk FROM jadwal ORDER BY RANDOM() LIMIT 1;")
    rand_struk = cur.fetchone()[0]
    keterangan_template = "".join(random.choices(keterangan_template_lst))
    cur.execute("INSERT INTO insiden(id_rekaman, keterangan, no_struk) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING", (i, keterangan_template, rand_struk,))

db_close(conn, cur)

