import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.rottenmangopodcast.com/")

print(response.status_code)