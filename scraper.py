import csv
import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

titles =  soup.find_all("h2")
company_names = soup.find_all("h3")
locations= soup.find_all("p", class_="location")
urls = soup.find_all("a", string="Apply")

##

with open("jobs.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Header row
    writer.writerow(["Job Title", "Company Name", "Location", "URL"])

    # Data rows
    for title, company, location, url in zip(titles, company_names, locations, urls):
        writer.writerow([
            title.get_text(strip=True),
            company.get_text(strip=True),
            location.get_text(strip=True),
            url.get("href")
        ])

print("Data saved to jobs.csv")
