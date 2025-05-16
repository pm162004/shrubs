import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from shrubs_setup.config import config
from constant import creds,validation_assert,input_field
from constant import error


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(config.WEB_URL)
email = config.CORRECT_EMAIL
password = config.PASSWORD
new_password = config.RESET_PASSWORD
wait = WebDriverWait(driver, 25)
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "body")))


def forgot_password_button():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='custom-link']")))

def email_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "email")))

def email_blank_validation():
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Email address is required')]")))
    return email

def email_validation():
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Email address is not valid.')]")))
    return email

def nonexist_email_validation():
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The selected email is invalid.')]")))
    return email

def resend_link_button():
    btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    return btn

def open_new_tab():
    return driver.get("https://www.mailinator.com/")


def yopmail_email_input_field():
       return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='search']")))


def select_mail():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(text(),'🛠️ Did You Lose Your Password… Again?')]")))

def select_reset_btn():
    driver.switch_to.frame("html_msg_body")
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'🔗 Reset My Password')]")))


def reset_password_link():
    try:
        driver.refresh()
        driver.switch_to.window(driver.window_handles[-1])
        return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    except TimeoutException:
        print("Reset password link not found.")
        raise

def login_password():
    return wait.until(EC.presence_of_element_located((By.NAME, "password")))

def valid_password():
    return wait.until(EC.presence_of_element_located((By.NAME, "new-password")))

def valid_confirm_password():
    return wait.until(EC.presence_of_element_located((By.NAME, "confirm-password")))

def refresh_page():
    driver.refresh()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))  # Wait for the body to load after refresh

def back_to_login():
    return wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='btn-reset'][type='button']")))

def new_password_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'New Password is required')]")))

def confirm_password_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Repeat New Password is required')]")))
def password_char_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The New Password field must be at least 8 characters')]")))

def password_special_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The New Password Must include uppercase, lowercase, number, and special character')]")))

def MyFilesPage():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//b[@class='text-active text-xs font-bold sidebar-menu'][normalize-space()='My Files']")))

def error_confirm_password():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='md-error'][normalize-space()='Repeat New Password field does not match New Password']")))

def hide_password():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//*[name()='path' and contains(@d,'M12 7c2.76')]")))

def password_validation():
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Invalid credentials')]")))
    return email


class TestChangePassword:


    def test_blank_field_validation(self):
     forgot_password_button().click()
     time.sleep(3)
     resend_link_button().click()
     assert email_blank_validation().text == validation_assert.ENTER_EMAIL
     time.sleep(3)


    def test_invalid_email(self):
      refresh_page()
      email_input_field().send_keys(input_field.INCORRECT_PASSWORD)
      resend_link_button().click()
      assert email_validation().text == error.EMAIL_VALIDATION


    def test_nonexist_email(self):
        refresh_page()

        email_input_field().send_keys(creds.EXISTING_EMAIL)
        resend_link_button().click()
        time.sleep(1)
        assert nonexist_email_validation().text == error.NON_EXIST_EMAIL

    def test_valid_email(self):
        refresh_page()

        email_input_field().send_keys(email)
        resend_link_button().click()
        open_new_tab()

    def test_resend_link(self):
        time.sleep(3)
        yopmail_email_input_field().send_keys(email)
        yopmail_email_input_field().send_keys(Keys.ENTER)
        time.sleep(3)
        select_mail().click()
        time.sleep(3)
        select_reset_btn().click()

    def test_password_validation(self):
        time.sleep(3)
        reset_password_link().click()

        assert new_password_validation().text == validation_assert.ENTER_NEW_PASSWORD
        assert confirm_password_validation().text == validation_assert.ENTER_CONFIRM_PASSWORD

    def test_confirm_validation(self):
        valid_password().send_keys(password)
        valid_confirm_password().send_keys(new_password)
        assert error_confirm_password().text == error.CONFIRM_PASSWORD_VALIDATION

    reset_password_link().click()
    def test_character_pass(self):
        refresh_page()
        valid_password().send_keys(input_field.INVALID_PASSWORD)
        valid_confirm_password().send_keys(input_field.INVALID_PASSWORD)
        assert password_char_validation().text == error.CHARACTER_8_NEW_PASSWORD
        reset_password_link().click()

    def test_invalid_pass(self):
        refresh_page()
        valid_password().send_keys(input_field.WRONG_PASSWORD[1])
        valid_confirm_password().send_keys(input_field.WRONG_PASSWORD[1])
        assert password_special_validation().text == error.LOWERCASE_NEW_PASSWORD
        reset_password_link().click()

    def test_copy_password(self):
        driver.refresh()
        valid_password().send_keys(password)
        hide_password().click()
        valid_password().send_keys(Keys.CONTROL + 'a')
        valid_password().send_keys(Keys.CONTROL + 'c')
        valid_confirm_password().send_keys(Keys.CONTROL + 'v')
        reset_password_link().click()

    def test_positive_validation(self):
        driver.refresh()
        valid_password().send_keys(password)
        valid_confirm_password().send_keys(password)
        reset_password_link().click()
        back_to_login().click()

    def test_old_login(self):
        driver.refresh()
        email_input_field().send_keys(email)
        login_password().send_keys(creds.OLD_PASSWORD)
        assert password_validation().text == error.PASS_VALIDATION
        btn_login = wait.until(EC.element_to_be_clickable((By.NAME, "btn-signin")))
        btn_login.click()

    def test_login(self):
        driver.refresh()
        email_input_field().send_keys(email)
        login_password().send_keys(password)
        btn_login = wait.until(EC.element_to_be_clickable((By.NAME, "btn-signin")))
        btn_login.click()
        assert MyFilesPage().text == validation_assert.MY_FILES
