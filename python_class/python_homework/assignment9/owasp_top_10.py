# owasp_top_10.py

# Task 6: Scrape OWASP Top 10 vulnerabilities

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd

import time

# Start the Selenium WebDriver

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://owasp.org/www-project-top-ten/")

time.sleep(3)  # wait for page to load

# Use XPath to find vulnerability links

vuln_elements = driver.find_elements(By.XPATH, '//a[contains(@href, "/www-project-top-ten/2021/")]')

# Extract title and link

top_10 = []

for el in vuln_elements:

    title = el.text.strip()

    link = el.get_attribute("href")

    if title and link:

        top_10.append({"Title": title, "Link": link})



# Print the results

for vuln in top_10:

    print(vuln)



# Save to CSV

df = pd.DataFrame(top_10)

df.to_csv("owasp_top_10.csv", index=False)



# Close the browser

driver.quit()