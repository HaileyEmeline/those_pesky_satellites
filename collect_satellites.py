import requests
from pathlib import Path

def collect_satellite():
    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=csv"
    filename = "_data/stations.csv"

    headers = { "User-Agent": "Mozilla/5.0" }

    r = requests.get(url, headers=headers, timeout=30)
    r.raise_for_status()

    Path(filename).write_bytes(r.content)

    print(f"Downloaded {filename}")