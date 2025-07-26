import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = "http://quotes.toscrape.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    # Prepare CSV file
    with open("output/quotes.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author", "Tags"])

        for quote in quotes:
            text = quote.find("span", class_="text").get_text()
            author = quote.find("small", class_="author").get_text()
            tags = ", ".join([tag.get_text() for tag in quote.find_all("a", class_="tag")])
            writer.writerow([text, author, tags])

    print("Scraping completed! Data saved to output/quotes.csv")
else:
    print("Failed to retrieve the page.")
