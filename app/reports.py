import pandas as pd
import sqlite3

def daily_report():
    con = sqlite3.connect("data/club.db")
    df = pd.read_sql("SELECT * FROM daily_activity", con)
    path = "reports/daily_activity.xlsx"
    df.to_excel(path, index=False)
    return path
