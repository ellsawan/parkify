from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup WebDriver for Chrome
driver = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver')

# Test Case 1: Check if the homepage loads correctly
def test_homepage():
    driver.get("http://54.208.103.105:8080/job/parkify/")  # Replace with the URL of your deployed app
    time.sleep(2)  # Wait for the page to load
    assert "Home" in driver.title  # Verify the title contains "Home"
    print("Test Case 1 Passed: Homepage title is correct")

# Test Case 2: Test form submission or a button click (Example)
def test_form_submission():
    driver.get("http://54.208.103.105:8080/job/parkify/")  # Replace with your app's URL
    time.sleep(2)  # Wait for the page to load

    # Find and fill in the form field (example)
    input_field = driver.find_element(By.NAME, "username")  # Replace with the correct input name
    input_field.send_keys("testuser")
    input_field.send_keys(Keys.RETURN)  # Submit form

    time.sleep(2)  # Wait for submission to complete
    assert "Welcome" in driver.page_source  # Verify the page source after form submission
    print("Test Case 2 Passed: Form submission successful")

# Run tests
test_homepage()
test_form_submission()

# Close the browser
driver.quit()
