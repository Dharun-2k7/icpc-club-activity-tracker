import requests, time
from datetime import datetime, timezone
from app.config import CF_RATE_DELAY

BASE = "https://codeforces.com/api"

def get_submissions(handle):
    try:
        r = requests.get(
            f"{BASE}/user.status?handle={handle}",
            timeout=10
        )
        if r.status_code == 200:
            return r.json().get("result", [])
    except Exception as e:
        print(f"[CF ERROR] {handle}: {e}")
    return []

def solved_today(handle):
    today = datetime.now(timezone.utc).date()
    solved = set()

    for s in get_submissions(handle):
        if s.get("verdict") == "OK":
            d = datetime.fromtimestamp(
                s["creationTimeSeconds"], timezone.utc
            ).date()
            if d == today:
                solved.add(s["problem"]["name"])

    time.sleep(CF_RATE_DELAY)
    return len(solved)
