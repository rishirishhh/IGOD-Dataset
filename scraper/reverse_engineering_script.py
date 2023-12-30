import requests
from bs4 import BeautifulSoup
import csv

# Create an empty dictionary to store title and href
data_dict = {}

# Iterate through the range of indices
for index in range(10671):
    # Construct the URL with the current index
    url = f"https://igod.gov.in/advanced_search_more/{index}/5"

    querystring = {"keyword_web": "", "url": "", "cat_id_search": "", "sector_id": "", "org_type_id_search": "", "state_id": ""}
    payload = ""
    headers = {
        "Accept": "*/*",
        "Accept-Language": "en-GB,en;q=0.5",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": "XSRF-TOKEN=...; igod_session=...",
        "Pragma": "no-cache",
        "Referer": f"https://igod.gov.in/advanced_search?keyword_web=&url=&cat_id_search=&sector_id=&state_id=&submit=submit",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all div elements with class 'search-row'
    search_rows = soup.find_all('div', class_='search-row')

    # Loop through each search row
    for search_row in search_rows:
        # Check if there is a div with class 'search-title' directly under the current search row
        title_div = search_row.find('div', class_='search-title')
        if title_div:
            # Extract title from div with class 'search-title'
            title = title_div.text.strip()
        else:
            # Handle the case where the title is inside an 'a' tag under the search row
            title = search_row.find('a', class_='search-title').text.strip()

        # Extract URL from div with class 'search-opts'
        # url = search_row.find('a', class_='btn-detail')['href'].strip()

        direct_link = search_row.find('div', class_='search-result-row').find('a')
        if direct_link:
            href = direct_link['href'].strip()
        else:
            # Handle the case where the link is within the 'a' tag within the 'div' with class 'search-title'
            title_div = search_row.find('div', class_='search-title')
            if title_div:
                link_in_title = title_div.find('a', class_='search-title')
                if link_in_title:
                    href = link_in_title['href'].strip()
                else:
                    href = None
            else:
                href = None

        # Add the data to the dictionary
        data_dict[title] = href

# Write the data dictionary to a CSV file
csv_file_path = "/home/maniac/Desktop/python/IGOD-scraper/output_data.csv"
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Title", "Href"])

    for title, href in data_dict.items():
        csv_writer.writerow([title, href])

print(f"Data saved to {csv_file_path}")
