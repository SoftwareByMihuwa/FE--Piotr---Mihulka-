import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities import setup_driver

driver = setup_driver()
driver.get('https://the-internet.herokuapp.com/dynamic_controls')

def test_dynamic_controls_checkbox_remove():
    
    try:
        # Find the checkbox
        checkbox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
        
        # Verify checkbox exists and is displayed
        assert checkbox.is_displayed(), "Checkbox should be visible"
        
        # Click remove button
        remove_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='swapCheckbox()']")
        remove_button.click()
        
        # Wait for "It's gone!" message
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "message")))
        message = driver.find_element(By.ID, "message")
        assert message.text == "It's gone!", "Message should indicate checkbox was removed"
        
        # Verify checkbox no longer exists
        try:
            driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
            assert False, "Checkbox should not be present"
        except:
            assert True, "Checkbox was successfully removed"

        # Click add button (same locator as Remove button)
        remove_button.click()

        # Wait for "It's back!" message
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "message")))
        message = driver.find_element(By.ID, "message")
        assert message.text == "It's back!", "Message should indicate checkbox was removed"
        
        # Verify checkbox no longer exists
        try:
            driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
            assert True, "Checkbox should not be present"
        except:
            assert False, "Checkbox was successfully removed"

    finally:
        print("Test completed")

def test_dynamic_controls_textbox():
    try:
        # Click enable button
        enable_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='swapInput()']")
        enable_button.click()

        # Wait for "It's enabled!" message
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "message")))
        message = driver.find_element(By.ID, "message")
        assert message.text == "It's enabled!", "Message should indicate text field was enabled"

        # Verify text field is enabled and input text
        text_field = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        assert text_field.is_enabled(), "Text field should be enabled"
        text_field.send_keys("Test")

        # Click disable button
        enable_button.click()

        # Wait for "It's disabled!" message
        wait.until(EC.presence_of_element_located((By.ID, "message")))
        message = driver.find_element(By.ID, "message")
        assert message.text == "It's disabled!", "Message should indicate text field was disabled"

        # Verify text field is disabled
        text_field = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        assert not text_field.is_enabled(), "Text field should be disabled"
    finally:
        print("Test completed")
    

# This line of code is used to run the test when the file is executed directly
if __name__ == "__main__":
    pytest.main([__file__])
