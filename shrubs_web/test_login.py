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

def MyFilesPage():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//b[@class='text-active text-xs font-bold sidebar-menu'][normalize-space()='My Files']")))

def email_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "email")))

def password_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "password")))

def login_button():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-signin']")))

def email_blank_validation():
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Email address is required')]")))
    return email

def pass_blank_validation():
    passw = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Password is required')]")))
    return passw

def email_validation():
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Email address is not valid.')]")))
    return email

def nonexist_email_validation():
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The selected email is invalid.')]")))
    return email

def password_validation():
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Invalid credentials')]")))
    return email

def refresh_page():
    return driver.refresh()

def password_mask_button():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//*[name()='path' and contains(@d,'M12 7c2.76')]")))

class TestLogin:
    def test_blank_field_validation(self):
        login_button().click()
        assert email_blank_validation().text == validation_assert.ENTER_EMAIL
        assert pass_blank_validation().text == validation_assert.ENTER_PASSWORD

    def test_invalid_email(self):
        refresh_page()
        email_input_field().send_keys(input_field.INVALID_EMAIL)
        password_input_field().send_keys(config.CORRECT_PASSWORD)
        login_button().click()
        time.sleep(2)
        assert nonexist_email_validation().text == error.NON_EXIST_EMAIL

    def test_invalid_password(self):
        refresh_page()
        email_input_field().send_keys(config.CORRECT_EMAIL)
        password_input_field().send_keys(input_field.INVALID_PASSWORD)
        login_button().click()
        assert password_validation().text == error.PASS_VALIDATION

    def test_incorrect_email(self):
        refresh_page()
        email_input_field().send_keys(input_field.INCORRECT_EMAIL)
        password_input_field().send_keys(config.CORRECT_PASSWORD)
        login_button().click()
        assert email_validation().text == error.EMAIL_VALIDATION

    def test_incorrect_password(self):
        refresh_page()
        email_input_field().send_keys(config.CORRECT_EMAIL)
        password_input_field().send_keys(input_field.INCORRECT_PASSWORD)
        login_button().click()
        assert password_validation().text == error.PASS_VALIDATION

    def test_both_invalid(self):
        refresh_page()
        email_input_field().send_keys(config.EMAIL)
        password_input_field().send_keys(config.PASSWORD)
        login_button().click()

    def test_valid(self):
        refresh_page()
        email_input_field().send_keys(config.CORRECT_EMAIL)
        password_input_field().send_keys(config.CORRECT_PASSWORD)
        password_mask_button().click()
        login_button().click()
        assert MyFilesPage().text == validation_assert.MY_FILES




