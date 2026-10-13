import requests
from bs4 import BeautifulSoup
url = "https://quotes.toscrape.com/"
r = requests.get(url, timeout=15, headers={"User-Agent":"UniAI-Course/1.0"})
r.raise_for_status()
soup = BeautifulSoup(r.text, "html.parser")
for item in soup.select(".quote"):
    print({
        "text": item.select_one(".text").get_text(strip=True),
        "author": item.select_one(".author").get_text(strip=True),
        "source_url": url
    })
