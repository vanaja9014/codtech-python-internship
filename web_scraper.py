# CODTECH PYTHON INTERNSHIP - TASK 4
# WEB SCRAPER USING BEAUTIFULSOUP
# Intern: Dasari Vanaja | ID: CITS9786 | Duration: 8 Weeks

import requests
from bs4 import BeautifulSoup
import csv

def scrape_quotes():
    url = "http://quotes.toscrape.com"
    
    print("Connecting to website...")
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to fetch website")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes_div = soup.find_all('div', class_='quote')
    
    data = []
    print(f"\nFound {len(quotes_div)} quotes:\n")
    print("-" * 60)
    
    for q in quotes_div:
        text = q.find('span', class_='text').text
        author = q.find('small', class_='author').text
        tags = ", ".join([t.text for t in q.find_all('a', class_='tag')])
        
        data.append([text, author, tags])
        print(f"Quote: {text}\nAuthor: {author}\nTags: {tags}\n")

    # Save to CSV file
    with open('quotes.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Quote', 'Author', 'Tags'])
        writer.writerows(data)
    
    print("-" * 60)
    print(f"Saved {len(data)} quotes to quotes.csv")
    print("Task 4 Completed - CITS9786")

if __name__ == "__main__":
    scrape_quotes()
