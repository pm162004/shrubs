import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from shrubs_setup.config import config
from constant import validation_assert
from constant import input_field
from constant import error
import constant
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome()
driver.maximize_window()
email = config.EMAIL
password = config.PASSWORD


driver.get(config.WEB_URL)
time.sleep(3)
wait = WebDriverWait(driver, 25)

def display_myfiles_after_login():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//b[@class='text-active text-xs font-bold sidebar-menu'][normalize-space()='My Files']")))

def email_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "email")))

def password_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "password")))

def login_button():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-signin']")))

def check_blank_email():
    email_variable = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Email address is required')]")))
    return email_variable

def check_blank_password():
    password_variable = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Password is required')]")))
    return password_variable

def check_valid_email():
    email_variable = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Email address is not valid.')]")))
    return email_variable

def check_nonexist_email():
    email_variable = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The selected email is invalid.')]")))
    return email_variable

def check_invalid_password():
    password_variable = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Invalid credentials')]")))
    return password_variable

def refresh_page():
    return driver.refresh()

def password_mask_button():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//*[name()='path' and contains(@d,'M12 7c2.76')]")))

class TestLogin:
    def test_blank_field_validation(self):
        login_button().click()
        assert check_blank_email().text == validation_assert.EMAIL_IS_REQUIRED
        assert check_blank_password().text == validation_assert.ENTER_PASSWORD

    def test_invalid_email(self):
        refresh_page()
        email_input_field().send_keys(input_field.INVALID_EMAIL)
        password_input_field().send_keys(config.CORRECT_PASSWORD)
        login_button().click()
        time.sleep(2)
        assert check_nonexist_email().text == error.NON_EXIST_EMAIL

    def test_invalid_password(self):
        refresh_page()
        email_input_field().send_keys(config.CORRECT_EMAIL)
        password_input_field().send_keys(input_field.INVALID_PASSWORD)
        login_button().click()
        assert check_invalid_password().text == error.PASSWORD_VALIDATION

    def test_incorrect_email(self):
        refresh_page()
        email_input_field().send_keys(input_field.INCORRECT_EMAIL)
        password_input_field().send_keys(config.CORRECT_PASSWORD)
        login_button().click()
        assert check_valid_email().text == error.EMAIL_VALIDATION

    def test_incorrect_password(self):
        refresh_page()
        email_input_field().send_keys(config.CORRECT_EMAIL)
        password_input_field().send_keys(input_field.INCORRECT_PASSWORD)
        login_button().click()
        assert check_invalid_password().text == error.PASSWORD_VALIDATION

    def test_invalid_login_flow(self):
        refresh_page()
        email_input_field().send_keys(config.EMAIL)
        password_input_field().send_keys(config.PASSWORD)
        login_button().click()

    def test_valid_login_flow(self):
        refresh_page()
        email_input_field().send_keys(config.CORRECT_EMAIL)
        password_input_field().send_keys(config.CORRECT_PASSWORD)
        password_mask_button().click()
        login_button().click()
        assert display_myfiles_after_login().text == validation_assert.MY_FILES




