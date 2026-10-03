# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///

"""
Fetch daily rainfall data for Hong Kong from Open-Meteo Archive API.
"""

from pathlib import Path
import requests

HERE = Path(__file__).parent
DATA = HERE / "data"
CACHE = DATA / "rainfall.json"
URL = "https://archive-api.open-meteo.com/v1/archive?latitude=22.32&longitude=114.17&start_date=2025-01-01&end_date=2025-12-31&daily=precipitation_sum"

def fetch():
    DATA.mkdir(exist_ok=True)
    print("Fetching rainfall data from Open-Meteo...")
    reply = requests.get(URL, timeout=30, headers={"User-Agent": "Student Project"})
    reply.raise_for_status()
    CACHE.write_text(reply.text, encoding="utf-8")
    print(f"Saved to data/{CACHE.name}")
    return CACHE

if __name__ == "__main__":
    fetch()
