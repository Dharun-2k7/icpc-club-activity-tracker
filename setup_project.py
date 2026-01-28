import os
from app.db import init_db

for f in ["data", "reports", "logs"]:
    os.makedirs(f, exist_ok=True)

init_db()
print("Setup complete.")
