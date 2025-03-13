import pytest
from selenium.webdriver.common.by import By
from Utilities import edit_chrome_options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = edit_chrome_options()

def test_nested_frames():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    try:
        # Navigate to nested frames page
        driver.get('https://the-internet.herokuapp.com/nested_frames')
        # Find the top frame
        top_frame = driver.find_element(By.CSS_SELECTOR, "frame[name='frame-top']")
        # Switch to the top frame
        driver.switch_to.frame(top_frame)   
        # Find the top left frame
        top_left_frame = driver.find_element(By.CSS_SELECTOR, "frame[name='frame-left']")
        # Switch to the top left frame
        driver.switch_to.frame(top_left_frame)
        # Find the content of the top left frame
        content = driver.find_element(By.CSS_SELECTOR, "body")
        # Verify the content of the top left frame
        assert content.text == "LEFT"
        # Find the top middle frame (first I have to switch back to the top frame)
        driver.switch_to.default_content()
        driver.switch_to.frame(top_frame) 
        top_middle_frame = driver.find_element(By.CSS_SELECTOR, "frame[name='frame-middle']")
        # Switch to the top middle frame
        driver.switch_to.frame(top_middle_frame)
        # Find the content of the tomiddle frame
        content = driver.find_element(By.CSS_SELECTOR, "body")
        # Verify the content of the middle frame
        assert content.text == "MIDDLE"
        # Find the top right frame
        driver.switch_to.default_content()
        driver.switch_to.frame(top_frame) 
        top_right_frame = driver.find_element(By.CSS_SELECTOR, "frame[name='frame-right']")
        # Switch to the top right frame
        driver.switch_to.frame(top_right_frame)
        # Find the content of the top right frame
        content = driver.find_element(By.CSS_SELECTOR, "body")
        # Verify the content of the top right frame
        assert content.text == "RIGHT"
        # Find the bottom frame
        driver.switch_to.default_content()
        bottom_frame = driver.find_element(By.CSS_SELECTOR, "frame[name='frame-bottom']")
        # Switch to the bottom frame
        driver.switch_to.frame(bottom_frame)
        # Find the content of the bottom frame
        content = driver.find_element(By.CSS_SELECTOR, "body")
        # Verify the content of the bottom frame
        assert content.text == "BOTTOM"

    finally:
        print("Test completed")

def test_iframes():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    try:
        # Navigate to iframes page
        driver.get('https://the-internet.herokuapp.com/iframe')
        # Find the iframe
        iframe = driver.find_element(By.CSS_SELECTOR, "iframe")
        # Switch to the iframe
        driver.switch_to.frame(iframe)
        # Find the content of the iframe
        content = driver.find_element(By.CSS_SELECTOR, "body")
        # Verify the content of the iframe
        assert content.text == "Your content goes here."

    finally:
        print("Test completed")
        
        
# This line of code is used to run the test when the file is executed directly
if __name__ == "__main__":
    pytest.main([__file__])
