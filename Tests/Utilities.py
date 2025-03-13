from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def edit_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    return chrome_options
