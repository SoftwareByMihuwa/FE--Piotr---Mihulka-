import pytest
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities import setup_driver

driver = setup_driver()

def test_exit_intent():
    try:
        # Navigate to exit intent page
        driver.get('https://the-internet.herokuapp.com/exit_intent')
        # Move mouse outside of the viewport
        pyautogui.moveTo(2000, 0)
        # Waiting a second to make that the window is visible
        #time.sleep(1)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.modal-footer")))
        # Click on the exit intent
        driver.find_element(By.CSS_SELECTOR, "div.modal-footer").click()
        # Verify the exit intent is closed
        assert driver.find_element(By.CSS_SELECTOR, "div.modal-footer").is_displayed() == False
        
    finally:
        print("Test completed")
    

# This line of code is used to run the test when the file is executed directly
if __name__ == "__main__":
    pytest.main([__file__])
