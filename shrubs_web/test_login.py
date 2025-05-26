import time,os,datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from shrubs_setup.config import config
from constant import validation_assert, input_field, error
from log_config import setup_logger

logger = setup_logger()

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=chrome_options)
chrome_options.add_argument('--headless')
driver.maximize_window()

email = config.CORRECT_EMAIL
password = config.CORRECT_PASSWORD

logger.info("Launching login page")
driver.get(config.WEB_URL)
time.sleep(3)

wait = WebDriverWait(driver, 25)

# Element getters

def display_myfiles_after_login():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//b[normalize-space()='My Files']")))

def email_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "email")))

def password_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "password")))

def login_button():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-signin']")))

def check_blank_email():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Email address is required')]")))

def check_blank_password():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Password is required')]")))

def check_invalid_email():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Email address is not valid.')]")))

def check_nonexist_email():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The selected email is invalid.')]")))

def check_invalid_password():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Invalid credentials')]")))

def refresh_page():
    logger.info("Refreshing page")
    return driver.refresh()

def password_mask_button():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//*[name()='path' and contains(@d,'M12 7c2.76')]")))

def check_logout_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Logout' and contains(@class, 'user-menu')]")))

def quit_browser():
    time.sleep(1)
    driver.quit()

def save_screenshot(filename, use_timestamp=True, folder="screenshorts"):
    os.makedirs(folder, exist_ok=True)

    if use_timestamp:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = "{}_{}.png".format(filename, timestamp)
    else:
        filename = "{}.png".format(filename)

    full_path = folder, filename
    driver.save_screenshot(f"{folder}/{filename}")  # using global driver
    return full_path

# ============================== TEST CASES ==============================

class TestLogin:

    def test_blank_field_validation(self):
        logger.info("Running test: Blank field validation")
        login_button().click()
        assert check_blank_email().text == validation_assert.EMAIL_IS_REQUIRED
        logger.info("Blank email validation passed")
        assert check_blank_password().text == validation_assert.ENTER_PASSWORD
        save_screenshot("blank_creds")
        logger.info("Blank password validation passed")

    def test_invalid_email(self):
        refresh_page()
        logger.info("Running test: Invalid email (non-existing email)")
        email_input_field().send_keys(input_field.INVALID_EMAIL_INPUT)
        logger.info(f"Entered email: {input_field.INVALID_EMAIL_INPUT}")
        password_input_field().send_keys(config.CORRECT_PASSWORD)
        login_button().click()
        assert check_invalid_email().text == error.EMAIL_VALIDATION
        save_screenshot("invalid_email")
        logger.info("Invalid email format validation passed")


    def test_invalid_password(self):
        refresh_page()
        logger.info("Running test: Invalid password")
        email_input_field().send_keys(config.CORRECT_EMAIL)
        password_input_field().send_keys(input_field.INVALID_PASSWORD)
        logger.info(f"Entered incorrect password: {input_field.INVALID_PASSWORD}")
        login_button().click()
        assert check_invalid_password().text == error.PASSWORD_VALIDATION
        save_screenshot("invalid_password")
        logger.info("Invalid password error validation passed")

    def test_non_exist_email(self):
        refresh_page()
        logger.info("Running test: Incorrectly formatted email")
        email_input_field().send_keys(input_field.NON_EXIST_EMAIL)
        logger.debug(f"Entered invalid email format: {input_field.NON_EXIST_EMAIL}")
        password_input_field().send_keys(config.CORRECT_PASSWORD)
        login_button().click()
        assert check_nonexist_email().text == error.NON_EXIST_EMAIL
        save_screenshot("non_exist_email")
        logger.info("Non-existent email error validation passed")


    def test_incorrect_password(self):
        refresh_page()
        logger.info("Running test: Incorrect password")
        email_input_field().send_keys(config.CORRECT_EMAIL)
        password_input_field().send_keys(input_field.INVALID_PASSWORD)
        login_button().click()
        assert check_invalid_password().text == error.PASSWORD_VALIDATION
        save_screenshot("incorrect_password")
        logger.info("Incorrect password validation passed")

    def test_invalid_login_flow(self):
        refresh_page()
        logger.info("Running test: Completely invalid credentials")
        email_input_field().send_keys(input_field.INVALID_EMAIL_INPUT)
        password_input_field().send_keys(input_field.INVALID_PASSWORD)
        login_button().click()
        assert check_invalid_email().text == error.EMAIL_VALIDATION
        save_screenshot("invalid_logs")
        logger.info("Submitted invalid login - check for error manually")

    def test_valid_login_flow(self):
        logger.info("Running test: Valid login flow")
        refresh_page()
        email_input_field().send_keys(config.CORRECT_EMAIL)
        password_input_field().send_keys(config.CORRECT_PASSWORD)
        password_mask_button().click()
        logger.debug("Clicked password visibility toggle")
        login_button().click()
        assert display_myfiles_after_login().text == validation_assert.MY_FILES
        logger.info("Valid login passed, My Files is visible")
        quit_browser()
