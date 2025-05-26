import time,datetime,os
from selenium.common import TimeoutException
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
driver = webdriver.Chrome(options=chrome_options)
chrome_options.add_argument('--headless=new')
driver.maximize_window()
driver.get(config.WEB_URL)

email = config.CORRECT_EMAIL
new_password = config.RESET_PASSWORD
confirm_password = config.CONFIRM_PASSWORD

wait = WebDriverWait(driver, 25)
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "body")))
wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))


def forgot_password_button():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='custom-link']")))

def email_input_field():
    time.sleep(1)
    return wait.until(EC.element_to_be_clickable((By.NAME, "email")))

def check_blank_email():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Email address is required')]")))

def check_invalid_email():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Email address is not valid.')]")))

def check_nonexist_email():
    time.sleep(1)
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The selected email is invalid.')]")))

def resend_link_button():
    time.sleep(1)
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

def open_new_tab():
    driver.get("https://www.mailinator.com/")

def yopmail_input_field():
    time.sleep(3)
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='search']")))

def select_mail():
    time.sleep(3)
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(text(),'🛠️ Did You Lose Your Password… Again?')]")))

def get_reset_password_link():
    time.sleep(3)
    driver.switch_to.frame("html_msg_body")
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'🔗 Reset My Password')]")))

def submit_reset_password():
    driver.refresh()
    driver.switch_to.window(driver.window_handles[-1])
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

def password_input_field():
    return wait.until(EC.element_to_be_clickable((By.NAME, "password")))

def new_password_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "new-password")))

def confirm_password_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "confirm-password")))

def refresh_page():
    wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "body")))
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
    time.sleep(1)
    return driver.refresh()

def back_to_login_btn():
    return wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='btn-reset'][type='button']")))

def check_new_password_blank_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'New Password is required')]")))

def check_confirm_password_blank_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Repeat New Password is required')]")))

def check_password_length_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The New Password field must be at least 8 characters')]")))

def check_strong_password_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The New Password Must include uppercase, lowercase, number, and special character')]")))

def display_myfiles_after_login():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//b[normalize-space()='My Files']")))

def check_error_confirm_password():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Repeat New Password field does not match New Password']")))

def hide_password_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//*[name()='path' and contains(@d,'M12 7c2.76')]")))

def check_invalid_password():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Invalid credentials')]")))

def quit_browser():
    logger.info("Quitting browser")
    driver.quit()

def capture_on_failure(test_name, use_timestamp=True, folder="screenshorts"):
    logger.error(f"Test '{test_name}' failed. Capturing screenshot...")
    os.makedirs(folder, exist_ok=True)

    if use_timestamp:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = "{}_{}.png".format(test_name, timestamp)
    else:
        filename = "{}.png".format(test_name)

    full_path = folder, filename

    driver.save_screenshot(f"{test_name}_failure.png")
    logger.info(f"Screenshot saved as: {test_name}_failure.png")
    return full_path

def login_button():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-signin']")))

# ============================== TEST CLASS ==============================

