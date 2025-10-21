#!/usr/bin/python

import psycopg2
import random

conn = psycopg2.connect(
        host="localhost",
        database="parkir",
        user="postgres"
        )
cur = conn.cursor()

first_name_lst = ["Jayvon", "Landon", "Glenn", "Bradyn", "Brian", "Janiah", "Anderson", "Araceli", "Rhett", "Donald"]
last_name_lst = ["George", "Christensen", "Bridges", "Tapia", "Stokes", "Carey", "Aguirre", "Reid", "Rivera", "Guerra", "Guerra", "Andersen"]

for i in range(10):
    rand_name = "".join(random.choices(first_name_lst)) + " " + "".join(random.choices(last_name_lst))
    cur.execute("INSERT INTO petugas(id_petugas, nama_petugas) VALUES (%s, %s) ON CONFLICT DO NOTHING", (i, rand_name,))


conn.commit()

cur.close()
conn.close()

