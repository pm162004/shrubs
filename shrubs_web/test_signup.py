import time
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from shrubs_setup.config import config
from shrubs_setup import randomeString
from shrubs_setup.randomeString import random_email_generator
import constant
from constant import creds, validation_assert,input_field
from constant import error
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
# Only run with the latest Chrome version
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(config.WEB_URL)
# email = config.EMAIL
# password = config.PASSWORD
wait = WebDriverWait(driver, 30)
driver.implicitly_wait(30)


def create_an_account():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Create Account']")))

def username_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "username")))

def email_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "email")))

def password_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "password")))

def signup_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-signup']")))

def check_blank_username():
    username = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Username is required')]")))
    return username

def check_blank_email():
    email_variable = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Email address is required')]")))
    return email_variable

def check_blank_password():
    password_variable = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Password is required')]")))
    return password_variable

def username1_exists_validation():
    # return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Username taken. Please choose another or try test8')]")))
    return wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[contains(text(),'Username taken. Please choose another or try test8')]")
    ))

def username2_exists_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Username taken. Please choose another or try admin16')]")))

def exist_email_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The email has already been taken.')]")))

def email_invalid_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Email address is not valid.')]")))

def check_password_length_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The Password field must be at least 8 characters')]")))

def check_strong_password_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The Password Must include uppercase, lowercase, number, and special character')]")))

def success_signup_message():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Congratulations! Your new account has been successfully created!')]")))

def refresh_page():
    return driver.refresh()

def quit():
    return driver.quit()

class TestSignup:
    def test_blank_field_validation(self):
        create_an_account().click()
        action = ActionChains(driver)
        action.move_to_element(signup_btn()).click().perform()
        assert check_blank_username().text == validation_assert.ENTER_SIGNUP_USERNAME
        assert check_blank_email().text == validation_assert.ENTER_SIGNUP_EMAIL
        assert check_blank_password().text == validation_assert.ENTER_SIGNUP_PASSWORD

    def test_already_exist_username1(self):
        username_input_field().send_keys(input_field.ALREADY_REGISTERED_USERNAME1)
        time.sleep(1)
        email_input_field().send_keys(input_field.VALID_EMAIL)
        password_input_field().send_keys(input_field.SIGNUP_PASSWORD)
        assert username1_exists_validation().text == error.EXIST_USERNAME_SUGGESION1_ERROR
        action = ActionChains(driver)
        action.move_to_element(signup_btn()).click().perform()

    def test_already_exist_username2(self):
        refresh_page()
        username_input_field().send_keys(input_field.ALREADY_REGISTERED_USERNAME1)
        time.sleep(1)
        email_input_field().send_keys(input_field.VALID_EMAIL)
        password_input_field().send_keys(input_field.SIGNUP_PASSWORD)
        time.sleep(1)
        assert username2_exists_validation().text == error.EXIST_USERNAME_SUGGESION2_ERROR
        action = ActionChains(driver)
        action.move_to_element(signup_btn()).click().perform()

    def test_exist_email(self):
        refresh_page()
        username_input_field().send_keys(input_field.VALID_UNAME)
        time.sleep(1)
        email_input_field().send_keys(input_field.ALREADY_REGISTERED_EMAIL)
        password_input_field().send_keys(input_field.SIGNUP_PASSWORD)
        time.sleep(1)
        action = ActionChains(driver)
        action.move_to_element(signup_btn()).click().perform()
        time.sleep(1)

    def test_invalid_email(self):
        refresh_page()
        username_input_field().send_keys(input_field.VALID_UNAME)
        time.sleep(1)
        email_input_field().send_keys(input_field.INVALID_EMAIL_ID_INPUT)
        password_input_field().send_keys(input_field.SIGNUP_PASSWORD)
        assert email_invalid_validation().text == error.EMAIL_VALIDATION
        action = ActionChains(driver)
        action.move_to_element(signup_btn()).click().perform()

    def test_password_length_validation(self):
        refresh_page()
        username_input_field().send_keys(input_field.VALID_UNAME)
        time.sleep(1)
        email_input_field().send_keys(input_field.VALID_EMAIL)
        password_input_field().send_keys(input_field.INVALID_PASSWORD)
        time.sleep(1)
        assert check_password_length_validation().text == error.CHARACTER_8_PASSWORD
        time.sleep(1)
        action = ActionChains(driver)
        action.move_to_element(signup_btn()).click().perform()

    def test_strong_validation_password(self):
        refresh_page()
        username_input_field().send_keys(input_field.VALID_UNAME)
        time.sleep(1)
        email_input_field().send_keys(input_field.VALID_EMAIL)
        password_input_field().send_keys(input_field.WRONG_PASSWORD[1])
        assert check_strong_password_validation().text == error.LOWERCASE_PASSWORD
        time.sleep(1)
        action = ActionChains(driver)
        action.move_to_element(signup_btn()).click().perform()

    def test_valid_signup(self):
        refresh_page()
        username_input_field().send_keys(randomeString.random_username)
        time.sleep(1)
        em = email_input_field().send_keys(randomeString.email)
        print(em)
        password_input_field().send_keys(randomeString.random_password)
        action = ActionChains(driver)
        action.move_to_element(signup_btn()).click().perform()
