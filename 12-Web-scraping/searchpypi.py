"""
searchpypi.py - Opens several search results.
"""

import sys
import webbrowser

from bs4 import BeautifulSoup
import requests

print("Searching...")
res = requests.get("https://pypi.org/search/?q=" + " ".join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links
soup = BeautifulSoup(res.text, "lxml")

# Open a browser tab for each result
link_elems = soup.select(".package-snippet")
num_open = min(5, len(link_elems))
for i in range(num_open):
    url_to_open = "https://pypi.org" + link_elems[i].get("href")
    print("Opening", url_to_open)
    webbrowser.open(url_to_open)
