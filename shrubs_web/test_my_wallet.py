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
driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.get(config.WEB_URL)
email = config.CORRECT_EMAIL
password = config.CORRECT_PASSWORD
wait = WebDriverWait(driver, 25)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))

# --- Element locators ---

def email_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your email']")))

def password_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your password']")))

def display_myfiles_after_login():
    return wait.until(EC.presence_of_element_located(
        (By.XPATH, "//b[@class='text-active text-xs font-bold sidebar-menu'][normalize-space()='My Files']")))

def droppable_area():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//i[normalize-space()='arrow_drop_down']")))

def my_profile():
    overlay_spinner()
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()[normalize-space()='My Profile']]")))

def my_wallet():
    time.sleep(2)
    overlay_spinner()
    return wait.until(EC.presence_of_element_located((By.XPATH, "//button[.//div[contains(text(), 'Wallet')]]")))

def check_for_incomplete_wallet():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Your card number is incomplete.']")))

def check_success_toaster_message_for_my_wallet():
    return wait.until(EC.presence_of_element_located((By.XPATH, "(//h2[contains(text(),'Would you like to add this card as your primary method of payment?')])[1]")))

def check_yes_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Yes']")))

def click_save_card_btn():
    overlay_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//div[text()='Save']]")))

def overlay_spinner():
    spinner = WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "overlay-spinner"))
    )
    time.sleep(1)
    return spinner

def check_card_number_input():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='cardnumber']")))

def check_expiry_date_input():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='exp-date']")))

def check_cvv_input():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='cvc']")))

def check_name_on_card_input():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='name-on-card']")))

def check_switch_to_iframe_for_name_on_card():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@title='Secure name on card input frame']")))

def check_switch_to_iframe_for_expiry_date():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@title='Secure expiration date input frame']")))

def check_switch_to_iframe_for_cvv():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@title='Secure CVC input frame']")))

def check_switch_to_iframe_for_card_number():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@title='Secure card number input frame']")))

def check_invalid_card_number():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Your card number is invalid.']")))

def check_declined_card_number():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Your card was declined')]")))

def check_incorrect_card_number():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Your card number is incorrect.']")))

def check_incomplete_card_number():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Your card number is incomplete.']")))

def check_incomplete_cvv():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Your card’s security code is incomplete.']")))

def check_past_expiry_date():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Your card’s expiration year is in the past.']")))

def check_invalid_expiry_date():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Your card’s expiration year is invalid.']")))


# --- Test Class with logging ---

