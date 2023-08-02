import requests
import selectorlib
from datetime import datetime
import sqlite3

URL = "http://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# Establish a connection to database
connection = sqlite3.connect("data.db")


def scrape(url):
    """This function will scrape the URL and fetch the source."""
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    """This function will extract the required data from the source."""
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temperature"]
    return value


def store(extracted):
    """This function will store the data in database."""
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperatures VALUES(?,?)", (now, extracted))
    connection.commit()


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
    store(extracted)
