import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from shrubs_setup.config import config
from constant import creds, validation_assert, input_field, error
from log_config import setup_logger

logger = setup_logger()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1920, 1080)
driver.get(config.WEB_URL)

email = config.CORRECT_EMAIL
password = config.PASSWORD
new_password = config.RESET_PASSWORD
wait = WebDriverWait(driver, 25)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))

# --- Element locators ---

def email_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your email']")))

def password_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your password']")))

def refresh_page():
    logger.info("Refreshing page")
    driver.refresh()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

def check_invalid_password():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Invalid credentials')]")))

def display_myfiles_after_login():
    return wait.until(EC.presence_of_element_located(
        (By.XPATH, "//b[@class='text-active text-xs font-bold sidebar-menu'][normalize-space()='My Files']")))

def change_password_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Change Password')]")))

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
    return wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[contains(text(),'New password cannot be the same as the current password. Please choose a different password.')]")))

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
    return WebDriverWait(driver, 20).until(
        EC.invisibility_of_element_located((By.ID, "overlay-spinner"))
    )

def my_profile():
    overlay_spinner()
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()[normalize-space()='My Profile']]")))

def reset_password_page():
    time.sleep(2)
    overlay_spinner()
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Reset Password')]")))

clear_input = Keys.CONTROL + 'a' + Keys.BACKSPACE

def quit_browser():
    logger.info("Quitting browser")
    driver.quit()

def check_logout_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Logout' and contains(@class, 'user-menu')]")))

# --- Test Class with logging ---

