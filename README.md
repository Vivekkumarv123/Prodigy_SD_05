# Prodigy_SD_05
**#Task_05:  Web Scrape Books with Error Handling (books.csv)**

This Python script scrapes book data (name, price, rating) from a website and saves it to a CSV file named "books.csv". It incorporates error handling to gracefully manage potential issues during data extraction.

**Libraries:**

* `requests`: Fetches web page content.
* `BeautifulSoup`: Parses the HTML structure of the webpage.
* `csv`: Writes data to a CSV file.

**Target Website:**

* This script targets the URL "[http://books.toscrape.com/](http://books.toscrape.com/)" for demonstration purposes. Be mindful of robots.txt and website terms of service when scraping data in practice.

**How it Works:**

1. **Fetches and parses the target webpage.**
2. **Finds elements representing individual book listings.**
3. **Iterates through each book listing:**
   - Extracts book title, price, and rating from the HTML structure.
   - Handles potential errors during extraction using a `try-except` block.
4. **Writes the extracted data (name, price, rating) to a CSV file.**

**Error Handling:**

* The script includes error handling to catch exceptions that might occur during data extraction. This makes the scraping process more robust.

**Note:**

* This script is provided for educational purposes. Always respect website robots.txt and terms of service when scraping data.
* Consider ethical scraping practices and avoid overwhelming the target website with excessive requests.
