import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from shrubs_setup.config import config
from constant import creds, validation_assert, input_field, error
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.service import Service as ChromeService

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.get(config.WEB_URL)
email = config.CORRECT_EMAIL
password = config.PASSWORD
wait = WebDriverWait(driver, 25)

def email_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "email")))

def password_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "password")))

def refresh_page():
    driver.refresh()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))  # Wait for the body to load after refresh

def MyFilesPage():
    return wait.until(EC.presence_of_element_located(
        (By.XPATH, "//b[@class='text-active text-xs font-bold sidebar-menu'][normalize-space()='My Files']")))

def droppable_area():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//i[normalize-space()='arrow_drop_down']")))

def droppable_area():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//i[normalize-space()='arrow_drop_down']")))

def my_profile():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='user']//li[1]")))

class TestMyProfile:


  def test_login(self):
     email_input_field().send_keys(email)
     password_input_field().send_keys(password)
     btn_login = wait.until(EC.element_to_be_clickable((By.NAME, "btn-signin")))
     btn_login.click()
     time.sleep(5)
     assert MyFilesPage().text == validation_assert.MY_FILES

  def test_my_profile(self):
      droppable_area().click()
      my_profile().click()
