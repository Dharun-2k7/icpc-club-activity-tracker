import os
from dotenv import load_dotenv

load_dotenv()

SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

CF_RATE_DELAY = 1.5
ATCODER_RATE_DELAY = 1.5
