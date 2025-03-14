import time
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import logging

# Set up logging
logging.basicConfig(filename='startup_scraper.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Initialize Selenium WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

def scrape_march_tables(url):
    """
    Scrapes funding data for March 2025 from the given URL.

    Args:
        url (str): Webpage URL containing the funding data.

    Returns:
        list: A list of dictionaries with extracted table data.
    """
    all_data = []
    try:
        driver.get(url)
        time.sleep(random.uniform(5, 10))  # Simulate human-like browsing behavior
        
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "gh-table"))
        )

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        logging.info(f"Page source length: {len(driver.page_source)}")

        # Find the section for March 2025
        h2_tags = soup.find_all('h2')
        target_h2 = next((h2 for h2 in h2_tags if "March 2025" in h2.text), None)

        if not target_h2:
            logging.warning("March 2025 section not found.")
            return all_data
        
        # Locate the table under the identified section
        target_div = target_h2.find_next('div', class_='gh-table')
        if not target_div:
            logging.warning("No table found for March 2025.")
            return all_data
        
        table = target_div.find('table')
        if not table:
            logging.warning("Table element not found inside 'gh-table' div.")
            return all_data

        # Extract column headers
        headers = [th.text.strip() for th in table.find_all('thead')[0].find_all('th')]

        # Extract rows
        rows = table.find_all('tbody')[0].find_all('tr')
        for row in rows:
            cells = [cell.text.strip() for cell in row.find_all('td')]
            if len(cells) == len(headers):
                all_data.append(dict(zip(headers, cells)))
            else:
                logging.warning(f"Row length mismatch: {cells}")

        logging.info(f"Scraped {len(all_data)} rows for March 2025.")

    except Exception as e:
        logging.error(f"Scraping error: {str(e)}")
    
    return all_data

def main():
    url = "https://startuptalky.com/indian-startups-funding-investors-data-2025/"  # Replace with actual URL
    march_data = scrape_march_tables(url)

    if march_data:
        pd.DataFrame(march_data).to_csv("startup_march_2025.csv", index=False)
        logging.info("Data saved to startup_march_2025.csv")
    else:
        logging.info("No data found for March 2025.")

    driver.quit()

if __name__ == "__main__":
    main()
