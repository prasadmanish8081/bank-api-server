import csv
import sys
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

from app.database import SessionLocal, engine
from app.models import Base, Bank, Branch

Base.metadata.create_all(bind=engine)
db = SessionLocal()



csv_file = os.path.join(BASE_DIR, "data", "bank_branches.csv")

banks_map = {}

count = 0

with open(csv_file, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        count += 1
        if count % 1000 == 0:
            print(f"{count} rows imported...")

        bank_name = row["bank_name"]
        bank_id = int(row["bank_id"])

        
        if bank_id not in banks_map:
            bank = Bank(id=bank_id, name=bank_name)
            db.merge(bank)
            banks_map[bank_id] = bank

        
        branch = Branch(
            ifsc=row["ifsc"],
            branch=row["branch"],
            address=row["address"],
            city=row["city"],
            state=row["state"],
            bank_id=bank_id
        )
        db.add(branch)

db.commit()
db.close()

print("Banks and branches imported successfully")
