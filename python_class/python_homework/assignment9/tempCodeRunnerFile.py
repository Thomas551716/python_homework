# get_books.py

# Task 3: Scrape Durham County Library search results

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

import pandas as pd

import json

import time

# Set up Selenium driver

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

time.sleep(5)  

# wait for page to load

# Find all <li> items that represent a book result

# Update the class name if yours is different!

book_items = driver.find_elements(By.TAG_NAME, "li")

print(f"Found {len(book_items)} total <li> elements")

results = []

for item in book_items:

    try:

        # Get title

        title_el = item.find_element(By.CLASS_NAME, "title-content-link")

        title = title_el.text.strip()



        # Get all authors

        author_els = item.find_elements(By.CLASS_NAME, "contributor-link")

        authors = "; ".join([a.text.strip() for a in author_els])



        # Get format-year

        container = item.find_element(By.CLASS_NAME, "cp-format-info")

        format_year = container.find_element(By.TAG_NAME, "span").text.strip()



        # Add to results list

        results.append({

            "Title": title,

            "Author": authors,

            "Format-Year": format_year

        })



    except Exception as e:

        print(f"Skipped one entry due to error: {e}")



# Create DataFrame

df = pd.DataFrame(results)

print(df)



# Close browser

driver.quit()

# Task 4: Save results to CSV and JSON
df.to_csv("get_books.csv", index=False)
with open("get_books.json", "w") as f:
    json.dump(results, f, indent=2)
    