import time,os,datetime

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from shrubs_setup.config import config
from shrubs_setup import randomeString
from constant import validation_assert, input_field, error
from log_config import setup_logger

logger = setup_logger()

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=chrome_options)
chrome_options.add_argument('--headless')
driver.maximize_window()

logger.info("Opening signup page")
driver.get(config.WEB_URL)
wait = WebDriverWait(driver, 30)
driver.implicitly_wait(30)

# Element Getters

def create_an_account():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Create Account']")))

def username_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "username")))

def email_input_field():
    time.sleep(1)
    return wait.until(EC.presence_of_element_located((By.NAME, "email")))

def password_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "password")))

def signup_btn():

    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-signup']")))

def check_blank_username():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Username is required')]")))

def check_blank_email():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Email address is required')]")))

def check_blank_password():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Password is required')]")))

def username_exists_validation():
    return wait.until(EC.visibility_of_element_located((
        By.XPATH, "//span[contains(text(),'Username taken. Please choose another')]"
    )))


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
    logger.info("Refreshing page")
    return driver.refresh()

def quit_browser():
    logger.info("Quitting browser")
    return driver.quit()

def overlay_spinner():
    return WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "overlay-spinner")))

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

class TestSignup:

    def test_blank_field_validation(self):
        logger.info("Running test: Blank field validation")
        create_an_account().click()
        ActionChains(driver).move_to_element(signup_btn()).click().perform()
        assert check_blank_username().text == validation_assert.ENTER_SIGNUP_USERNAME
        logger.info("Blank username validation passed")
        assert check_blank_email().text == validation_assert.ENTER_SIGNUP_EMAIL
        logger.info("Blank email validation passed")
        assert check_blank_password().text == validation_assert.ENTER_SIGNUP_PASSWORD
        logger.info("Blank password validation passed")

    def test_already_exist_username1(self):
        logger.info("Running test: Existing username (suggestion 1)")
        refresh_page()
        username_input_field().send_keys(input_field.ALREADY_REGISTERED_USERNAME1)
        email_input_field().send_keys(input_field.VALID_EMAIL)
        email_input_field().send_keys(Keys.TAB)
        password_input_field().send_keys(input_field.SIGNUP_PASSWORD)
        assert error.EXIST_USERNAME_ERROR in username_exists_validation().text
        logger.info("Username suggestion 1 validation passed")
        ActionChains(driver).move_to_element(signup_btn()).click().perform()



    def test_already_exist_username2(self):
        logger.info("Running test: Existing username (suggestion 2)")
        refresh_page()
        username_input_field().send_keys(input_field.ALREADY_REGISTERED_USERNAME2)
        email_input_field().send_keys(input_field.VALID_EMAIL)
        email_input_field().send_keys(Keys.TAB)
        password_input_field().send_keys(input_field.SIGNUP_PASSWORD)
        assert error.EXIST_USERNAME_ERROR in username_exists_validation().text
        logger.info("Username suggestion 2 validation passed")
        ActionChains(driver).move_to_element(signup_btn()).click().perform()

    def test_exist_email(self):
        logger.info("Running test: Already registered email")
        refresh_page()
        username_input_field().send_keys(input_field.VALID_UNAME)
        email_input_field().send_keys(input_field.ALREADY_REGISTERED_EMAIL)
        email_input_field().send_keys(Keys.TAB)
        password_input_field().send_keys(input_field.SIGNUP_PASSWORD)
        ActionChains(driver).move_to_element(signup_btn()).click().perform()
        assert exist_email_validation().text == error.EXIST_EMAIL_ERROR
        logger.info("Email already taken validation passed")

    def test_invalid_email(self):
        logger.info("Running test: Invalid email format")
        refresh_page()
        username_input_field().send_keys(input_field.VALID_UNAME)
        email_input_field().send_keys(input_field.INVALID_EMAIL_INPUT)
        email_input_field().send_keys(Keys.TAB)
        password_input_field().send_keys(input_field.SIGNUP_PASSWORD)
        assert email_invalid_validation().text == error.EMAIL_VALIDATION
        logger.info("Invalid email format validation passed")
        ActionChains(driver).move_to_element(signup_btn()).click().perform()

    def test_password_length_validation(self):
        logger.info("Running test: Password too short")
        refresh_page()
        username_input_field().send_keys(input_field.VALID_UNAME)
        email_input_field().send_keys(input_field.VALID_EMAIL)
        email_input_field().send_keys(Keys.TAB)
        password_input_field().send_keys(input_field.INVALID_PASSWORD)
        assert check_password_length_validation().text == error.CHARACTER_8_PASSWORD
        logger.info("Short password validation passed")
        ActionChains(driver).move_to_element(signup_btn()).click().perform()

    def test_strong_validation_password(self):
        logger.info("Running test: Weak password strength")
        refresh_page()
        username_input_field().send_keys(input_field.VALID_UNAME)
        email_input_field().send_keys(input_field.VALID_EMAIL)
        email_input_field().send_keys(Keys.TAB)
        password_input_field().send_keys(input_field.WRONG_PASSWORD[1])
        assert check_strong_password_validation().text == error.LOWERCASE_PASSWORD
        logger.info("Weak password strength validation passed")
        ActionChains(driver).move_to_element(signup_btn()).click().perform()

    def test_valid_signup(self):
        logger.info("Running test: Valid signup flow")
        refresh_page()

        uname = randomeString.random_username
        em = randomeString.email
        pwd = randomeString.random_password
        logger.debug(f"Generated credentials: {uname}, {em}, {pwd}")

        username_input_field().send_keys(uname)
        email_input_field().send_keys(em)
        email_input_field().send_keys(Keys.TAB)
        password_input_field().send_keys(pwd)

        ActionChains(driver).move_to_element(signup_btn()).click().perform()
        time.sleep(3)

        try:
            msg = success_signup_message().text
            assert msg.startswith("Congratulations")
            logger.info("Valid signup successful with message: " + msg)
        except Exception as e:
            logger.error("Signup failed or success message not found.")
            save_screenshot("signup_failure.png")
            logger.warning("Screenshot saved as signup_failure.png")

            raise e
        quit_browser()
