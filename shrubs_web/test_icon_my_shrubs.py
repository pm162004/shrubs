import random
import time
from selenium.common import TimeoutException
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
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument("--headless")  # Optional for headless mode

prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False
}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()
logger.info("Launching browser and navigating to URL")
driver.get(config.WEB_URL)

email = config.CORRECT_EMAIL
password = config.CORRECT_PASSWORD
new_password = config.RESET_PASSWORD
wait = WebDriverWait(driver, 25)
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "body")))


# Element Getters

def email_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "email")))


def password_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "password")))


def refresh_page():
    logger.info("Refreshing the page")
    driver.delete_all_cookies()
    driver.execute_script("window.localStorage.clear(); window.sessionStorage.clear();")
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    return driver.refresh()


def display_myfiles_after_login():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//b[normalize-space()='My Files']")))


def get_my_shrubs():
    time.sleep(2)
    return wait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='My Shrubs']")))


def get_new_shrub():
    time.sleep(5)
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='md-button-content' and text()='New Shrub']")))


def shrub_title_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='shrub-name']")))


def shrub_title_blank_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Shrub Title is required']")))


def permissions_field_validation():
    return wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Permissions field is required']")))


def select_view_only_permissions():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='View Only']")))


def thumbnail_type_field_validation():
    return wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Thumbnail type field is required']")))


def shrub_project_icon_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Shrub Project Icon']")))


def select_thumbnail_icon():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//h6[normalize-space()='alert-octagon']")))


def thumbnail_icon_cancel_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Cancel')]")))


def shrub_title_already_exists_validation():
    logger.info("Checking if duplicate shrub title validation appears")
    try:
        driver.find_element(By.NAME, "btn-save").click()
        error_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[normalize-space()='Project already exist with the given slug']"))
        )
        logger.info("Error message: " + error_message.text)
        return error_message.text
    except TimeoutException:
        logger.warning("No error message found within timeout.")
        try:
            alert = driver.switch_to.alert
            msg = alert.text
            logger.warning("Alert found: " + msg)
            return msg
        except:
            logger.warning("No alert found, retrying for modal.")
            try:
                error_message = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//span[normalize-space()='Project already exist with the given slug']"))
                )
                logger.info("Modal error message: " + error_message.text)
                return error_message.text
            except TimeoutException:
                logger.warning("No modal or message found.")
                return None


def save_new_shrub_btn():
    logger.info("Waiting for save shrub button to be clickable")
    overlay_spinner()
    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btn-save")))


def background_color_dropdown():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Background']")))


def select_color_picker_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='thumbnail']")))


def select_color_from_color_picker():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Color:#BD10E0']")))


def save_style_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Save')]")))


def save_header_style_btn():
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "overlay-spinner")))
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Save')]")))


def overlay_spinner():
    return WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "overlay-spinner")))


def progress_spinner():
    return WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.ID, "progress-spinner")))


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
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Save')]")))


def branch_add_link_btn():
    progress_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-upload-image']")))


def add_link_input_field():
    progress_spinner()
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Link']")))


def blank_link_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='md-error']")))


def invalid_link_error():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='md-error']")))


def link_save_btn():
    progress_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Save')]")))


def back_link_btn():
    progress_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Back')]")))


def save_link_message(driver):
    try:
        success_message = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='text-success']"))
        )
        return success_message
    except TimeoutException:
        logger.warning("Timeout: Success message not found")
        return None


def back_branch_link_btn():
    progress_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Back')]")))


def select_random_icon():

    icons = wait.until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, "div.icon-hover")
    ))

    if not icons:
        raise Exception("No icons found in the modal.")

    random_icon = random.choice(icons)
    random_icon.click()
# ============================== TEST CASES ==============================
class TestMyShrubsIcon:

    def test_login(self):
        logger.info("Running test_login")
        email_input_field().send_keys(email)
        password_input_field().send_keys(password)
        wait.until(EC.element_to_be_clickable((By.NAME, "btn-signin"))).click()
        assert display_myfiles_after_login().text == validation_assert.MY_FILES
        logger.info("Login successful")


def test_my_shrubs():
    logger.info("Navigating to My Shrubs")
    get_my_shrubs().click()
    get_new_shrub().click()
    logger.info("Clicked on new shrub button")


def test_blank_input_field_shrubs():
    logger.info("Testing blank shrub validations")
    save_new_shrub_btn().click()
    assert shrub_title_blank_validation().text == validation_assert.ENTER_SHRUBS_TITLE
    assert permissions_field_validation().text == validation_assert.ENTER_SHRUBS_PERMISSIONS
    assert thumbnail_type_field_validation().text == validation_assert.ENTER_SHRUBS_THUMBNAIL
    logger.info("Blank field validations passed")


def test_shrub_title_already_exists():
    logger.info("Testing existing shrub title")
    shrub_title_input_field().send_keys(input_field.EXISTING_SHRUBS)
    select_view_only_permissions().click()
    shrub_project_icon_btn().click()
    select_thumbnail_icon().click()
    thumbnail_icon_cancel_btn().click()
    time.sleep(2)
    assert shrub_title_already_exists_validation() == validation_assert.EXISTS_SHRUBS_TITLE
    logger.info("Duplicate title validation passed")


# def test_valid_shrubs():
#     logger.info("Testing valid shrub creation")
#     refresh_page()
#     shrub_title_input_field().send_keys(input_field.VALID_SHRUBS)
#     select_view_only_permissions().click()
#     shrub_project_icon_btn().click()
#     select_random_icon()
#     thumbnail_icon_cancel_btn().click()
#     save_new_shrub_btn().click()
#     logger.info("Valid shrub created")
#
#
# def test_shrub_style():
#     logger.info("Testing shrub styling")
#     background_color_dropdown().click()
#     select_color_picker_btn().click()
#     select_color_from_color_picker().click()
#     save_style_btn().click()
#     save_header_style_btn().click()
#     logger.info("Shrub styling applied successfully")
#
#
# def test_shrub_branch():
#     logger.info("Testing branch creation")
#     get_new_branch().click()
#     create_links_btn().click()
#     save_new_branch_btn().click()
#     assert link_branch_title_validation().text == validation_assert.ENTER_LIST_BRANCH
#     link_branch_title_input_field().send_keys(input_field.VALID_SHRUBS)
#     save_new_branch_btn().click()
#     logger.info("Branch created successfully")
#
#
# def test_add_link():
#     logger.info("Testing add link to branch")
#     branch_add_link_btn().click()
#     add_link_input_field().send_keys(Keys.ENTER)
#     time.sleep(1)
#     link_save_btn().click()
#     assert blank_link_validation().text == validation_assert.ENTER_LINK
#     add_link_input_field().send_keys(input_field.VALID_SHRUBS)
#     link_save_btn().click()
#     assert invalid_link_error().text == error.LINK_ERROR
#     add_link_input_field().send_keys(Keys.CONTROL, "a")
#     add_link_input_field().send_keys(Keys.DELETE)
#     add_link_input_field().send_keys(input_field.LINK)
#     add_link_input_field().send_keys(Keys.ENTER)
#     time.sleep(2)
#     link_save_btn().click()
#     success_msg = save_link_message(driver)
#     assert success_msg.text == validation_assert.SAVE_SUCCESS_LINK
#     back_branch_link_btn().click()
#     link_save_btn().click()
#     back_link_btn().click()
#     logger.info("Link added successfully")
