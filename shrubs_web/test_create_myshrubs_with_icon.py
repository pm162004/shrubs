import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
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

def email_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "email")))

def password_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "password")))

def refresh_page():
    driver.refresh()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))  # Wait for the body to load after refresh

def MyFilesPage():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//b[@class='text-active text-xs font-bold sidebar-menu'][normalize-space()='My Files']")))

def myShrubs():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='My Shrubs']")))

def new_shrub():
    return wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".md-button-content")))

def shrubs_title_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "shrub-name")))

def shrubs_title_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Shrub Title is required']")))

def shrubs_background_color():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Background']")))

def shrubs_icon_color():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='center cursor-pointer flex items-center box-square-50']//img[@alt='thumbnail']")))

def shrubs_icon_type():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Color:#BD10E0']")))

def overlay_spinner():
    btn =  WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "overlay-spinner"))  # Adjust ID if necessary
    )
    return btn
def progress_spinner():
    btn =   WebDriverWait(driver, 30).until(
        EC.invisibility_of_element_located((By.ID, "progress-spinner"))  # Wait for the spinner to disappear
    )
    return btn


def shrubs_already_exits_validation():

    try:
        driver.find_element(By.NAME, "btn-save").click()
        error_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Project already exist with the given slug']"))
        )

        if error_message:
         print("Error message found:", error_message.text)
        return error_message.text

    except TimeoutException:
        print("No error message found within the timeout period.")
        try:
            alert = driver.switch_to.alert
            msg = alert.text
            print("Alert box contains the following message," + msg)
            return msg
        except:
            print("Alert not found, checking for modal or error message.")

        try:
            error_message = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Project already exist with the given slug']"))
            )

            if error_message:
                print("Modal error message found:", error_message.text)
            return error_message.text
        except TimeoutException:
            print("No modal or error message found.")
            return None

def shrubs_permissions_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Permissions field is required']")))

def shrubs_thumbnail_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Thumbnail type field is required']")))

def new_branch():
    overlay_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-new-branch']")))

def shrubs_btn():
    # Wait until the overlay (spinner) is no longer visible
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "overlay-spinner"))  # Adjust ID if necessary
    )


    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "btn-save"))
    )
    return button
def show_title():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Do you want to show the title?']")))

def shrubs_view_only():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='View Only']")))

def hide_thumbnail():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Do you want to show thumbnail?']")))

def select_type():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Shrub Project Icon']")))

def select_icon():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//h6[normalize-space()='alert-octagon']")))

def close_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Cancel')]")))

def save_style():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='md-button all-button-height br6 font-size-16 md-theme-default md-ripple-off md-primary mt1 mr1 h50']")))

def save_header():
    # Wait until the overlay (spinner) is no longer visible
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "overlay-spinner"))  # Adjust ID if necessary
    )

    # Wait for the button to be clickable
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='md-button all-button-height br6 font-size-16 md-theme-default md-ripple-off md-primary mt1 mr1 h50']")))
    return button

def create_link():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='Create Links']")))
def list_branch_list():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Branch Title']")))
def list_branch_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//small[@class='text-danger']")))
def save_branch():
    # Wait until the overlay (spinner) is no longer visible
    overlay_spinner()
    # Wait for the button to be clickable
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='md-button all-button-height br6 md-theme-default md-ripple-off md-primary h50 w-100 font-size-16']//div[@class='md-ripple md-disabled']")))
    return button
def add_link():
    progress_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-upload-image']//div[@class='md-ripple md-disabled']")))
def link_input_field():

    progress_spinner()
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Link']")))
def link_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='md-error']")))
def link_error():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='md-error']")))
def link_save_btn():
    progress_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='md-button all-button-height br6 md-theme-default md-ripple-off md-primary h50 w-100 font-size-16']")))
def back_branch():
    progress_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Back')]")))


def link_save_msg(driver):
    try:
        # Wait until the success message with class 'text-success' is visible
        success_message = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='text-success']"))
        )
        return success_message
    except TimeoutException:
        print("Timeout: Success message with class 'text-success' not found!")
        # Log the page source for debugging
        print(driver.page_source)
        return None
    except Exception as e:
        # Catch any other unexpected exceptions and log the error
        print(f"An error occurred: {e}")
        return None

def back_link():
    progress_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='md-button all-button-height br6 md-theme-default md-ripple-off md-danger h50 w-100 font-size-16 mr1']//div[@class='md-ripple md-disabled']")))

def test_login():

    email_input_field().send_keys(email)
    password_input_field().send_keys(password)
    btn_login = wait.until(EC.element_to_be_clickable((By.NAME, "btn-signin")))
    btn_login.click()
    assert MyFilesPage().text == validation_assert.MY_FILES

def test_myShrubs():
    myShrubs().click()
    time.sleep(10)
    new_shrub().click()

def test_blank_shrubs():
    shrubs_btn().click()
    assert shrubs_title_validation().text == validation_assert.ENTER_SHRUBS_TITLE
    assert shrubs_permissions_validation().text == validation_assert.ENTER_SHRUBS_PERMISSIONS
    assert shrubs_thumbnail_validation().text == validation_assert.ENTER_SHRUBS_THUMBNAIL


def test_already_exist_shrubs():
    refresh_page()
    shrubs_title_input_field().send_keys(input_field.EXISTING_SHRUBS)

    # shrubs_btn().click()
    shrubs_view_only().click()
    select_type().click()
    select_icon().click()
    close_btn().click()
    # shrubs_btn().click()
    time.sleep(2)
    assert shrubs_already_exits_validation()== validation_assert.EXISTS_SHRUBS_TITLE

def test_valid_shrubs():
    refresh_page()
    shrubs_title_input_field().send_keys(input_field.VALID_SHRUBS)
    shrubs_btn().click()
    shrubs_view_only().click()
    select_type().click()
    select_icon().click()
    close_btn().click()
    shrubs_btn().click()

def test_background():
    shrubs_background_color().click()
    shrubs_icon_color().click()
    shrubs_icon_type().click()
    save_style().click()
    save_header().click()
    new_branch().click()
    create_link().click()
    save_branch().click()
    assert list_branch_validation().text == validation_assert.ENTER_LIST_BRANCH
    list_branch_list().send_keys(input_field.VALID_SHRUBS)
    save_branch().click()

def test_link():
    add_link().click()
    link_input_field().send_keys(Keys.ENTER)
    time.sleep(2)
    link_save_btn().click()
    time.sleep(2)
    assert link_validation().text == validation_assert.ENTER_LINK
    link_input_field().send_keys(input_field.VALID_SHRUBS)
    time.sleep(2)
    link_save_btn().click()
    time.sleep(2)
    assert link_error().text == error.LINK_ERROR
    link_input_field().send_keys(Keys.CONTROL, "a")
    link_input_field().send_keys(Keys.DELETE)
    link_input_field().send_keys(input_field.LINK)
    link_input_field().send_keys(Keys.ENTER)
    time.sleep(5)
    link_save_btn().click()
    time.sleep(5)
    success_msg = link_save_msg(driver)
    assert success_msg.text == validation_assert.SAVE_SUCCESS_LINK
    time.sleep(2)
    back_link().click()
    time.sleep(2)
    link_save_btn().click()
    time.sleep(2)
    back_branch().click()
    time.sleep(2)

