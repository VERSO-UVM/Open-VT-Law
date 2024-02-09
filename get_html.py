import os
import csv
import requests
from bs4 import BeautifulSoup

# Ensure html_output directory exists
if not os.path.exists('html_output'):
    os.makedirs('html_output')

# Load URLs from CSV file
with open('full_links.csv', 'r') as file:
    reader = csv.reader(file)
    urls = [row[0] for row in reader]

# Fetch and save main content for each URL
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the required elements
    statute_title = soup.find(class_="statute-title")
    statute_chapter = soup.find(class_="statute-chapter")
    statutes_detail = soup.find(class_="item-list statutes-detail")

    # Create a filename from the URL
    filename = "html_output/" + url.replace("https://legislature.vermont.gov/statutes/", "").replace("/", "_") + ".html"

    # Save the required elements to HTML file
    with open(filename, 'w') as file:
        file.write(str(statute_title) + '\n')
        file.write(str(statute_chapter) + '\n')
        file.write(str(statutes_detail))