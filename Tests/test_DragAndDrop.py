import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from Utilities import setup_driver

driver = setup_driver()

def test_drag_and_drop_positive():
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
