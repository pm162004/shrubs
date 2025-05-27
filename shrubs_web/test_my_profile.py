import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from shrubs_setup.config import config
from constant import validation_assert, input_field, error
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

def email_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "email")))

def password_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "password")))

def display_myfiles_after_login():
    return wait.until(EC.presence_of_element_located(
        (By.XPATH, "//b[@class='text-active text-xs font-bold sidebar-menu'][normalize-space()='My Files']")))

def droppable_area():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//i[normalize-space()='arrow_drop_down']")))

def my_profile():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='user']//li[1]")))

def check_blank_first_name():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'First Name is required')]")))

def check_blank_last_name():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Last Name is required')]")))

def check_blank_phone_number():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Phone number is required')]")))

def check_blank_date_of_birth():
    return wait.until(EC.presence_of_element_located(
        (By.XPATH, "//span[contains(text(),'Date of Birth field is required with valid format')]")))

def check_blank_country():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Country is required')]")))

def check_blank_city():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'City is required')]")))

def check_blank_address():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Address is required')]")))

def check_blank_zip_code():
    return wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Postal Code/Zip Code is required')]")))

def check_blank_state():
    return wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Province / State is required')]")))

def check_invalid_date_of_birth():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Date of birth cannot be in the future')]")))

def check_invalid_phone_number():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Phone number is not valid']")))

def check_invalid_least_phone_number():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Phone number must be at least 10 characters']")))

def check_invalid_greater_than_phone_number():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Phone number must not be greater than 17 characters']")))

def check_invalid_zip_code():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Postal Code/Zip Code must not be greater than 7 characters')]")))

def check_invalid_state():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Province / State may only contain alphabetic characters')]")))

def check_invalid_city():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'City may only contain alphabetic characters')]")))

def check_success_message_for_my_profile():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Your information has been saved')]")))

def firstname_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "first-name")))

def lastname_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "last-name")))

def date_of_birth_input_field():
    return wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[@type='text' and @pattern='[0-9]{2}/[0-9]{2}/[0-9]{4}' and contains(@class, 'md-input')]")))

def date_picker_ok_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Ok')]")))

def phone_no_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "phone-number")))

def country_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='multiselect__select'])[1]")))

def country_select():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Canada')]")))

def address_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "address")))

def city_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "city")))

def state_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "state-or-province")))

def zip_code_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "postal-zip-code")))

def bio_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//div[p[@data-placeholder='Enter text here']]")))

def save_my_profile_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-save']")))


class TestMyProfile:

    def test_login(self):
        logger.info("Running test: Login")
        email_input_field().send_keys(email)
        password_input_field().send_keys(password)
        btn_login = wait.until(EC.element_to_be_clickable((By.NAME, "btn-signin")))
        btn_login.click()
        time.sleep(5)
        assert display_myfiles_after_login().text == validation_assert.MY_FILES
        logger.info("Login successful, 'My Files' is visible")

    def test_my_profile(self):
        logger.info("Running test: Check mandatory field validation messages on My Profile")
        droppable_area().click()
        my_profile().click()
        assert check_blank_first_name().text == validation_assert.ENTER_FIRST_NAME
        assert check_blank_last_name().text == validation_assert.ENTER_LAST_NAME
        assert check_blank_date_of_birth().text == validation_assert.ENTER_DATE
        assert check_blank_phone_number().text == validation_assert.ENTER_PHONE
        assert check_blank_country().text == validation_assert.ENTER_COUNTRY
        assert check_blank_city().text == validation_assert.ENTER_CITY
        assert check_blank_address().text == validation_assert.ENTER_ADDRESS
        assert check_blank_zip_code().text == validation_assert.ENTER_ZIP_CODE
        assert check_blank_state().text == validation_assert.ENTER_STATE
        logger.info("All mandatory field validations for My Profile are verified")

    def test_input_my_profile(self):
        logger.info("Running test: Input invalid and valid data on My Profile")
        firstname_input_field().send_keys(input_field.FIRSTNAME)
        lastname_input_field().send_keys(input_field.LASTNAME)
        date_of_birth_input_field().send_keys(input_field.INVALID_DATE_OF_BIRTH)
        date_picker_ok_btn().click()
        assert check_invalid_date_of_birth().text == error.DATE_OF_BIRTH_VALIDATION
        logger.info("Invalid DOB validation message verified")

        date_of_birth_input_field().send_keys(Keys.CONTROL, "a" + Keys.DELETE)
        date_of_birth_input_field().send_keys(input_field.DATE_OF_BIRTH)
        date_picker_ok_btn().click()

        phone_no_input_field().send_keys(input_field.INVALID_PHONE_NUMBER[0])
        assert check_invalid_least_phone_number().text == error.LEAST_PHONE_NUMBER_ERROR
        logger.info("Phone number too short validation message verified")

        phone_no_input_field().send_keys(Keys.CONTROL, "a" + Keys.DELETE)
        phone_no_input_field().send_keys(input_field.INVALID_PHONE_NUMBER[1])
        assert check_invalid_greater_than_phone_number().text == error.GREATER_PHONE_NUMBER_ERROR
        logger.info("Phone number too long validation message verified")

        phone_no_input_field().send_keys(Keys.CONTROL, "a" + Keys.DELETE)
        phone_no_input_field().send_keys(input_field.INVALID_PHONE_NUMBER[2])
        assert check_invalid_phone_number().text == error.PHONE_VALIDATION
        logger.info("Phone number invalid format validation message verified")

        phone_no_input_field().send_keys(Keys.CONTROL, "a" + Keys.DELETE)
        phone_no_input_field().send_keys(input_field.PHONE_NUMBER)

        country_input_field().click()
        country_select().click()

        address_input_field().send_keys(input_field.ADDRESS)

        city_input_field().send_keys(input_field.INVALID_CITY)
        assert check_invalid_city().text == error.CITY_VALIDATION
        logger.info("Invalid city validation message verified")

        city_input_field().send_keys(Keys.CONTROL, "a" + Keys.DELETE)
        city_input_field().send_keys(input_field.CITY)

        state_input_field().send_keys(input_field.INVALID_STATE)
        assert check_invalid_state().text == error.STATE_VALIDATION
        logger.info("Invalid state validation message verified")

        state_input_field().send_keys(Keys.CONTROL, "a" + Keys.DELETE)
        state_input_field().send_keys(input_field.STATE)

        zip_code_input_field().send_keys(input_field.INVALID_POSTAL_CODE)
        assert check_invalid_zip_code().text == error.POSTAL_CODE_VALIDATION
        logger.info("Invalid postal code validation message verified")

        zip_code_input_field().send_keys(Keys.CONTROL, "a" + Keys.DELETE)
        zip_code_input_field().send_keys(input_field.ZIPCODE)

        bio_input_field().send_keys(input_field.BIO)
        save_my_profile_btn().click()
        assert check_success_message_for_my_profile().text == validation_assert.SUCCESS_MESSAGE_FOR_MY_PROFILE
        logger.info("Profile updated successfully with valid data")