from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def edit_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920,1080')
    return chrome_options
