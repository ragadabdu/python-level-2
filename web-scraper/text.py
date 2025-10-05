import requests
from bs4 import BeautifulSoup

response = requests.get("https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings")
soup = BeautifulSoup(response.text, "lxml")

# Find the first job card
jobs = soup.find_all("li", class_="new-listing-container feature")
for job in jobs:
    print(job)