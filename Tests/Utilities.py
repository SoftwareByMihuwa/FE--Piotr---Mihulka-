from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def edit_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--ignore-certificate-errors')
    # chrome_options.add_argument('--disable-extensions')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    return chrome_options
