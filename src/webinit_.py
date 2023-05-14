from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def initBrowser(headless) :
    options = webdriver.ChromeOptions() 
    if(headless):
        options.add_argument('--headless')
    try :
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        return driver;
    except Exception as err:
        print(err)