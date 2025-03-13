import pytest
from selenium.webdriver.common.by import By
from Utilities import edit_chrome_options
import time
import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = edit_chrome_options()

def test_secure_download():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    try:
        # Navigate to secure download page
        driver.get('https://admin:admin@the-internet.herokuapp.com/download_secure')
        # Wait for 10 seconds
        driver.implicitly_wait(10)
        # Find the download link
        download_link = driver.find_element(By.LINK_TEXT, "example.txt")
        # Click the download link
        download_link.click()
        # Wait for file to download (10 seconds max)
        
        downloads_path = str(Path.home() / "Downloads")
        file_path = os.path.join(downloads_path, "example.txt")
        
        timeout = 10
        while timeout > 0:
            if os.path.exists(file_path):
                assert os.path.getsize(file_path) > 0
                break
            time.sleep(1)
            timeout -= 1
            
        # Verify file was downloaded
        assert os.path.exists(file_path), "File was not downloaded"

        # Read and verify file contents
        with open(file_path, 'r') as file:
            content = file.read()
            assert content == "this is example.txt", "File content does not match expected text"

        # Delete the downloaded file
        os.remove(file_path)

    finally:
        print("Test completed")
    
# This line of code is used to run the test when the file is executed directly
if __name__ == "__main__":
    pytest.main([__file__])
