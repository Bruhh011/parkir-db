#!/usr/bin/python

import psycopg2
import subprocess

conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres"
        )
cur = conn.cursor()
conn.autocommit = True
cur.execute("DROP DATABASE IF EXISTS parkir;")
cur.execute("CREATE DATABASE parkir;")

conn.commit()
cur.close()
conn.close()

conn = psycopg2.connect(
        host="localhost",
        database="parkir",
        user="postgres"
        )
cur = conn.cursor()

load_db = ["psql", "-q", "-U", "postgres", "-d", "parkir", "-f", "./parkir.sql"]
load_petugas = ["python", "./petugas.py"]
load_jabatan = ["python", "./jabatan.py"]
load_lokasi = ["python", "./lokasi.py"]
load_kendaraan = ["python", "./kendaraan.py"]
load_pintu = ["python", "./pintu.py"]
load_absensi = ["python", "./absensi.py"]
load_menjabat = ["python", "./menjabat.py"]
load_jadwal = ["python", "./jadwal.py"]
load_insiden = ["python", "./insiden.py"]

results = [load_db, load_petugas, load_jabatan, load_lokasi, load_kendaraan, load_pintu, load_absensi, load_menjabat, load_jadwal, load_insiden]

for i in results:
    result = subprocess.run(i)
    if result.returncode == 0:
        print(f"{i} Success")
    else:
        print(f"{i} Failed")


conn.commit()
cur.close()
conn.close()






