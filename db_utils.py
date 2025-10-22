#!/usr/bin/python
import psycopg2
import os
from getpass import getpass

_pg_pass = None

def _get_pg_pass():
    """Prompt for password only once per process, or read from environment."""
    global _pg_pass
    if _pg_pass is None:
        _pg_pass = os.environ.get("PG_PASSWORD")
        if _pg_pass is None:
            _pg_pass = getpass("Postgres password: ")
    return _pg_pass

# Prompt once for the current process
pg_pass = _get_pg_pass()

# Export to environment for any subprocess launched from this process
os.environ["PG_PASSWORD"] = pg_pass

def db_restart():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password=pg_pass
    )
    cur = conn.cursor()
    conn.autocommit = True
    cur.execute("""
        SELECT pg_terminate_backend(pid)
        FROM pg_stat_activity
        WHERE datname = 'postgres' AND pid <> pg_backend_pid();
    """)
    cur.execute("DROP DATABASE IF EXISTS parkir;")
    cur.execute("CREATE DATABASE parkir;")
    cur.close()
    conn.close()

def db_con():
    conn = psycopg2.connect(
        host="localhost",
        database="parkir",
        user="postgres",
        password=pg_pass
    )
    cur = conn.cursor()
    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()
