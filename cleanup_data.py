import collect_satellites
import csv
import json
from datetime import datetime, timedelta
from pathlib import Path

LAST_UPDATE = Path("_data/last_update.txt")
TWO_HOURS = timedelta(hours=2.1) #Run over for safety

def can_update():
    if not LAST_UPDATE.exists():
        return True
    
    last_update = datetime.fromisoformat(LAST_UPDATE.read_text().strip())
    
    return datetime.now() - last_update >= TWO_HOURS

def record_update():
    LAST_UPDATE.write_text(
        datetime.now().isoformat()
    )

def format_data():
    
    if (can_update):
        #Update data to latest information if not rate-limited
        try:
            collect_satellites.collect_satellite()
            record_update()
            print("Collection Updated! ")
            
        except Exception as e: 
            print(f"Collection failed: {e}")

    else:
        print("Epoch is up to date.")

    with open("_data/stations.csv", "r") as f:
        reader = csv.DictReader(f)
        data = list(reader)

    print(f"Loaded {len(data)} rows!")

    with open("_data/satellites.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print("Finished")


format_data()
