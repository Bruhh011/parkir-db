#!/usr/bin/python

from datetime import datetime, timedelta
import psycopg2
import random

def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

start_date = datetime(2021,1,1)
end_date = datetime(2025, 10, 30)

conn = psycopg2.connect(
        host="localhost",
        database="parkir",
        user="postgres"
        )
cur = conn.cursor()
kehadiran_lst = ["hadir", "izin", "sakit"]

for i in range(1000):
    id_petugas = str(random.randint(0,9))
    rand_date = random_date(start_date, end_date).date()
    rand_kehadiran = "".join(random.choices(kehadiran_lst))
    cur.execute("INSERT INTO absensi(id_petugas, tanggal_absen, kehadiran) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING", (id_petugas, rand_date, rand_kehadiran,))


conn.commit()

cur.close()
conn.close()