class TestForgotPassword:



    def test_blank_field_validation(self):
        try:
            logger.info("Running test: Blank field validation")
            forgot_password_button().click()
            resend_link_button().click()
            assert check_blank_email().text == validation_assert.EMAIL_IS_REQUIRED
        except Exception as e:
            capture_on_failure("test_blank_field_validation")
            raise e

    def test_invalid_email(self):
        try:
            logger.info("Running test: Invalid email format")
            refresh_page()
            email_input_field().send_keys(input_field.INVALID_EMAIL_INPUT)
            resend_link_button().click()
            assert check_invalid_email().text == error.EMAIL_VALIDATION
        except Exception as e:
            capture_on_failure("test_invalid_email")
            raise e

    def test_nonexist_email(self):
        try:
            refresh_page()
            logger.info("Running test: Non-existing email")

            email_input_field().send_keys(input_field.NON_EXIST_EMAIL)
            resend_link_button().click()
            assert check_nonexist_email().text == error.NON_EXIST_EMAIL
        except Exception as e:
            capture_on_failure("test_nonexist_email")
            raise e

    def test_valid_email(self):
        try:
            logger.info("Running test: Valid email")
            refresh_page()
            email_input_field().send_keys(creds.CHANGE_PASSWORD_EMAIL)
            resend_link_button().click()
            open_new_tab()
        except Exception as e:
            capture_on_failure("test_valid_email")
            raise e

    def test_send_resend_link(self):
        try:
            logger.info("Running test: Open email & reset password")
            yopmail_input_field().send_keys(creds.CHANGE_PASSWORD_EMAIL)
            yopmail_input_field().send_keys(Keys.ENTER)
            select_mail().click()
            get_reset_password_link().click()
        except Exception as e:
            capture_on_failure("test_send_resend_link")
            raise e

    def test_blank_password_validation(self):
        try:
            logger.info("Running test: Blank password validation")
            submit_reset_password().click()
            assert check_new_password_blank_validation().text == validation_assert.ENTER_NEW_FORGOT_PASSWORD
            assert check_confirm_password_blank_validation().text == validation_assert.ENTER_CONFIRM_PASSWORD
        except Exception as e:
            capture_on_failure("test_blank_password_validation")
            raise e

    def test_confirm_password_validation(self):
        try:
            logger.info("Running test: Confirm password mismatch")
            new_password_input_field().send_keys(creds.CHANGE_OLD_PASSWORD)
            confirm_password_input_field().send_keys(creds.CONFIRM_PASSWORD)
            assert check_error_confirm_password().text == error.CONFIRM_PASSWORD_VALIDATION
            submit_reset_password().click()
        except Exception as e:
            capture_on_failure("test_confirm_password_validation")
            raise e

    def test_password_length_validation(self):
        try:
            logger.info("Running test: Password too short")
            refresh_page()
            new_password_input_field().send_keys(input_field.LENGTH_INVALID_PASSWORD)
            confirm_password_input_field().send_keys(input_field.LENGTH_INVALID_PASSWORD)
            assert check_password_length_validation().text == error.LENGTH_VALIDATION_PASSWORD
            submit_reset_password().click()
        except Exception as e:
            capture_on_failure("test_password_length_validation")
            raise e

    def test_strong_validation_password(self):
        try:
            logger.info("Running test: Weak password")
            refresh_page()
            new_password_input_field().send_keys(input_field.WRONG_PASSWORD[1])
            confirm_password_input_field().send_keys(input_field.WRONG_PASSWORD[1])
            assert check_strong_password_validation().text == error.STRONG_NEW_PASSWORD
            submit_reset_password().click()
        except Exception as e:
            capture_on_failure("test_strong_validation_password")
            raise e

    def test_copy_paste_new_password(self):
        try:
            logger.info("Running test: Copy-paste password")
            driver.refresh()
            new_password_input_field().send_keys(creds.RESET_PASSWORD)
            hide_password_btn().click()
            new_password_input_field().send_keys(Keys.CONTROL + 'a')
            new_password_input_field().send_keys(Keys.CONTROL + 'c')
            confirm_password_input_field().send_keys(Keys.CONTROL + 'v')
            submit_reset_password().click()
        except Exception as e:
            capture_on_failure("test_copy_paste_new_password")
            raise e

    def test_positive_flow(self):
        try:
            logger.info("Running test: Positive reset password flow")
            driver.refresh()
            new_password_input_field().send_keys(creds.RESET_PASSWORD)
            confirm_password_input_field().send_keys(creds.RESET_PASSWORD)
            submit_reset_password().click()
            back_to_login_btn().click()
        except Exception as e:
            capture_on_failure("test_positive_flow")
            raise e

    def test_old_password_login(self):
            logger.info("Running test: Login with old password (should fail)")
            driver.get(config.WEB_URL)
            wait.until(EC.element_to_be_clickable((By.NAME, "email")))


            email_input_field().send_keys(creds.CHANGE_PASSWORD_EMAIL)
            time.sleep(0.5)
            password_input_field().send_keys(creds.CHANGE_OLD_PASSWORD)

            login_button().click()
            time.sleep(0.5)
            assert check_invalid_password().text == error.PASSWORD_VALIDATION


    def test_new_password_login(self):
        try:
            refresh_page()
            logger.info("Running test: Login with new password")
            email_input_field().send_keys(creds.CHANGE_PASSWORD_EMAIL)
            password_input_field().send_keys(creds.RESET_PASSWORD)
            login_button().click()
            assert display_myfiles_after_login().text == validation_assert.MY_FILES
            quit_browser()
        except Exception as e:
            capture_on_failure("test_new_password_login")
            raise e
