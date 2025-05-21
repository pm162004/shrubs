import time

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
wait = WebDriverWait(driver, 25)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))


def email_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "email")))


def password_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "password")))


def refresh_page():
    driver.refresh()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))  # Wait for the body to load after refresh


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


def check_toaster_message_for_my_wallet():
    return wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Your card number is incomplete.']")))


def click_save_card_btn():
    overlay_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//div[text()='Save']]")))


def overlay_spinner():
    spinner = WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "overlay-spinner"))  # Adjust ID if necessary
    )
    time.sleep(1)
    return spinner


def click_login_btn():
    overlay_spinner()
    btn_login = wait.until(EC.element_to_be_clickable((By.NAME, "btn-signin")))
    return btn_login


def check_card_number_input():
    card_number_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='cardnumber']")))
    return card_number_input


def check_expiry_date_input():
    expiry_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='exp-date']")))
    return expiry_input


def check_cvv_input():
    cvv_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='cvc']")))
    return cvv_input


def check_name_on_card_input():
    name_on_card_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='name-on-card']")))
    return name_on_card_input


def check_switch_to_iframe_for_name_on_card():
    iframe_name_on_card = wait.until(
        EC.presence_of_element_located((By.XPATH, "//iframe[@title='Secure name on card input frame']")))
    return iframe_name_on_card


def check_switch_to_iframe_for_expiry_date():
    iframe_expiry = wait.until(
        EC.presence_of_element_located((By.XPATH, "//iframe[@title='Secure expiration date input frame']"))
    )
    return iframe_expiry


def check_switch_to_iframe_for_cvv():
    iframe_cvv = wait.until(
        EC.presence_of_element_located((By.XPATH, "//iframe[@title='Secure CVC input frame']"))
    )
    return iframe_cvv


def check_switch_to_iframe_for_card_number():
    iframe_card_number = wait.until(
        EC.presence_of_element_located((By.XPATH, "//iframe[@title='Secure card number input frame']"))
    )
    return iframe_card_number


def check_invalid_card_number():
    return wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Your card number is invalid.']")))


class TestMyProfile:

    def test_login(self):
        email_input_field().send_keys(email)
        password_input_field().send_keys(password)
        btn_login = wait.until(EC.element_to_be_clickable((By.NAME, "btn-signin")))
        btn_login.click()
        time.sleep(5)
        assert display_myfiles_after_login().text == validation_assert.MY_FILES

    def test_my_wallet(self):
        droppable_area().click()
        my_profile().click()
        my_wallet().click()
        click_save_card_btn().click()
        assert check_toaster_message_for_my_wallet().text == validation_assert.TOASTER_MESSAGE_FOR_BLANK_WALLET

    def test_input_my_wallet_with_invalid_card_number(self):
        refresh_page()
        overlay_spinner()
        driver.switch_to.frame(check_switch_to_iframe_for_card_number())
        check_card_number_input().send_keys(input_field.INVALID_CARD_NUMBER)
        driver.switch_to.default_content()
        # driver.switch_to.frame(check_switch_to_iframe_for_name_on_card())
        check_name_on_card_input().send_keys(input_field.CARD_NAME)
        # driver.switch_to.default_content()
        driver.switch_to.frame(check_switch_to_iframe_for_expiry_date())
        check_expiry_date_input().send_keys(input_field.EXPIRY_DATE)  # MMYY format or whatever your app expects
        driver.switch_to.default_content()
        driver.switch_to.frame(check_switch_to_iframe_for_cvv())
        check_cvv_input().send_keys(input_field.CVV_NUMBER)
        driver.switch_to.default_content()
        click_save_card_btn().click()
        time.sleep(5)
        assert check_invalid_card_number().text == error.INVALID_CARD_NUMBER

    def test_input_my_wallet(self):
        overlay_spinner()
        driver.switch_to.frame(check_switch_to_iframe_for_card_number())
        check_card_number_input().send_keys(input_field.CARD_NUMBER)
        driver.switch_to.default_content()
        # driver.switch_to.frame(check_switch_to_iframe_for_name_on_card())
        check_name_on_card_input().send_keys(input_field.CARD_NAME)
        # driver.switch_to.default_content()
        driver.switch_to.frame(check_switch_to_iframe_for_expiry_date())
        check_expiry_date_input().send_keys(input_field.EXPIRY_DATE)  # MMYY format or whatever your app expects
        driver.switch_to.default_content()
        driver.switch_to.frame(check_switch_to_iframe_for_cvv())
        check_cvv_input().send_keys(input_field.CVV_NUMBER)
        driver.switch_to.default_content()
        click_save_card_btn().click()

    # Validate toaster message
    assert check_toaster_message_for_my_wallet().text == validation_assert.TOASTER_MESSAGE_FOR_BLANK_WALLET
