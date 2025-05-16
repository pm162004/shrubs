import time

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Shrubs_Automation.shrubs_setup.config import config
from Shrubs_Automation.shrubs_setup import randomeString
from Shrubs_Automation.shrubs_setup.randomeString import random_string_generator
import Shrubs_Automation.constant
from Shrubs_Automation.constant import creds, validation_assert,input_field
from Shrubs_Automation.constant import error
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.core.os_manager import ChromeType
# from selenium.webdriver.chrome.service import Service as ChromeService

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

def email_blank_validation():
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Email address is required')]")))
    return email

def pass_blank_validation():
    passw = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Password is required')]")))
    return passw

def exist_username_test_validation():
    # return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Username taken. Please choose another or try test8')]")))
    return wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[contains(text(),'Username taken. Please choose another or try test8')]")
    ))


def exist_username_admin_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Username taken. Please choose another or try admin16')]")))


def exist_email_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The email has already been taken.')]")))

def email_invalid_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Email address is not valid.')]")))


def password_char_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The Password field must be at least 8 characters')]")))

def password_special_validation():
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
        # wait.until(EC.invisibility_of_element_located((By.ID, "overlay-spinner")))
        action = ActionChains(driver)
        action.move_to_element(register_btn()).click().perform()

        assert username_blank_validation().text == validation_assert.ENTER_SIGNUP_USERNAME
        assert email_blank_validation().text == validation_assert.ENTER_SIGNUP_EMAIL
        assert pass_blank_validation().text == validation_assert.ENTER_SIGNUP_PASSWORD

    def test_exist_uname_test(self):

        # register().click()
        username_input_field().send_keys(input_field.ALREADY_REGISTERED_UNAME_TEST)

        time.sleep(1)
        email_input_field().send_keys(input_field.VALID_EMAIL)

        password_input_field().send_keys(input_field.SIGNUP_PASSWORD)
        assert exist_username_test_validation().text == error.EXIST_USERNAME_TEST_ERROR
        action = ActionChains(driver)
        action.move_to_element(register_btn()).click().perform()




    def test_exist_uname_admin(self):
        refresh_page()
        username_input_field().send_keys(input_field.ALREADY_REGISTERED_UNAME_ADMIN)

        time.sleep(1)
        email_input_field().send_keys(input_field.VALID_EMAIL)
        password_input_field().send_keys(input_field.SIGNUP_PASSWORD)
        time.sleep(1)
        assert exist_username_admin_validation().text == error.EXIST_USERNAME_ADMIN_ERROR
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

    def test_character_pass(self):
        refresh_page()
        username_input_field().send_keys(input_field.VALID_UNAME)

        time.sleep(1)
        email_input_field().send_keys(input_field.VALID_EMAIL)
        password_input_field().send_keys(input_field.INVALID_PASSWORD)
        time.sleep(1)
        assert password_char_validation().text == error.CHARACTER_8_PASSWORD
        time.sleep(1)
        action = ActionChains(driver)
        action.move_to_element(register_btn()).click().perform()

    def test_invalid_pass(self):
        refresh_page()
        username_input_field().send_keys(input_field.VALID_UNAME)

        time.sleep(1)
        email_input_field().send_keys(input_field.VALID_EMAIL)
        password_input_field().send_keys(input_field.WRONG_PASSWORD[1])
        assert password_special_validation().text == error.LOWERCASE_PASSWORD
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
        # assert password_special_validation().text == error.LOWERCASE_PASSWORD

        action = ActionChains(driver)
        action.move_to_element(register_btn()).click().perform()



    # def test_exist_email(self):
    #     email_input_field().send_keys(input_field.ALREADY_REGISTERED_EMAIL)
    #     assert exist_email_validation()

    # def test_validation(self):
    #     MyAccountPage().click()
    #     MyAccountPage().click()
    #     if MyAccountPage().text == "Logout":
    #         click_logout_button()
    #     register().click()
    #     signup().click()
    #     assert first_name_validation().text == error.FIRST_NAME_VALIDATION
    #     assert last_name_validation().text == error.LAST_NAME_VALIDATION
    #     assert email_validation().text == error.EMAIL_VALIDATION
    #     assert mobile_no_validation().text == error.MOBILE_NO_VALIDATION
    #     assert set_password_validation().text == error.SET_PASSWORD_VALIDATION
    #     assert agree_validation().text == validation_assert.SELECT_AGREE
    #
    # def test_negative_cases(self):
    #     driver.refresh()
    #     first_name().send_keys(creds.INCORRECT_FIRSTNAME)
    #     last_name().send_keys(creds.INCORRECT_LASTNAME)
    #     email_input_field().send_keys(creds.INCORRECT_EMAIL)
    #     assert email_validation().text == error.EMAIL_VALIDATION
    #     mobile().send_keys(creds.INCORRECT_MOBILE)
    #     assert mobile_no_validation().text == error.MOBILE_NO_VALIDATION
    #     password_input_field().send_keys(creds.INCORRECT_PASSWORD)
    #     assert set_password_validation().text == error.SET_PASSWORD_VALIDATION
    #     confirm_password().send_keys(creds.INCORRECT_CONFIRM_PASSWORD)
    #     confirm_password().send_keys(Keys.BACKSPACE * 2)
    #     # assert confirm_password_validation().text == error.CONFIRM_PASSWORD_VALIDATION
    #
    #     assert agree_validation().text == validation_assert.SELECT_AGREE
    #     signup().click()
    #
    # def test_email_validation(self):
    #     driver.refresh()
    #     signup_btn().click()
    #     first_name().send_keys(creds.FIRSTNAME)
    #     last_name().send_keys(creds.LASTNAME)
    #     email_input_field().send_keys(creds.EXISTING_EMAIL)
    #     mobile().send_keys(creds.MOBILE)
    #     password_input_field().send_keys(password)
    #     confirm_password().send_keys(password)
    #     agree().click()
    #     signup().click()
    #     time.sleep(1)
    #     assert exist_email_validation().text == validation_assert.EXIST_EMAIL
    #
    # def test_password_validation(self):
    #     driver.refresh()
    #     signup_btn().click()
    #     first_name().send_keys(creds.FIRSTNAME)
    #     last_name().send_keys(creds.LASTNAME)
    #     email_input_field().send_keys(creds.EMAIL_ID)
    #     mobile().send_keys(creds.MOBILE)
    #     password_input_field().send_keys(creds.INCORRECT_PASSWORD)
    #     confirm_password().send_keys(creds.INCORRECT_CONFIRM_PASSWORD)
    #     agree().click()
    #     btn_submit().click()
    #     time.sleep(1)
    #     assert confirm_password_validation().text == error.CONFIRM_PASSWORD_VALIDATION
    #
    #
    # def test_positive_case(self):
    #     driver.refresh()
    #     signup_btn().click()
    #     first_name().send_keys(creds.FIRSTNAME)
    #     last_name().send_keys(creds.LASTNAME)
    #     self.email = random_string_generator() + '@gmail.com'
    #     print(self.email)
    #     email_input_field().send_keys(self.email)
    #     mobile().send_keys(creds.MOBILE)
    #     password_input_field().send_keys(password)
    #     confirm_password().send_keys(password)
    #     agree().click()
    #     # signup().click()
    #     btn_submit().click()
    #     # assert verify_otp_validation().text == error.VERIFY_OTP_VALIDATION
    #     # otp = your_otp_validation().text
    #     # verify().send_keys(otp)
    #     # verify().send_keys(Keys.ARROW_LEFT * 4 + Keys.SHIFT + Keys.ARROW_LEFT * 14 + Keys.DELETE)
    #
    #     time.sleep(1)
    #     assert success_signup().text == validation_assert.SUCCESS_MESSAGE
    #     # delete_account_button().click()
    #     # yes_button().click()
    #     time.sleep(1)
    #     click_logout_button().click()
    #     driver.quit()
