# README: Startup Weekly Scraper

## Overview
This script scrapes startup funding data for **March 2025** from **Startup Weekly** using **Selenium** and **BeautifulSoup**. It extracts structured table data and saves it in a CSV file.

## Prerequisites
Ensure you have the following installed:

- Python 3.x
- Google Chrome browser
- ChromeDriver (automatically managed by `webdriver-manager`)
- Required Python libraries:
  ```bash
  pip install selenium webdriver-manager beautifulsoup4 pandas
  ```

## How It Works
1. **Setup WebDriver**: Initializes a Chrome browser using Selenium.
2. **Load Webpage**: Navigates to the Startup Weekly funding page.
3. **Wait for Content**: Ensures the page loads completely.
4. **Extract Data**: Finds the relevant table for March 2025 using `BeautifulSoup`.
5. **Process Table Data**: Reads headers and rows, converting them into structured dictionaries.
6. **Save Data**: Stores extracted data into `startupweekly_march_2025.csv`.

## Usage
Run the script using:
```bash
python scraper.py
```

This will generate a CSV file containing the extracted data.

## Logs
A log file `startupweekly_scraper.log` is maintained to track execution status and errors.

## Notes
- The script includes **randomized delays** to mimic human browsing behavior.
- For automation, remove manual delays but ensure responsible scraping practices.

## Author
This script is designed for educational and research purposes. Please use it responsibly.
