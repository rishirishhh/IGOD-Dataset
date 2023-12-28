# IGOD Website Scraper

## Overview

This Python script utilizes the Selenium WebDriver library to scrape information from the [IGOD website](https://igod.gov.in/). The script is designed to navigate the site, extract relevant details, and save them to a CSV file.

## Dependencies

- [Selenium](https://www.selenium.dev/)
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager)

## Installation

Ensure you have the necessary dependencies installed:

```bash
pip install selenium webdriver_manager
```
# Script
## Setting Up WebDriver

Configures a headless Chrome browser using WebDriver and ChromeDriverManager.

## Navigating to the Website

Opens the IGOD website using the configured WebDriver.

## Scraping Content

Defines a function (get_element_count()) to count the number of search result rows on the page.

## Initiates a scrolling loop to load dynamic content:

Uses Selenium's ActionChains to simulate the PAGE_DOWN key.
Pauses for a short duration (scroll_pause_time) to allow content to load.
Checks for new content and continues scrolling until the desired element count is reached.
Extracting Data
For each search result row:

# Extracts the title using the class name 'search-title'.

Attempts to find an anchor (<a>) element within the row:
If found, extracts and prints the URL.
If not found, prints a message indicating no URL.
Saving Data
Stores the extracted titles and URLs in lists.

Writes the data to a CSV file located at '/home/maniac/Desktop/python/IGOD-scraper/output_data.csv'.

## Printing Information
Prints the title and URL of each element during the scraping process.

## Closing WebDriver
Closes the WebDriver once the scraping is complete.



