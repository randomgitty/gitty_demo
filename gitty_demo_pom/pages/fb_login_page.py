import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

class FB_LoginPage:
    '''
    Login with newly created credentials. Takes data from test_data.json.
    '''
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.email_field = (By.ID, "email")
        self.password_field = (By.ID, "pass")
        self.login_button = (By.XPATH, "//button[@id='loginbutton']")
        
    def fb_login(self, fb_email, fb_password):
        logger.info("Entering email: %s", fb_email)
        fb_email_field = self.wait.until(EC.presence_of_element_located(self.email_field))
        fb_email_field.clear()
        fb_email_field.send_keys(fb_email)
        
        logger.info("Entering password")
        fb_password_field = self.wait.until(EC.presence_of_element_located(self.password_field))
        fb_password_field.clear()
        fb_password_field.send_keys(fb_password)
        
        logger.info("Clicking login button")
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()