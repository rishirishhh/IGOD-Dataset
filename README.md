[![DOI](https://zenodo.org/badge/736608146.svg)](https://zenodo.org/doi/10.5281/zenodo.10445632)

# IGOD Website Scraper

## Overview
We have 2 scripts in the Scraper directory :

One is pretty simple and is as follows ->
The Python script is a web scraper designed to extract data from the Indian Government Online Directory (IGOD)   [IGOD website](https://igod.gov.in/) website. It iterates through a range of URLs, sends HTTP requests, and utilizes BeautifulSoup for HTML parsing. The script extracts title and href information from search rows, creating a dictionary where titles serve as keys and corresponding href values are stored. The collected data is then written to a CSV file named "output_data.csv." The script provides flexibility in adjusting the file path for saving the CSV file, making it a versatile tool for scraping IGOD information and storing it in a structured format for further analysis or reference.

The second one is pretty complex ->
The provided Python script utilizes Selenium, a web automation tool, to scrape data from the Indian Government Online Directory (IGOD) website. The script employs a headless Chrome browser to navigate through the IGOD advanced search page, scrolling down dynamically loaded content to ensure comprehensive data retrieval. The script iterates through search result rows, extracting titles and associated URLs from each row. To manage the potentially large dataset, the script utilizes a dictionary (data_dict) to store the extracted information. The scraping process continues until the desired number of elements (specified by desired_element_count) is reached. The collected data is then saved to a CSV file named "output_data.csv" on the desktop. The script provides flexibility for adjusting the file path and serves as a useful tool for systematically retrieving IGOD information for further analysis or reference. As with any web scraping activity, it is important to adhere to ethical scraping practices and be mindful of the website's terms of service.

## Dependencies
1. **Requests:**
   - Library for sending HTTP requests.
   - Install with: `pip install requests`

2. **BeautifulSoup:**
   - HTML parsing library for web scraping.
   - Install with: `pip install beautifulsoup4`

3. **CSV:**
   - Library for reading and writing CSV files.
   - Part of the Python standard library, no separate installation required.

4. **Selenium**
    - Automates the Web browser


# Usage
1. Install the required dependencies using the provided commands.
2. Run the script to initiate web scraping and generate the CSV file.
3. Adjust the file path in the script to specify the location for saving the output CSV file.

# Note
Ensure responsible and ethical use of web scraping practices. Be aware of and comply with the terms of service of the website being scraped. Adjustments to the script may be needed if the structure of the target website changes.

Feel free to modify and adapt the script according to your specific needs or use it as a starting point for web scraping tasks related to IGOD data.