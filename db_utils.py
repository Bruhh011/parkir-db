#!/usr/bin/python

import psycopg2
import getpass

def db_restart():
    pg_pass = getpass("Postgres password: ")
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password=pg_pass
        )
    cur = conn.cursor()
    conn.autocommit = True
    cur.execute("DROP DATABASE IF EXISTS parkir;")
    cur.execute("CREATE DATABASE parkir;")
    cur.close()
    conn.close()

def db_con():
    conn = psycopg2.connect(
        host="localhost",
        database="parkir",
        user="postgres"
        )
    cur = conn.cursor()
    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()


