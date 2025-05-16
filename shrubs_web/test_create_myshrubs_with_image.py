import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from shrubs_setup.config import config
from constant import creds, validation_assert, input_field
# from Shrubs_Automation.shrubs_web.myShrubs import shrubs_ALREADY_EXIST_validation
from constant import error
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.service import Service as ChromeService

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
# Only run with the latest Chrome version
driver = webdriver.Chrome()
# driver.set_window_size(1920, 1080)
driver.maximize_window()
driver.get(config.WEB_URL)
email = config.CORRECT_EMAIL
password = config.PASSWORD
new_password = config.RESET_PASSWORD
wait = WebDriverWait(driver, 35)
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "body")))

def email_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "email")))

def login_password():
    return wait.until(EC.presence_of_element_located((By.NAME, "password")))

def refresh_page():
    driver.refresh()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))  # Wait for the body to load after refresh

def MyFilesPage():
    return wait.until(EC.presence_of_element_located(
        (By.XPATH, "//b[@class='text-active text-xs font-bold sidebar-menu'][normalize-space()='My Files']")))

def myShrubs():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='My Shrubs']")))

def new_shrub():
    overlay_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='md-button-content']")))

def shrubs_title_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "shrub-name")))

def shrubs_title_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Shrub Title is required']")))

def shrubs_background_color():
    overlay_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Background']")))

def shrubs_icon_color():
    return wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@class='center cursor-pointer flex items-center box-square-50']//img[@alt='thumbnail']")))

def shrubs_icon_type():
    progress_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Color:#BD10E0']")))

def overlay_spinner():
    btn = WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "overlay-spinner"))  # Adjust ID if necessary
    )
    return btn

def progress_spinner():
    btn = WebDriverWait(driver, 30).until(
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
    return wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Permissions field is required']")))


def shrubs_thumbnail_validation():
    return wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Thumbnail type field is required']")))


def new_branch():

    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-new-branch']")))


def shrubs_btn():
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "overlay-spinner"))  # Adjust ID if necessary
    )

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "btn-save"))
    )
    return button


def show_title():
    return wait.until(
        EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Do you want to show the title?']")))


def shrubs_view_only():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='View Only']")))


def hide_thumbnail():
    return wait.until(
        EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Do you want to show thumbnail?']")))


def select_type():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Thumbnail Image']")))

def select_thumbnail():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='cursor-pointer relative box-square-50 profile-bg br6']")))

image_paths = [
     "/home/web-h-028/PycharmProjects/TrainingAutomation/Shrubs_Automation/shrubs_web/image/image1.png"
    #   "C:/Users/Winner/PycharmProjects/TrainingAutomationLinux/Shrubs_Automation/shrubs_web/images/i1.jpg"
]


def upload_images():
    overlay_spinner()
    wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='white-action-icon font-size-16 font-weight-700']")))


    for image_path in image_paths:
        try:
            # Wait for the file input field to be clickable before interacting with it
            file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='upload-image']")))

            time.sleep(1)

        except Exception as e:
            print(f"Error uploading image {image_path}: {e}")




def keep_both():
    return wait.until(EC.element_to_be_clickable((By.XPATH,"//label[normalize-space()='Keep both files']")))
def ok_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='button-base demo w-full theme-solid']")))
def next_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Next')]")))
def save_media():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button']//div[@class='md-button-content'][normalize-space()='Save']")))

def close_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Cancel')]")))

def save_style():
    overlay_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH,
                                                  "(//button[contains(@class, 'md-button') and .//div[normalize-space()='Save']])[2]")))

def save_shrubs():
    overlay_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='md-button all-button-height br6 font-size-16 md-theme-default md-ripple-off md-primary h50']//div[@class='md-button-content'][normalize-space()='Save']")))

def save_header():
    # Wait until the overlay (spinner) is no longer visible
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "overlay-spinner"))  # Adjust ID if necessary
    )

    # Wait for the button to be clickable
    button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='md-button all-button-height br6 font-size-16 md-theme-default md-ripple-off md-primary mt1 mr1 h50']")))
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
    return wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='md-button all-button-height br6 md-theme-default md-ripple-off md-primary h50 w-100 font-size-16']")))


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
    return wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='md-button all-button-height br6 md-theme-default md-ripple-off md-danger h50 w-100 font-size-16 mr1']//div[@class='md-ripple md-disabled']")))

def save_as_template():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Save As Template')]")))

def add_style_validation():
    overlay_spinner()
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Template Name is required']")))

def add_style_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "(//input[contains(@id, 'md-input')])[5]")))

def remove_background():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='flex cursor-pointer box-square-50']//img[@alt='thumbnail']")))

def test_login():
    email_input_field().send_keys(email)
    login_password().send_keys(password)
    btn_login = wait.until(EC.element_to_be_clickable((By.NAME, "btn-signin")))
    btn_login.click()
    time.sleep(5)
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
    refresh_page()  # Ensure this function is implemented correctly
    shrubs_title_input_field().send_keys(input_field.EXISTING_SHRUBS)
    shrubs_view_only().click()
    select_type().click()
    upload_images()
    keep_both().click()
    ok_btn().click()
    next_btn().click()
    save_media().click()
    # wait.until(EC.presence_of_element_located((By.XPATH, "//element-that-indicates-completion")))
    save_shrubs().click()
    assert shrubs_already_exits_validation() == validation_assert.EXISTS_SHRUBS_TITLE

def test_valid_shrubs():
    refresh_page()
    shrubs_title_input_field().send_keys(input_field.VALID_SHRUBS)
    shrubs_btn().click()
    shrubs_view_only().click()
    select_type().click()
    upload_images()
    keep_both().click()
    ok_btn().click()
    next_btn().click()
    save_media().click()
    shrubs_btn().click()
    time.sleep(10)


def test_background():
    shrubs_background_color().click()
    shrubs_icon_color().click()
    shrubs_icon_type().click()
    select_thumbnail().click()
    upload_images()
    keep_both().click()
    ok_btn().click()
    next_btn().click()
    save_media().click()
    time.sleep(2)
    remove_background().click()
    save_as_template().click()
    add_style_input_field().send_keys(Keys.ENTER)
    time.sleep(5)
    assert add_style_validation().text == validation_assert.ENTER_TEMPLATE_NAME
    add_style_input_field().send_keys(input_field.VALID_SHRUBS)
    add_style_input_field().send_keys(Keys.ENTER)
    time.sleep(5)
    save_style().click()
    save_header().click()
    time.sleep(5)
    new_branch().click()
    create_link().click()
    time.sleep(5)
    save_branch().click()
    time.sleep(5)
    assert list_branch_validation().text == validation_assert.ENTER_LIST_BRANCH
    list_branch_list().send_keys(input_field.VALID_SHRUBS)
    time.sleep(5)
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

