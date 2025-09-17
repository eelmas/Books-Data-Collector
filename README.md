# Books Data Collector

A Python web scraping project that collects book information from [Books to Scrape](http://books.toscrape.com/).

## Features

- Scrapes book **titles**, **prices**, and **availability**.
- Cleans price data and converts it to numeric values.
- Saves results to `books.csv`.
- Visualizes **price distribution** using a bar chart with Matplotlib.

## Technologies Used

- Python
- Requests
- BeautifulSoup4
- Matplotlib
- CSV

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/eelmas/Books-Data-Collector.git
```
2. Install dependencies:
```bash
pip install requests beautifulsoup4 matplotlib
```
3. Run the script:
```bash
python books_scraper.py
```
The CSV file books.csv will be generated.

A bar chart showing price distribution will pop up.


## Notes

This project is intended for educational purposes and portfolio demonstration.

The website used is Books to Scrape
, which allows web scraping practice.