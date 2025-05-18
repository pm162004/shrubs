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
password = config.CORRECT_PASSWORD
new_password = config.NEW_PASSWORD
wait = WebDriverWait(driver, 25)
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "body")))

def email_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "email")))

def password_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "password")))

def refresh_page():
    driver.refresh()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))  # Wait for the body to load after refresh

def display_myfiles_after_login():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//b[@class='text-active text-xs font-bold sidebar-menu'][normalize-space()='My Files']")))

def get_my_shrubs():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='My Shrubs']")))

def get_new_shrub():
    return wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".md-button-content")))

def shrub_title_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "shrub-name")))

def shrub_title_blank_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Shrub Title is required']")))

def permissions_field_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Permissions field is required']")))

def select_view_only_permissions():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='View Only']")))

def thumbnail_type_field_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Thumbnail type field is required']")))

def shrub_project_icon_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Shrub Project Icon']")))

def select_thumbnail_icon():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//h6[normalize-space()='alert-octagon']")))

def thumbnail_icon_cancel_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Cancel')]")))

def shrub_title_already_exists_validation():

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

def save_new_shrub_btn():
    # Wait until the overlay (spinner) is no longer visible
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "overlay-spinner"))  # Adjust ID if necessary
    )


    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "btn-save"))
    )
    return button


def background_color_dropdown():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Background']")))

def select_color_picker_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='center cursor-pointer flex items-center box-square-50']//img[@alt='thumbnail']")))

def select_color_from_color_picker():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Color:#BD10E0']")))

def save_style_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='md-button all-button-height br6 font-size-16 md-theme-default md-ripple-off md-primary mt1 mr1 h50']")))

def save_header_style_btn():
    # Wait until the overlay (spinner) is no longer visible
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "overlay-spinner"))  # Adjust ID if necessary
    )

    # Wait for the button to be clickable
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='md-button all-button-height br6 font-size-16 md-theme-default md-ripple-off md-primary mt1 mr1 h50']")))
    return button

def overlay_spinner():
    spinner =  WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.ID, "overlay-spinner"))  # Adjust ID if necessary
    )
    return spinner

def progress_spinner():
    spinner =   WebDriverWait(driver, 30).until(
        EC.invisibility_of_element_located((By.ID, "progress-spinner"))  # Wait for the spinner to disappear
    )
    return spinner

def get_new_branch():
    overlay_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-new-branch']")))

def create_links_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='Create Links']")))

def link_branch_title_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Branch Title']")))

def link_branch_title_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//small[@class='text-danger']")))

def save_new_branch_btn():
    overlay_spinner()
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='md-button all-button-height br6 md-theme-default md-ripple-off md-primary h50 w-100 font-size-16']//div[@class='md-ripple md-disabled']")))
    return button

def branch_add_link_btn():
    progress_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-upload-image']//div[@class='md-ripple md-disabled']")))

def add_link_input_field():
    progress_spinner()
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Link']")))

def blank_link_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='md-error']")))

def invalid_link_error():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='md-error']")))

def link_save_btn():
    progress_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='md-button all-button-height br6 md-theme-default md-ripple-off md-primary h50 w-100 font-size-16']")))

def back_link_btn():
    progress_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Back')]")))

def save_link_message(driver):
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

def back_branch_link_btn():
    progress_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='md-button all-button-height br6 md-theme-default md-ripple-off md-danger h50 w-100 font-size-16 mr1']//div[@class='md-ripple md-disabled']")))

def test_login():
    email_input_field().send_keys(email)
    password_input_field().send_keys(password)
    btn_login = wait.until(EC.element_to_be_clickable((By.NAME, "btn-signin")))
    btn_login.click()
    assert display_myfiles_after_login().text == validation_assert.MY_FILES

def test_my_shrubs():
    get_my_shrubs().click()
    time.sleep(10)
    get_new_shrub().click()

def test_blank_input_field_shrubs():
    save_new_shrub_btn().click()
    assert shrub_title_blank_validation().text == validation_assert.ENTER_SHRUBS_TITLE
    assert permissions_field_validation().text == validation_assert.ENTER_SHRUBS_PERMISSIONS
    assert thumbnail_type_field_validation().text == validation_assert.ENTER_SHRUBS_THUMBNAIL


def test_shrub_title_already_exists():
    refresh_page()
    shrub_title_input_field().send_keys(input_field.EXISTING_SHRUBS)
    select_view_only_permissions().click()
    shrub_project_icon_btn().click()
    select_thumbnail_icon().click()
    thumbnail_icon_cancel_btn().click()
    time.sleep(2)
    assert shrub_title_already_exists_validation()== validation_assert.EXISTS_SHRUBS_TITLE

def test_valid_shrubs():
    refresh_page()
    shrub_title_input_field().send_keys(input_field.VALID_SHRUBS)
    # save_new_shrub_btn().click()
    select_view_only_permissions().click()
    shrub_project_icon_btn().click()
    select_thumbnail_icon().click()
    thumbnail_icon_cancel_btn().click()
    save_new_shrub_btn().click()

def test_shrub_style():
    background_color_dropdown().click()
    select_color_picker_btn().click()
    select_color_from_color_picker().click()
    save_style_btn().click()
    save_header_style_btn().click()
   
def test_shrub_branch():
    get_new_branch().click()
    create_links_btn().click()
    save_new_branch_btn().click()
    assert link_branch_title_validation().text == validation_assert.ENTER_LIST_BRANCH
    link_branch_title_input_field().send_keys(input_field.VALID_SHRUBS)
    save_new_branch_btn().click()

def test_add_link():
    branch_add_link_btn().click()
    add_link_input_field().send_keys(Keys.ENTER)
    time.sleep(2)
    link_save_btn().click()
    time.sleep(2)
    assert blank_link_validation().text == validation_assert.ENTER_LINK
    add_link_input_field().send_keys(input_field.VALID_SHRUBS)
    time.sleep(2)
    link_save_btn().click()
    time.sleep(2)
    assert invalid_link_error().text == error.LINK_ERROR
    add_link_input_field().send_keys(Keys.CONTROL, "a")
    add_link_input_field().send_keys(Keys.DELETE)
    add_link_input_field().send_keys(input_field.LINK)
    add_link_input_field().send_keys(Keys.ENTER)
    time.sleep(5)
    link_save_btn().click()
    time.sleep(5)
    success_msg = save_link_message(driver)
    assert success_msg.text == validation_assert.SAVE_SUCCESS_LINK
    time.sleep(2)
    back_branch_link_btn().click()
    time.sleep(2)
    link_save_btn().click()
    time.sleep(2)
    back_link_btn().click()
    time.sleep(2)

