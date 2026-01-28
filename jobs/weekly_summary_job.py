from app.reports import daily_report
from app.mailer import send_mail
from app.config import ADMIN_EMAIL

report = daily_report()
send_mail(
    ADMIN_EMAIL,
    "Weekly ICPC Club Summary",
    "Weekly summary attached.",
    report
)
