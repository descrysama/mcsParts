from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def initBrowser(headless):
    options = webdriver.FirefoxOptions()
    if(headless):
        options.add_argument('--headless')
    try:
        driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()), options=options)
        return driver
    except Exception as err:
        print(err)
