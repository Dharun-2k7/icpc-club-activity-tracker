import logging
from datetime import date
from app.members import load_members
from app.cf_api import solved_today as cf_solved
from app.atcoder_api import solved_today as at_solved
from app.activity_logic import status
from app.db import save_daily
from app.reports import daily_report
from app.mailer import send_mail
from app.config import ADMIN_EMAIL

logging.basicConfig(
    filename="logs/daily.log",
    level=logging.INFO
)

today = str(date.today())
members = load_members()

for m in members:
    cf = cf_solved(m["cf"])
    atc = at_solved(m["atcoder"]) if m["atcoder"] else 0
    st = status(cf + atc)

    save_daily(m["email"], today, cf, atc, st)

report = daily_report()
send_mail(
    ADMIN_EMAIL,
    "Daily ICPC Club Activity Report",
    "Attached is today's activity report.",
    report
)
