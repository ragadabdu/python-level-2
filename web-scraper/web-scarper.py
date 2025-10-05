import requests
from bs4 import BeautifulSoup

response = requests.get("https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings")
soup = BeautifulSoup(response.text, "lxml")

# Find the first job card
jobs = soup.find_all("li", class_="new-listing-container feature")

for job in jobs:
    job_title = job.find("h3", class_="new-listing__header__title").text
    job_company_name = job.find("p", class_="new-listing__company-name").text
    job_location = job.find("p", class_="new-listing__company-headquarters").text
    job_posting_date = job.find("p", class_="new-listing__header__icons__date").text
    job_type = ""
    job_salary= ""
    job_link = "https://weworkremotely.com"+job.find("a",href=True)["href"]
    print(job_link)
    
    job_types = ["Full-Time", "Contract"]
    infos = job.find_all("p", class_="new-listing__categories__category")
    for info in infos:
        text = info.get_text(strip=True)
        if "$" in text:
            job_salary = info.text
        elif text in job_types:
            job_type = text
        elif "$" not in text:
            job_salary = "not disclosed"

    print(f'job title: {job_title}\ncompany: {job_company_name}\nsalary: {job_salary}\nloaction: {job_location}\nJob type: {job_type}\nposting date: {job_posting_date}\nlink: {job_link}\n\n')


