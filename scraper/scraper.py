from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import csv
import time

options = Options()
options.add_experimental_option("detach", True)
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://igod.gov.in/advanced_search?keyword_web=&url=&cat_id_search=&sector_id=&state_id=&submit=submit")
print(driver.title)

def get_element_count():
    return len(driver.find_elements(By.CLASS_NAME, 'search-result-row'))

def save_to_csv(titles,urls,file_path):
    # Combine titles and URLs into a list of tuples
    data = list(zip(titles,urls))

    # Write  data to a csv file
    with open(file_path, 'w', newline='',encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)

        # Write header 
        csv_writer.writerow(['Title','URL'])

        # Write data rows
        csv_writer.writerows(data)

titles_list = []
urls_list = []
desired_element_count = 10619
scroll_pause_time = 1
element_counter = 0

while element_counter < desired_element_count:
    # Scroll down to load more content
    actions = ActionChains(driver)
    actions.send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(scroll_pause_time)

    # Extract and print information for each result row
    search_result_rows = driver.find_elements(By.CLASS_NAME, 'search-result-row')
    for result_row in search_result_rows:
        title_element = result_row.find_element(By.CLASS_NAME, 'search-title')
        title_text = title_element.text
        element_counter += 1
        print(f"Title: {title_text}")
        titles_list.append(title_text)

        try:
            anchor_element = result_row.find_element(By.TAG_NAME, 'a')
            href_attribute = anchor_element.get_attribute('href')
            urls_list.append(href_attribute)
            print(f"URL: {href_attribute}")
        except NoSuchElementException:
            print("No URL found for this div")
            urls_list.append("No URL found for this div")
        # Check if the element counter has reached the desired count
        if element_counter >= desired_element_count:
            break
print(element_counter)

file_path = '/home/maniac/Desktop/python/IGOD-scraper/output_data.csv'

save_to_csv(titles_list,urls_list,file_path)
print(f"Scraping complete. Data saved to {file_path}")
driver.close()


