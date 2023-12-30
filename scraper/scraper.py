from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import time
import csv

options = Options()
options.add_argument("--headless=new")

# options.add_experimental_option("detach", True)
# options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://igod.gov.in/advanced_search?keyword_web=&url=&cat_id_search=&sector_id=&state_id=&submit=submit")
print(driver.title)

def get_element_count():
    return len(driver.find_elements(By.CLASS_NAME, 'search-result-row'))

# Scroll down to load dynamic content
scroll_pause_time = 1
element_counter = 0
desired_element_count = 10619
data_dict = {}

while len(data_dict) < desired_element_count:
    # Scroll down to load more content
    actions = ActionChains(driver)
    actions.send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(scroll_pause_time)

    # Extract and print information for each result row
    search_result_rows = driver.find_elements(By.CLASS_NAME, 'search-result-row')
    for result_row in search_result_rows:
        title_element = result_row.find_element(By.CLASS_NAME, 'search-title')
        title_text = title_element.text
        # print(f"Title: {title_text}")

        try:
            anchor_element = result_row.find_element(By.TAG_NAME, 'a')
            href_attribute = anchor_element.get_attribute('href')
            data_dict[title_text] = href_attribute
            # print(f"URL: {href_attribute}")
        except NoSuchElementException:
            # print("No URL found for this div")
            data_dict[title_text] = ''

        print(len(data_dict))
        # Check if the element counter has reached the desired count
        if len(data_dict) >= desired_element_count:
            break


csv_file_path = '/home/maniac/Desktop/python/IGOD-scraper/output_data.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Title', 'URL'])
    for title, url in data_dict.items():
        csv_writer.writerow([title, url])

# Close WebDriver
driver.quit()

# Print the data dictionary
print(len(data_dict))
