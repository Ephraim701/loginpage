from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def ping_scrapers():
    urls = [
        "https://linkage.ng/news.php",
    "https://linkage.ng/newsc.php"
    ]
    results = []
    for url in urls:
        try:
            r = requests.get(url, timeout=600)
            results.append(f"{url} → {r.status_code}")
        except Exception as e:
            results.append(f"{url} → error: {e}")
    return "<br>".join(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
