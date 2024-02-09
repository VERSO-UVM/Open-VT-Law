import requests
from bs4 import BeautifulSoup
import csv

root_url = "https://legislature.vermont.gov/statutes/title/"
urls = [root_url + str(i).zfill(2) for i in range(1, 100)]
valid_urls = []
all_links = []

for url in urls:
    response = requests.get(url)
    if response.status_code == 200:
        valid_urls.append(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all(class_="item-list statutes-list")
        for item in items:
            links = item.find_all('a')
            for link in links:
                all_links.append(link.get('href'))

all_links = [link.replace('statutes/chapter', 'fullchapter') for link in all_links]

base_url = "https://legislature.vermont.gov/statutes"
full_links = [base_url + link for link in all_links]

with open('full_links.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for link in full_links:
        writer.writerow([link])

print("done")


