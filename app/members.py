import pandas as pd

CSV_PATH = "data/members.example.csv"  # switch to members.csv later

def load_members():
    df = pd.read_csv(CSV_PATH)
    members = []

    for _, row in df.iterrows():
        members.append({
            "cf": str(row["Codeforces Handle"]).strip(),
            "atcoder": (
                str(row["Atcoder Handle"]).strip()
                if not pd.isna(row["Atcoder Handle"])
                else None
            ),
            "email": row["Email Address ( actively used personal email address)"].strip()
        })
    return members
