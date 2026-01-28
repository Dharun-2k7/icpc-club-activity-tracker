import sqlite3

DB = "data/club.db"

def connect():
    return sqlite3.connect(DB)

def init_db():
    con = connect()
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS daily_activity (
            email TEXT,
            date TEXT,
            cf_solved INTEGER,
            atcoder_solved INTEGER,
            status TEXT
        )
    """)
    con.commit()
    con.close()

def save_daily(email, date, cf, atc, status):
    con = connect()
    cur = con.cursor()
    cur.execute(
        "INSERT INTO daily_activity VALUES (?, ?, ?, ?, ?)",
        (email, date, cf, atc, status)
    )
    con.commit()
    con.close()
