import time

from selenium.common import TimeoutException
from selenium.webdriver.common import keys
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
password = config.CORRECT_PASSWORD
confirm_password = config.NEW_PASSWORD
wait = WebDriverWait(driver, 25)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))

def email_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your email']")))


def password_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your password']")))

def refresh_page():
    driver.refresh()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))  # Wait for the body to load after refresh

def check_invalid_password():
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Invalid credentials')]")))
    return email

def display_myfiles_after_login():
    return wait.until(EC.presence_of_element_located(
        (By.XPATH, "//b[@class='text-active text-xs font-bold sidebar-menu'][normalize-space()='My Files']")))

def change_password_btn():
    btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Change Password')]")))
    return btn

def current_password_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='current-password']")))

def new_password_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='new-password']")))

def confirm_new_password_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='confirm-password']")))



def check_current_password_blank_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Current password is required')]")))

def check_new_password_blank_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'New password is required')]")))

def check_confirm_new_password_blank_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Confirm new password is required')]")))

def check_current_password_length_validation():
    time.sleep(1)
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The Current password field must be at least 8 characters')]")))

def check_new_password_length_validation():
    time.sleep(1)
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The New password field must be at least 8 characters')]")))

def check_incorrect_current_password_validation():
    time.sleep(1)
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The current password is incorrect.')]")))

def check_enter_old_password_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'New password cannot be the same as the current password. Please choose a different password.')]")))

def check_enter_different_confirm_password_validation():
    time.sleep(1)
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Confirm new password field does not match New Password')]")))

def check_current_strong_password_validation():
    time.sleep(1)
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The Current password Must include uppercase, lowercase, number, and special character')]")))

def check_new_strong_password_validation():
    time.sleep(1)
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The New password Must include uppercase, lowercase, number, and special character')]")))

def check_success_message_change_password():
    return wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='You Have Successfully Changed Your Password']")))



def hide_current_password_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[1]")))

def hide_new_password_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[2]")))

def hide_confirm_password_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[3]")))


def droppable_area():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//i[normalize-space()='arrow_drop_down']")))

def overlay_spinner():
    spinner = WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "overlay-spinner"))  # Adjust ID if necessary
    )
    time.sleep(1)
    return spinner

def my_profile():
    overlay_spinner()
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()[normalize-space()='My Profile']]")))


def reset_password_page():
    time.sleep(2)
    overlay_spinner()
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Reset Password')]")))

clear_input = Keys.CONTROL+ 'a' +Keys.BACKSPACE


def check_logout_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Logout' and contains(@class, 'user-menu')]")))

class TestChangePassword:

    def test_login(self):
        email_input_field().send_keys(email)
        password_input_field().send_keys(confirm_password)
        btn_login = wait.until(EC.element_to_be_clickable((By.NAME, "btn-signin")))
        btn_login.click()
        time.sleep(5)
        assert display_myfiles_after_login().text == validation_assert.MY_FILES

    def test_my_wallet(self):
        droppable_area().click()
        my_profile().click()
        reset_password_page().click()

    def test_blank_field_validation(self):
      change_password_btn().click()
      assert check_current_password_blank_validation().text == validation_assert.ENTER_CURRENT_PASSWORD
      assert check_new_password_blank_validation().text == validation_assert.ENTER_NEW_PASSWORD
      assert check_confirm_new_password_blank_validation().text == validation_assert.ENTER_NEW_CONFIRM_PASSWORD


    def test_validation_current_password(self):
        hide_current_password_btn().click()
        current_password_input_field().send_keys(input_field.LENGTH_INVALID_PASSWORD)
        assert check_current_password_length_validation().text == error.CURRENT_LENGTH_VALIDATION_PASSWORD
        current_password_input_field().send_keys(clear_input)
        current_password_input_field().send_keys(input_field.WRONG_PASSWORD[1])
        assert check_current_strong_password_validation().text == error.CURRENT_STRONG_PASSWORD
        current_password_input_field().send_keys(clear_input)
        current_password_input_field().send_keys(config.CORRECT_PASSWORD)

    def test_validation_new_password(self):
        hide_new_password_btn().click()
        new_password_input_field().send_keys(input_field.LENGTH_INVALID_PASSWORD)
        assert check_new_password_length_validation().text == error.NEW_LENGTH_VALIDATION_PASSWORD
        new_password_input_field().send_keys(clear_input)
        new_password_input_field().send_keys(input_field.WRONG_PASSWORD[1])
        assert check_new_strong_password_validation().text == error.NEW_STRONG_PASSWORD
        new_password_input_field().send_keys(clear_input)
        new_password_input_field().send_keys(config.NEW_PASSWORD)

    def test_validation_confirm_password(self):
        hide_confirm_password_btn()
        confirm_new_password_input_field().send_keys(config.CONFIRM_PASSWORD)
        assert check_enter_different_confirm_password_validation().text == error.DIFFERENT_PASSWORD_ERROR

    def test_validation_incorrect_current_password(self):
        refresh_page()
        hide_current_password_btn().click()
        current_password_input_field().send_keys(input_field.OLD_PASSWORD)
        new_password_input_field().send_keys(config.NEW_PASSWORD)
        confirm_new_password_input_field().send_keys(config.NEW_PASSWORD)
        change_password_btn().click()
        assert check_incorrect_current_password_validation().text == error.INCORRECT_CURRENT_PASSWORD_ERROR
        # current_password_input_field().send_keys(clear_input)
        # current_password_input_field().send_keys(config.CORRECT_PASSWORD)

    def test_new_password_as_current_password(self):
       refresh_page()
       current_password_input_field().send_keys(config.NEW_PASSWORD)
       new_password_input_field().send_keys(config.NEW_PASSWORD)
       confirm_new_password_input_field().send_keys(config.NEW_PASSWORD)
       change_password_btn().click()
       assert check_enter_old_password_validation().text == error.OLD_PASSWORD_ERROR



    def test_copy_paste_new_password(self):
        refresh_page()
        current_password_input_field().send_keys(config.CORRECT_PASSWORD)
        new_password_input_field().send_keys(config.NEW_PASSWORD)
        new_password_input_field().send_keys(Keys.CONTROL + 'a')
        new_password_input_field().send_keys(Keys.CONTROL + 'c')
        confirm_new_password_input_field().send_keys(Keys.CONTROL + 'v')


    def test_change_password_flow(self):
        hide_current_password_btn()
        hide_new_password_btn().click()
        hide_confirm_password_btn().click()
        change_password_btn().click()
        assert check_success_message_change_password().text == validation_assert.SUCCESS_TOASTER_MESSAGE_FOR_CHANGE_PASSWORD

    def test_old_password_login(self):
        check_logout_btn().click()
        email_input_field().send_keys(config.CORRECT_EMAIL)
        password_input_field().send_keys(config.CORRECT_PASSWORD)
        assert check_invalid_password().text == error.PASSWORD_VALIDATION
        btn_login = wait.until(EC.element_to_be_clickable((By.NAME, "btn-signin")))
        btn_login.click()

    def test_new_password_login(self):
        driver.refresh()
        email_input_field().send_keys(email)
        password_input_field().send_keys(config.NEW_PASSWORD)
        btn_login = wait.until(EC.element_to_be_clickable((By.NAME, "btn-signin")))
        btn_login.click()
        assert display_myfiles_after_login().text == validation_assert.MY_FILES