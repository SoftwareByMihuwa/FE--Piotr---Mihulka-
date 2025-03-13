import pytest
from selenium.webdriver.common.by import By
from Utilities import edit_chrome_options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = edit_chrome_options()

def test_first_shadowDOM():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    try:
        # Navigate to shadow DOM page
        driver.get('https://the-internet.herokuapp.com/shadowdom')
        # Get the shador root host
        shadow_host = driver.find_element(By.XPATH, "//my-paragraph")
        # Access the shadow root using JavaScript
        driver.execute_script("return arguments[0].shadowRoot", shadow_host)
        # Find the element inside the shadow root
        shadow_element = driver.find_element(By.CSS_SELECTOR, "span[slot='my-text']")
        # Verify the text inside the shadow element
        assert shadow_element.text == "Let's have some different text!", "Text does not match"

    finally:
        print("Test completed")

def test_second_shadowDOM():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    try:
        # Navigate to shadow DOM page
        driver.get('https://the-internet.herokuapp.com/shadowdom')
        # Get the shadow root host
        shadow_host = driver.find_element(By.XPATH, "//my-paragraph[2]")
        # Access the shadow root using JavaScript
        driver.execute_script("return arguments[0].shadowRoot", shadow_host)
        # Find the element inside the shadow root
        shadow_element = driver.find_elements(By.CSS_SELECTOR, "ul[slot='my-text'] > li")
        # Verify the text inside the shadow elements
        assert shadow_element[0].text == "Let's have some different text!", "Text does not match"
        assert shadow_element[1].text == "In a list!", "Text does not match"

    finally:
        print("Test completed")


# This line of code is used to run the test when the file is executed directly
if __name__ == "__main__":
    pytest.main([__file__])
