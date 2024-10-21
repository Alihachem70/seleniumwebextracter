from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Step 2: Navigate to the website
website_url = "https://www.ccib.org.lb/en/membership-directory/metals-and-metallic-products"  # Replace with your website URL
driver.get(website_url)
print(1)
time.sleep(5)
# Step 3: Locate elements with a specific class name
class_name = "col-lg-3 col-md-4 col-sm-6 col-10 custom-polygon-shadow pb-4 show"  # Replace with the class name you want to target
print(2)

elements = driver.find_elements(By.CLASS_NAME, class_name)
print(3)
# Step 4: Iterate over each element and visit the corresponding URL

for element in elements:
    print(4)

    # Step 4a: Get the link from the element (assuming it's a clickable link)
    link = element.get_attribute("href")

    # Step 4b: Visit the link if it exists
    if link:
        driver.get(link)

        # Step 4c: Perform any actions you need on the page (optional)
        # Add your code here to interact with the page

        # Optional: Add a delay to allow page to load completely (adjust as needed)
        time.sleep(2)

        # Navigate back to the original page if necessary
        driver.back()

        # Add a delay after navigating back (optional)
        time.sleep(1)

# Step 5: Close the WebDriver
driver.quit()