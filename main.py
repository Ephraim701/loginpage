import requests
import datetime
import time
import random

SCRAPER_URLS = [
    "https://linkage.ng/news.php",
    "https://linkage.ng/newsc.php"
]

def ping_scrapers():
    print(f"--- Cron Run: {datetime.datetime.now()} ---")
    for url in SCRAPER_URLS:
        print(f"Starting: {url}")
        try:
            response = requests.get(url, timeout=600)  # wait up to 10 minutes
            print(f"✅ Completed {url} -> Status: {response.status_code}")
        except requests.exceptions.Timeout:
            print(f"⚠️ Timeout: {url} took too long (>10 mins)")
        except Exception as e:
            print(f"❌ Error pinging {url}: {e}")

        # Optional delay (2–5 seconds) between scrapers
        time.sleep(random.randint(2, 5))

if __name__ == "__main__":
    ping_scrapers()
