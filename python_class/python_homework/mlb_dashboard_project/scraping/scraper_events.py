import undetected_chromedriver as uc

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

import time


# URL you're scraping

url = "https://example.com/mlb-events"  # Replace with the actual page



# Set up undetected Chrome driver

options = uc.ChromeOptions()

options.headless = True  # Set to False if you want to see the browser

driver = uc.Chrome(options=options)



driver.get(url)
time.sleep(10)
print("Page title:", driver.title)



# Optional: wait until some known element appears (adjust selector as needed)

try:

    WebDriverWait(driver, 15).until(

        EC.presence_of_element_located((By.TAG_NAME, "table"))  # or any unique element

    )

except:

    print("⚠️ Page didn't load expected elements.")

    driver.quit()

    exit()



# Debug: print page title

print("Page title:", driver.title)


# Example: extract table data

# You can use BeautifulSoup here too if needed

if "Just a moment" in driver.title:
    print("page is being blocked by cloudflare or similar protection.")
driver.quit()
exit()



# Use pandas to read any table on the page (update logic if needed)

tables = pd.read_html(html)

if tables:

    df = tables[0]  # Choose the correct table if there are multiple

    df.to_csv("mlb_events.csv", index=False)

    print("✅ mlb_events.csv created!")

else:

    print("❌ No tables found.")

