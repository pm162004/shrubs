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
new_password = config.NEW_PASSWORD
confirm_password = config.CONFIRM_PASSWORD
wait = WebDriverWait(driver, 25)
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "body")))
wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))


def forgot_password_button():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='custom-link']")))

def email_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "email")))

def check_blank_email():
    email_variable = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Email address is required')]")))
    return email_variable

def check_valid_email():
    email_variable = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Email address is not valid.')]")))
    return email_variable

def check_nonexist_email():
    email_variable = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'The selected email is invalid.')]")))
    return email_variable

def resend_link_button():
    btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    return btn

def open_new_tab():
    return driver.get("https://www.mailinator.com/")

def yopmail_input_field():
       return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='search']")))

def select_mail():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//td[contains(text(),'🛠️ Did You Lose Your Password… Again?')]")))

def get_reset_password_link():
    driver.switch_to.frame("html_msg_body")
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'🔗 Reset My Password')]")))

def submit_reset_password():
    try:
        driver.refresh()
        driver.switch_to.window(driver.window_handles[-1])
        return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    except TimeoutException:
        print("Reset password link not found.")
        raise

def password_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "password")))

def new_password_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "new-password")))

def confirm_password_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "confirm-password")))

def refresh_page():
    driver.refresh()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))  # Wait for the body to load after refresh

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
    return wait.until(EC.presence_of_element_located((By.XPATH, "//b[@class='text-active text-xs font-bold sidebar-menu'][normalize-space()='My Files']")))

def check_error_confirm_password():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='md-error'][normalize-space()='Repeat New Password field does not match New Password']")))

def hide_password_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//*[name()='path' and contains(@d,'M12 7c2.76')]")))

def check_invalid_password():
    email = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Invalid credentials')]")))
    return email


class TestChangePassword:


    def test_blank_field_validation(self):
     forgot_password_button().click()
     time.sleep(3)
     resend_link_button().click()
     assert check_blank_email().text == validation_assert.EMAIL_IS_REQUIRED
     time.sleep(3)

    def test_change_password_flow(self):

        current_password = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Current Password']")))
        current_password.send_keys("old_password_123")


        new_password = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='New Password']")))
        new_password.send_keys("NewSecurePass@2024")


        confirm_password = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Confirm New Password']")))
        confirm_password.send_keys("NewSecurePass@2024")

        # Click the change password button
        change_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Change Password']")))
        change_button.click()

        # Assert success message appears
        success_message = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Password changed successfully')]")))
        assert success_message.is_displayed(), "Password change success message not found."
    def test_invalid_email(self):
      refresh_page()
      email_input_field().send_keys(input_field.INVALID_EMAIL)
      resend_link_button().click()
      assert check_valid_email().text == error.EMAIL_VALIDATION


    def test_nonexist_email(self):
        refresh_page()
        email_input_field().send_keys(creds.NON_EXISTING_EMAIL)
        resend_link_button().click()
        time.sleep(1)
        assert check_nonexist_email().text == error.NON_EXIST_EMAIL

    def test_valid_email(self):
        refresh_page()
        email_input_field().send_keys(email)
        resend_link_button().click()
        open_new_tab()

    def test_send_resend_link(self):
        time.sleep(3)
        yopmail_input_field().send_keys(email)
        yopmail_input_field().send_keys(Keys.ENTER)
        time.sleep(3)
        select_mail().click()
        time.sleep(3)
        get_reset_password_link().click()

    def test_blank_password_validation(self):
        time.sleep(3)
        submit_reset_password().click()
        assert check_new_password_blank_validation().text == validation_assert.ENTER_NEW_PASSWORD
        assert check_confirm_password_blank_validation().text == validation_assert.ENTER_CONFIRM_PASSWORD

    def test_confirm_password_validation(self):
        new_password_input_field().send_keys(new_password)
        confirm_password_input_field().send_keys(confirm_password)
        assert check_error_confirm_password().text == error.CONFIRM_PASSWORD_VALIDATION
        submit_reset_password().click()

    def test_password_length_validation(self):
        refresh_page()
        new_password_input_field().send_keys(input_field.LENGTH_INVALID_PASSWORD)
        confirm_password_input_field().send_keys(input_field.LENGTH_INVALID_PASSWORD)
        assert check_password_length_validation().text == error.LENGTH_VALIDATION_PASSWORD
        submit_reset_password().click()

    def test_strong_validation_password(self):
        refresh_page()
        new_password_input_field().send_keys(input_field.WRONG_PASSWORD[1])
        confirm_password_input_field().send_keys(input_field.WRONG_PASSWORD[1])
        assert check_strong_password_validation().text == error.STRONG_NEW_PASSWORD
        submit_reset_password().click()

    def test_copy_paste_new_password(self):
        driver.refresh()
        new_password_input_field().send_keys(new_password)
        hide_password_btn().click()
        new_password_input_field().send_keys(Keys.CONTROL + 'a')
        new_password_input_field().send_keys(Keys.CONTROL + 'c')
        confirm_password_input_field().send_keys(Keys.CONTROL + 'v')
        submit_reset_password().click()

    def test_positive_flow(self):
        driver.refresh()
        new_password_input_field().send_keys(new_password)
        confirm_password_input_field().send_keys(new_password)
        submit_reset_password().click()
        back_to_login_btn().click()

    def test_old_password_login(self):
        driver.refresh()
        email_input_field().send_keys(email)
        password_input_field().send_keys(creds.OLD_PASSWORD)
        assert check_invalid_password().text == error.PASSWORD_VALIDATION
        btn_login = wait.until(EC.element_to_be_clickable((By.NAME, "btn-signin")))
        btn_login.click()

    def test_new_password_login(self):
        driver.refresh()
        email_input_field().send_keys(email)
        password_input_field().send_keys(new_password)
        btn_login = wait.until(EC.element_to_be_clickable((By.NAME, "btn-signin")))
        btn_login.click()
        assert display_myfiles_after_login().text == validation_assert.MY_FILES
