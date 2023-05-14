from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

def login(driver: webdriver): 
    driver.get("https://www.utopya.fr/customer/account/login/");
    div = driver.find_element(by="id", value="footer")
    hidden_div = div.find_elements(by="xpath", value=".//div[@style='display: none']")
    driver.execute_script("arguments[0].style.display = 'block';", hidden_div[1])

    email_input = driver.find_element(by="name", value="login[username]");
    email_input.send_keys('louis.lantiez@outlook.com')

    password_input = driver.find_element(by="name", value="login[password]");
    password_input.send_keys('Google59')

    form = driver.find_element(by="id", value="form-popup-login");
    form.find_element(by="id", value="send2").click();
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".account-sidebar")))
    return driver