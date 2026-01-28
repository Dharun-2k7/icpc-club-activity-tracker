from app.members import load_members

members = load_members()
print(f"Loaded {len(members)} members")
