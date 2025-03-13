import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from Utilities import edit_chrome_options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = edit_chrome_options()

def test_drag_and_drop_positive():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    try:
        # Navigate to drag and drop page
        driver.get('https://the-internet.herokuapp.com/drag_and_drop')
        
        # Find source and target elements
        source = driver.find_element(By.ID, "column-a")
        target = driver.find_element(By.ID, "column-b")
        
        # Create action chain object
        actions = ActionChains(driver)
        
        # Perform drag and drop
        actions.drag_and_drop(source, target).perform()
        
        # Verify the swap occurred
        column_a = driver.find_element(By.XPATH, "//div[@id='column-a']/header")
        assert column_a.text == "B"
        
    finally:
        print("Test completed")


def test_drag_and_drop_negative():
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get('https://the-internet.herokuapp.com/drag_and_drop')
        # Find source and target elements
        source = driver.find_element(By.ID, "column-a")
        target = driver.find_element(By.XPATH, "//a/img")
        
        # Create action chain object
        actions = ActionChains(driver)
        
        # Perform drag and drop
        actions.drag_and_drop(source, target).perform()
        
        # Verify the swap occurred
        column_a = driver.find_element(By.XPATH, "//div[@id='column-a']/header")
        assert column_a.text == "A"
        
    finally:
        print("Test completed")
    

# This line of code is used to run the test when the file is executed directly
if __name__ == "__main__":
    pytest.main([__file__])
