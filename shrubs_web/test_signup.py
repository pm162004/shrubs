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
from shrubs_setup.randomeString import random_string_generator
import constant
from constant import creds, validation_assert,input_field
from constant import error
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
# Only run with the latest Chrome version
driver = webdriver.Chrome()
# driver.set_window_size(1920, 1080)
driver.maximize_window()
driver.get(config.WEB_URL)
# email = config.EMAIL
# password = config.PASSWORD
wait = WebDriverWait(driver, 30)
driver.implicitly_wait(30)


def register():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Create Account']")))

def username_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "username")))

def email_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "email")))

def password_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "password")))

def register_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-signup']")))

def username_blank_validation():
    username = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Username is required')]")))
    return username

def check_blank_email():
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Email address is required')]")))
    return email

def check_blank_password():
    passw = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Password is required')]")))
    return passw

def exist_username_suggestion1_validation():
    # return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Username taken. Please choose another or try test8')]")))
    return wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[contains(text(),'Username taken. Please choose another or try test8')]")
    ))

def exist_username_suggestion2_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Username taken. Please choose another or try admin16')]")))

def exist_email_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The email has already been taken.')]")))

def email_invalid_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Email address is not valid.')]")))

def check_password_length_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The Password field must be at least 8 characters')]")))

def check_strong_password_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The Password Must include uppercase, lowercase, number, and special character')]")))

def success_signup():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Congratulations! Your new account has been successfully created!')]")))

def refresh_page():
    return driver.refresh()

def quit():
    return driver.quit()

class TestSignup:
    def test_blank_field_validation(self):
        register().click()
        action = ActionChains(driver)
        action.move_to_element(register_btn()).click().perform()
        assert username_blank_validation().text == validation_assert.ENTER_SIGNUP_USERNAME
        assert check_blank_email().text == validation_assert.ENTER_SIGNUP_EMAIL
        assert check_blank_password().text == validation_assert.ENTER_SIGNUP_PASSWORD

    def test_exist_uname_suggestion_1(self):
        username_input_field().send_keys(input_field.ALREADY_REGISTERED_UNAME_SUGGESION1)
        time.sleep(1)
        email_input_field().send_keys(input_field.VALID_EMAIL)
        password_input_field().send_keys(input_field.SIGNUP_PASSWORD)
        assert exist_username_suggestion1_validation().text == error.EXIST_USERNAME_SUGGESION1_ERROR
        action = ActionChains(driver)
        action.move_to_element(register_btn()).click().perform()

    def test_exist_uname_suggestion_2(self):
        refresh_page()
        username_input_field().send_keys(input_field.ALREADY_REGISTERED_UNAME_SUGGESION2)
        time.sleep(1)
        email_input_field().send_keys(input_field.VALID_EMAIL)
        password_input_field().send_keys(input_field.SIGNUP_PASSWORD)
        time.sleep(1)
        assert exist_username_suggestion2_validation().text == error.EXIST_USERNAME_SUGGESION2_ERROR
        action = ActionChains(driver)
        action.move_to_element(register_btn()).click().perform()

    def test_exist_email(self):
        refresh_page()
        username_input_field().send_keys(input_field.VALID_UNAME)
        time.sleep(1)
        email_input_field().send_keys(input_field.ALREADY_REGISTERED_EMAIL)
        password_input_field().send_keys(input_field.SIGNUP_PASSWORD)
        time.sleep(1)
        action = ActionChains(driver)
        action.move_to_element(register_btn()).click().perform()
        time.sleep(1)

    def test_invalid_email(self):
        refresh_page()
        username_input_field().send_keys(input_field.VALID_UNAME)
        time.sleep(1)
        email_input_field().send_keys(input_field.INVALID_EMAIL_ID_INPUT)
        password_input_field().send_keys(input_field.SIGNUP_PASSWORD)
        assert email_invalid_validation().text == error.EMAIL_VALIDATION
        action = ActionChains(driver)
        action.move_to_element(register_btn()).click().perform()

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
        action.move_to_element(register_btn()).click().perform()

    def test_strong_validation_password(self):
        refresh_page()
        username_input_field().send_keys(input_field.VALID_UNAME)
        time.sleep(1)
        email_input_field().send_keys(input_field.VALID_EMAIL)
        password_input_field().send_keys(input_field.WRONG_PASSWORD[1])
        assert check_strong_password_validation().text == error.LOWERCASE_PASSWORD
        time.sleep(1)
        action = ActionChains(driver)
        action.move_to_element(register_btn()).click().perform()

    def test_valid_signup(self):
        refresh_page()
        username_input_field().send_keys(randomeString.random_username)
        time.sleep(1)
        em = email_input_field().send_keys(randomeString.email)
        print(em)
        password_input_field().send_keys(randomeString.random_password)
        action = ActionChains(driver)
        action.move_to_element(register_btn()).click().perform()
