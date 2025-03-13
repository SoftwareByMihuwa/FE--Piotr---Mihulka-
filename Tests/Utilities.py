from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    return webdriver.Chrome(options=chrome_options) 