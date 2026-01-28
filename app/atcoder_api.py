import requests, time
from datetime import datetime
from app.config import ATCODER_RATE_DELAY

BASE = "https://kenkoooo.com/atcoder/atcoder-api/v3"

def solved_today(handle):
    try:
        r = requests.get(f"{BASE}/user/submissions?user={handle}&from_second=0")
        subs = r.json()
    except Exception:
        return 0

    today = datetime.utcnow().date()
    solved = set()

    for s in subs:
        if s["result"] == "AC":
            d = datetime.utcfromtimestamp(s["epoch_second"]).date()
            if d == today:
                solved.add(s["problem_id"])

    time.sleep(ATCODER_RATE_DELAY)
    return len(solved)
