import logging
import unittest
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from pages.fb_login_page import FB_LoginPage
from utils.json_reader import JsonReader
import pytest
import os      
logger = logging.getLogger(__name__)

@allure.feature("E-commerce Checkout")
@allure.story("End-to-End Checkout Flow")


def test_checkout_flow(driver):
    # fb_login_page
    try:
        with allure.step("Facebook Login"):
            test_data = JsonReader.read_test_data("test_data.json")
            fb_login_page = FB_LoginPage(driver)
            driver.get(test_data["fb_login_page"][0]["url"])
            logger.info("Navigated to Facebook login page")
            logger.info("Entering Facebook credentials")
            driver.implicitly_wait(30)
            fb_login_page.fb_login(test_data["fb_credentials"]["fb_email"], test_data["fb_credentials"]["fb_password"])
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
            logger.info("Facebook Login successful")
            driver.implicitly_wait(30)
            
    except Exception as e:
        logger.error("Facebook Login Failed : %s", str(e))
        screenshot_path = f"screenshots/fb_login_error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(screenshot_path) 
if __name__ == "__main__":
    unittest.main()