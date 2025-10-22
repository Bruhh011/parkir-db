#!/usr/bin/python

import sys
import subprocess
import importlib

packages = ["rstr", "psycopg2", "datetime"]  
for package_name in packages:
    try:
        importlib.import_module(package_name)
    except ModuleNotFoundError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

import psycopg2
import os
from db_utils import db_restart, db_con, db_close

os_name = os.name.lower()

if os_name in ["nt", "darwin"]:
    postgre_path = input("Enter postgresql path (absolute): ").strip()
    python_path = input("Enter python path (absolute): ").strip()
    os.environ["PATH"] += os.pathsep + postgre_path + os.pathsep + python_path
    with open(os.devnull, "w") as devnull:
        psql_exe = os.path.join(postgre_path, "psql.exe")
        test_postgre = subprocess.run([psql_exe, "--help"], stdout=devnull, stderr=devnull)
        python_exe = os.path.join(python_path, "python.exe")
        test_python = subprocess.run([python_exe, "--help"], stdout=devnull, stderr=devnull)
    if test_postgre.returncode != 0 or test_python.returncode != 0:
        print("psql/python cannot be used")

db_restart()
conn, cur = db_con()

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

results = [
        ("load_db", load_db), 
        ("load_petugas", load_petugas), 
        ("load_jabatan", load_jabatan), 
        ("load_lokasi", load_lokasi), 
        ("load_kendaraan", load_kendaraan),
        ("load_pintu", load_pintu), 
        ("load_absensi", load_absensi), 
        ("load_menjabat", load_menjabat), 
        ("load_jadwal", load_jadwal), 
        ("load_insiden", load_insiden)
        ]

for process, i in results:
    result = subprocess.run(i)
    if result.returncode == 0:
        print(f"\033[92m{process} Success\033[0m")
    else:
        print(f"\033[91m{process} Failed\033[0m")


db_close(conn, cur)



