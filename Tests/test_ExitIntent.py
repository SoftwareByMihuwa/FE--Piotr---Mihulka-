import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities import edit_chrome_options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = edit_chrome_options()

def test_exit_intent():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    try:
        # Navigate to exit intent page
        driver.get('https://the-internet.herokuapp.com/exit_intent')
        
        # Trigger exit intent using JavaScript
        driver.execute_script("""
            var event = new MouseEvent('mouseout', {
                'view': window,
                'bubbles': true,
                'cancelable': true,
                'clientX': 0,
                'clientY': -100
            });
            document.dispatchEvent(event);
        """)
        
        # Wait for modal to appear
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