class TestChangePassword:

    def test_login(self):
        logger.info("Running test: Login with valid credentials")
        email_input_field().send_keys(creds.CHANGE_PASSWORD_EMAIL)
        password_input_field().send_keys(password)
        btn_login = wait.until(EC.element_to_be_clickable((By.NAME, "btn-signin")))
        btn_login.click()
        time.sleep(5)
        assert display_myfiles_after_login().text == validation_assert.MY_FILES
        logger.info("Login successful, 'My Files' visible")

    def test_my_wallet(self):
        logger.info("Navigating to Reset Password page via My Profile")
        droppable_area().click()
        my_profile().click()
        reset_password_page().click()

    def test_blank_field_validation(self):
        logger.info("Testing blank field validation in change password form")
        change_password_btn().click()
        assert check_current_password_blank_validation().text == validation_assert.ENTER_CURRENT_PASSWORD
        assert check_new_password_blank_validation().text == validation_assert.ENTER_NEW_PASSWORD
        assert check_confirm_new_password_blank_validation().text == validation_assert.ENTER_NEW_CONFIRM_PASSWORD
        logger.info("Blank field validations passed")

    def test_validation_confirm_password(self):
        logger.info("Testing confirm password mismatch validation")
        current_password_input_field().send_keys(password)
        new_password_input_field().send_keys(new_password)
        hide_confirm_password_btn().click()
        confirm_new_password_input_field().send_keys(password)
        assert check_enter_different_confirm_password_validation().text == error.DIFFERENT_PASSWORD_ERROR
        logger.info("Confirm password mismatch validation passed")

    def test_validation_current_password(self):
        logger.info("Testing current password validation rules")
        current_password_input_field().send_keys(Keys.CONTROL + 'a' + Keys.BACKSPACE)
        hide_current_password_btn().click()
        current_password_input_field().send_keys(input_field.LENGTH_INVALID_PASSWORD)
        assert check_current_password_length_validation().text == error.CURRENT_LENGTH_VALIDATION_PASSWORD
        current_password_input_field().send_keys(clear_input)
        current_password_input_field().send_keys(input_field.WRONG_PASSWORD[1])
        assert check_current_strong_password_validation().text == error.CURRENT_STRONG_PASSWORD
        current_password_input_field().send_keys(clear_input)
        current_password_input_field().send_keys(password)
        logger.info("Current password validation passed")

    def test_validation_new_password(self):
        logger.info("Testing new password validation rules")
        hide_new_password_btn().click()
        new_password_input_field().send_keys(Keys.CONTROL + 'a' + Keys.BACKSPACE)
        new_password_input_field().send_keys(input_field.LENGTH_INVALID_PASSWORD)
        assert check_new_password_length_validation().text == error.NEW_LENGTH_VALIDATION_PASSWORD
        new_password_input_field().send_keys(clear_input)
        new_password_input_field().send_keys(input_field.WRONG_PASSWORD[1])
        assert check_new_strong_password_validation().text == error.NEW_STRONG_PASSWORD
        new_password_input_field().send_keys(clear_input)
        new_password_input_field().send_keys(new_password)
        logger.info("New password validation passed")

    def test_validation_incorrect_current_password(self):
        logger.info("Testing validation for incorrect current password")
        refresh_page()
        hide_current_password_btn().click()
        current_password_input_field().send_keys(new_password)
        new_password_input_field().send_keys(password)
        confirm_new_password_input_field().send_keys(password)
        change_password_btn().click()
        assert check_incorrect_current_password_validation().text == error.INCORRECT_CURRENT_PASSWORD_ERROR
        logger.info("Incorrect current password validation passed")

    def test_new_password_as_current_password(self):
        logger.info("Testing validation when new password is same as current password")
        refresh_page()
        current_password_input_field().send_keys(password)
        new_password_input_field().send_keys(password)
        confirm_new_password_input_field().send_keys(password)
        change_password_btn().click()
        assert check_enter_old_password_validation().text == error.OLD_PASSWORD_ERROR
        logger.info("New password same as current password validation passed")

    def test_copy_paste_new_password(self):
        logger.info("Testing copy-paste functionality in new password fields")
        refresh_page()
        current_password_input_field().send_keys(password)
        new_password_input_field().send_keys(new_password)
        new_password_input_field().send_keys(Keys.CONTROL + 'a')
        new_password_input_field().send_keys(Keys.CONTROL + 'c')
        hide_confirm_password_btn().click()
        confirm_new_password_input_field().send_keys(Keys.CONTROL + 'v')
        logger.info("Copy-paste test completed")

    def test_change_password_flow(self):
        logger.info("Testing full password change flow")
        hide_current_password_btn()
        hide_new_password_btn().click()
        hide_confirm_password_btn().click()
        change_password_btn().click()
        assert check_success_message_change_password().text == validation_assert.SUCCESS_TOASTER_MESSAGE_FOR_CHANGE_PASSWORD
        logger.info("Password change successful")

    def test_old_password_login(self):
        logger.info("Testing login with old password (should fail)")
        check_logout_btn().click()
        email_input_field().send_keys(creds.CHANGE_PASSWORD_EMAIL)
        password_input_field().send_keys(password)
        assert check_invalid_password().text == error.PASSWORD_VALIDATION
        btn_login = wait.until(EC.element_to_be_clickable((By.NAME, "btn-signin")))
        btn_login.click()
        logger.info("Old password login test passed (login failed as expected)")

    def test_new_password_login(self):
        logger.info("Testing login with new password")
        refresh_page()
        email_input_field().send_keys(creds.CHANGE_PASSWORD_EMAIL)
        password_input_field().send_keys(config.new_password)
        btn_login = wait.until(EC.element_to_be_clickable((By.NAME, "btn-signin")))
        btn_login.click()
        assert display_myfiles_after_login().text == validation_assert.MY_FILES
        logger.info("New password login successful, 'My Files' visible")

        droppable_area().click()
        my_profile().click()
        reset_password_page().click()

        current_password_input_field().send_keys(new_password)
        new_password_input_field().send_keys(password)
        confirm_new_password_input_field().send_keys(password)
        change_password_btn().click()
        quit_browser()
        logger.info("Password reset to original and browser closed")
