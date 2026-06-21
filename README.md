Job Listings Scraper

A Python web scraping project that extracts job listings from the Fake Python Jobs website and stores the data in a CSV file.

Project URL

https://roadmap.sh/projects/job-listings-scraper

Source Website

https://realpython.github.io/fake-jobs/

Features

* Extracts Job Title
* Extracts Company Name
* Extracts Location
* Extracts Job Detail Page URL
* Saves results to a CSV file
* Handles basic missing field scenarios

Technologies Used

* Python
* Requests
* BeautifulSoup4
* CSV Module

Project Structure

fake-jobs-scraper/
│
├── scraper.py
├── jobs.csv
├── requirements.txt
└── README.md

Installation

Install dependencies:

pip install -r requirements.txt

Run the Project


python scraper.py


Output

The scraper generates a CSV file named:


jobs.csv

with the following columns:

* Job Title
* Company Name
* Location
* Job Detail URL

What I Learned

* Sending HTTP requests using Requests
* Parsing HTML using BeautifulSoup
* Extracting structured data from web pages
* Working with lists and loops
* Writing scraped data to CSV files
* Organizing a simple Python project

Author
Amrit Raj