class TestMyWallet:

    def test_login(self):
        logger.info("Running test: Login with valid credentials")
        email_input_field().send_keys(email)
        password_input_field().send_keys(password)
        btn_login = wait.until(EC.element_to_be_clickable((By.NAME, "btn-signin")))
        btn_login.click()
        time.sleep(5)
        assert display_myfiles_after_login().text == validation_assert.MY_FILES
        logger.info("Login successful - 'My Files' visible")

    def test_my_wallet(self):
        logger.info("Navigating to My Wallet")
        droppable_area().click()
        my_profile().click()
        my_wallet().click()
        click_save_card_btn().click()
        assert check_for_incomplete_wallet().text == validation_assert.TOASTER_MESSAGE_FOR_BLANK_WALLET
        logger.info("Blank wallet card number validation passed")

    def test_input_my_wallet_with_incomplete_card_number(self):
        logger.info("Testing wallet input with incomplete card number")
        overlay_spinner()
        driver.switch_to.frame(check_switch_to_iframe_for_card_number())
        check_card_number_input().send_keys(input_field.INCOMPLETE_CARD_NUMBER)
        driver.switch_to.default_content()
        check_name_on_card_input().send_keys(input_field.CARD_NAME)
        driver.switch_to.frame(check_switch_to_iframe_for_expiry_date())
        check_expiry_date_input().send_keys(input_field.EXPIRY_DATE)
        driver.switch_to.default_content()
        driver.switch_to.frame(check_switch_to_iframe_for_cvv())
        check_cvv_input().send_keys(input_field.CVV_NUMBER)
        driver.switch_to.default_content()
        click_save_card_btn().click()
        overlay_spinner()
        assert check_incomplete_card_number().text == error.INCOMPLETE_CARD_NUMBER_ERROR
        logger.info("Incomplete card number error validated")

    def test_input_my_wallet_with_invalid_card_number(self):
        logger.info("Testing wallet input with invalid card number")
        overlay_spinner()
        driver.switch_to.frame(check_switch_to_iframe_for_card_number())
        check_card_number_input().send_keys(input_field.INVALID_CARD_NUMBER)
        driver.switch_to.default_content()
        check_name_on_card_input().send_keys(input_field.CARD_NAME)
        driver.switch_to.frame(check_switch_to_iframe_for_expiry_date())
        check_expiry_date_input().send_keys(input_field.EXPIRY_DATE)
        driver.switch_to.default_content()
        driver.switch_to.frame(check_switch_to_iframe_for_cvv())
        check_cvv_input().send_keys(input_field.CVV_NUMBER)
        driver.switch_to.default_content()
        click_save_card_btn().click()
        overlay_spinner()
        assert check_invalid_card_number().text == error.INVALID_CARD_NUMBER_ERROR
        logger.info("Invalid card number error validated")

    def test_input_my_wallet_with_declined_card_number(self):
        logger.info("Testing wallet input with declined card number")
        overlay_spinner()
        driver.switch_to.frame(check_switch_to_iframe_for_card_number())
        check_card_number_input().send_keys(input_field.DECLINED_CARD_NUMBER)
        driver.switch_to.default_content()
        check_name_on_card_input().send_keys(input_field.CARD_NAME)
        driver.switch_to.frame(check_switch_to_iframe_for_expiry_date())
        check_expiry_date_input().send_keys(input_field.EXPIRY_DATE)
        driver.switch_to.default_content()
        driver.switch_to.frame(check_switch_to_iframe_for_cvv())
        check_cvv_input().send_keys(input_field.CVV_NUMBER)
        driver.switch_to.default_content()
        click_save_card_btn().click()
        overlay_spinner()
        assert check_declined_card_number().text == error.DECLINED_CARD_NUMBER_ERROR
        logger.info("Declined card number error validated")

    def test_input_my_wallet_with_incorrect_card_number(self):
        logger.info("Testing wallet input with incorrect card number")
        overlay_spinner()
        driver.switch_to.frame(check_switch_to_iframe_for_card_number())
        check_card_number_input().send_keys(input_field.INCORRECT_CARD_NUMBER)
        driver.switch_to.default_content()
        check_name_on_card_input().send_keys(input_field.CARD_NAME)
        driver.switch_to.frame(check_switch_to_iframe_for_expiry_date())
        check_expiry_date_input().send_keys(input_field.EXPIRY_DATE)
        driver.switch_to.default_content()
        driver.switch_to.frame(check_switch_to_iframe_for_cvv())
        check_cvv_input().send_keys(input_field.CVV_NUMBER)
        driver.switch_to.default_content()
        click_save_card_btn().click()
        overlay_spinner()
        assert check_incorrect_card_number().text == error.INCORRECT_CARD_NUMBER_ERROR
        logger.info("Incorrect card number error validated")

    def test_input_my_wallet_with_past_expiry_date(self):
        logger.info("Testing wallet input with past expiry date")
        overlay_spinner()
        driver.switch_to.frame(check_switch_to_iframe_for_card_number())
        check_card_number_input().send_keys(input_field.CARD_NUMBER)
        driver.switch_to.default_content()
        check_name_on_card_input().send_keys(input_field.CARD_NAME)
        driver.switch_to.frame(check_switch_to_iframe_for_expiry_date())
        check_expiry_date_input().send_keys(input_field.PAST_EXPIRY_DATE)
        driver.switch_to.default_content()
        driver.switch_to.frame(check_switch_to_iframe_for_cvv())
        check_cvv_input().send_keys(input_field.CVV_NUMBER)
        driver.switch_to.default_content()
        click_save_card_btn().click()
        overlay_spinner()
        assert check_past_expiry_date().text == error.PAST_EXPIRY_DATE_ERROR
        logger.info("Past expiry date error validated")

    def test_input_my_wallet_with_invalid_expiry_date(self):
        logger.info("Testing wallet input with invalid expiry date")
        overlay_spinner()
        driver.switch_to.frame(check_switch_to_iframe_for_card_number())
        check_card_number_input().send_keys(input_field.CARD_NUMBER)
        driver.switch_to.default_content()
        check_name_on_card_input().send_keys(input_field.CARD_NAME)
        driver.switch_to.frame(check_switch_to_iframe_for_expiry_date())
        check_expiry_date_input().send_keys(input_field.INVALID_EXPIRY_DATE)
        driver.switch_to.default_content()
        driver.switch_to.frame(check_switch_to_iframe_for_cvv())
        check_cvv_input().send_keys(input_field.CVV_NUMBER)
        driver.switch_to.default_content()
        click_save_card_btn().click()
        overlay_spinner()
        assert check_invalid_expiry_date().text == error.INVALID_EXPIRY_DATE_ERROR
        logger.info("Invalid expiry date error validated")

    def test_input_my_wallet_with_incomplete_cvv(self):
        logger.info("Testing wallet input with incomplete CVV")
        overlay_spinner()
        driver.switch_to.frame(check_switch_to_iframe_for_card_number())
        check_card_number_input().send_keys(input_field.CARD_NUMBER)
        driver.switch_to.default_content()
        check_name_on_card_input().send_keys(input_field.CARD_NAME)
        driver.switch_to.frame(check_switch_to_iframe_for_expiry_date())
        check_expiry_date_input().send_keys(input_field.EXPIRY_DATE)
        driver.switch_to.default_content()
        driver.switch_to.frame(check_switch_to_iframe_for_cvv())
        check_cvv_input().send_keys(input_field.INCOMPLETE_CVV_NUMBER)
        driver.switch_to.default_content()
        click_save_card_btn().click()
        overlay_spinner()
        assert check_incomplete_cvv().text == error.INCOMPLETE_CVV_ERROR
        logger.info("Incomplete CVV error validated")

    def test_input_my_wallet(self):
        logger.info("Testing wallet input with valid card details")
        overlay_spinner()
        driver.switch_to.frame(check_switch_to_iframe_for_card_number())
        check_card_number_input().send_keys(input_field.CARD_NUMBER)
        driver.switch_to.default_content()
        check_name_on_card_input().send_keys(input_field.CARD_NAME)
        driver.switch_to.frame(check_switch_to_iframe_for_expiry_date())
        check_expiry_date_input().send_keys(input_field.EXPIRY_DATE)
        driver.switch_to.default_content()
        driver.switch_to.frame(check_switch_to_iframe_for_cvv())
        check_cvv_input().send_keys(input_field.CVV_NUMBER)
        driver.switch_to.default_content()
        click_save_card_btn().click()
        assert check_success_toaster_message_for_my_wallet().text == validation_assert.POP_UP_FOR_WALLET
        check_yes_btn().click()
        logger.info("Wallet card added successfully and confirmation accepted")