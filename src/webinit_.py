from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def initBrowser(headless):
    options = webdriver.FirefoxOptions()
    if(headless):
        options.add_argument('--headless')
    try:
        print('initializing driver...')
        driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()), options=options)
        print('driver successfully initialized')
        return driver
    except Exception as err:
        print(err)
