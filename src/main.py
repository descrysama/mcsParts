from webinit_ import initBrowser;
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time;

driver = initBrowser(False);
driver.get("https://www.utopya.fr/customer/account/login/");
connect_button = driver.find_element(by='css selector', value='.button-plain.login');
connect_button.click();

email_input = driver.find_element(by="name", value="login[username]");
time.sleep(3)
driver.execute_script("arguments[0].value = 'New value'", email_input)

##password = driver.find_element(by="name", value="login[password]");
##password.send_keys("Google59");
