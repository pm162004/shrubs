import random
import time,os,datetime
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from shrubs_setup.config import config
from constant import validation_assert, input_field, error
from log_config import setup_logger

logger = setup_logger()

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=chrome_options)
chrome_options.add_argument('--headless')
driver.maximize_window()

email = config.CORRECT_EMAIL
password = config.CORRECT_PASSWORD

logger.info("Launching login page")
driver.get(config.WEB_URL)
time.sleep(3)

wait = WebDriverWait(driver, 25)



def display_myfiles_after_login():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//b[normalize-space()='My Files']")))

def email_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "email")))

def password_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "password")))

def login_button():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-signin']")))


def refresh_page():
    logger.info("Refreshing page")
    return driver.refresh()

def password_mask_button():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//*[name()='path' and contains(@d,'M12 7c2.76')]")))

def check_logout_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Logout' and contains(@class, 'user-menu')]")))

def quit_browser():
    time.sleep(1)
    driver.quit()

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


def get_my_shrubs():
    time.sleep(2)
    return wait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='My Shrubs']")))


def get_new_shrub():
    time.sleep(5)
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='md-button-content' and text()='New Shrub']")))

def shrub_title_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='shrub-name']")))

def shrub_sub_header_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='shrub-sub-header']")))

def shrub_description_textbox():
    return wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(@class, 'ck-editor__editable') and @contenteditable='true'])[1]")))

def select_view_only_permissions():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='View Only']")))

def select_allow_resharing_permissions():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Allow Resharing']")))

def select_download_save_permissions():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Download and save to Shrubdrive']")))


def shrub_project_icon_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Shrub Project Icon']")))

def select_thumbnail_image_btn():
    overlay_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Thumbnail Image']")))


def select_thumbnail_icon():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//h6[normalize-space()='alert-octagon']")))

def thumbnail_icon_cancel_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Cancel')]")))

def save_new_shrub_btn():
    logger.info("Waiting for save shrub button to be clickable")
    overlay_spinner()
    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btn-save")))

def next_image_btn():
    overlay_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//div[normalize-space(text())='Next']]")))

def save_crop_image_btn():
    overlay_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and .//div[@class='md-button-content' and normalize-space()='Save']]")))

def upload_image_my_files_btn():
    return wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[contains(@class, 'sidebar-card') and .//p[normalize-space(text())='My Files']]//a[contains(@class, 'menu-list-item')]")))

def upload_image_my_shrubs_btn():
    return wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[contains(@class, 'sidebar-card') and .//p[normalize-space(text())='My Shrubs']]//a[contains(@class, 'menu-list-item')]")))

def select_thumbnail_folder():
    return wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[span[text()[normalize-space()='thumbnail']]]")))



def select_random_image(driver):
    try:
        images = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img.thumbnail-height"))
        )
        selected_image = random.choice(images)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", selected_image)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img.thumbnail-height")))
        ActionChains(driver).move_to_element(selected_image).click().perform()
    except Exception as e:
        raise Exception(f"Failed to select random image: {str(e)}")

def zoomin_image_btn():
    overlay_spinner()
    zoom_in_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'icons')]//img[contains(@src, 'zoom-in')]"))
    )

    return zoom_in_button.click()

def zoom_out_image_btn():
    overlay_spinner()
    zoom_out_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'icons')]//img[contains(@src, 'zoom-out')]"))
    )
    return zoom_out_button.click()

def overlay_spinner():
    return WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "overlay-spinner")))


def select_random_icon():

    icons = wait.until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, "div.icon-hover")
    ))

    if not icons:
        raise Exception("No icons found in the modal.")

    random_icon = random.choice(icons)
    random_icon.click()


# def upload_file(file_path):
#     abs_path = os.path.abspath(file_path)  # Convert to absolute path
#     file_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))
#     file_input.send_keys(abs_path)


def upload_random_image(relative_folder):
    folder_path = os.path.abspath(relative_folder)
    images = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if not images:
        raise Exception(f"No images found in {folder_path}")

    file_path = os.path.join(folder_path, random.choice(images))


    file_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))
    file_input.send_keys(file_path)

    try:
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//h5[normalize-space()='File already exists!']"))
        )
        ok_button = driver.find_element(By.XPATH, "//button[normalize-space()='Ok']")
        ok_button.click()
    except:
        pass

def select_random_my_shrub():
    try:
        shrub_cards = wait.until(EC.presence_of_all_elements_located((
            By.CSS_SELECTOR,
            "div.cursor-pointer.flex.flex-wrap.items-center.justify-center.rounded-lg"
        )))

        selected_shrub = random.choice(shrub_cards)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", selected_shrub)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.cursor-pointer.flex.flex-wrap.items-center.justify-center.rounded-lg")))
        selected_shrub.click()
    except Exception as e:
        print(f"[ERROR] Failed to select shrub: {e}")
        driver.save_screenshot("error_select_shrub.png")
        raise




# ============================== TEST CASES ==============================

class TestPositiveFlow:


    def test_valid_login_flow(self):
        logger.info("Running test: Valid login flow")
        refresh_page()
        email_input_field().send_keys(config.CORRECT_EMAIL)
        password_input_field().send_keys(config.CORRECT_PASSWORD)
        password_mask_button().click()
        logger.debug("Clicked password visibility toggle")
        login_button().click()
        assert display_myfiles_after_login().text == validation_assert.MY_FILES
        logger.info("Valid login passed, My Files is visible")


def test_my_shrubs():
    logger.info("Navigating to My Shrubs")
    get_my_shrubs().click()
    wait.until(EC.invisibility_of_element_located((By.ID, "overlay-spinner")))
    get_new_shrub().click()
    logger.info("Clicked on new shrub button")

def test_valid_shrubs():
    logger.info("Testing valid shrub creation")
    shrub_title_input_field().send_keys(input_field.VALID_SHRUBS)
    shrub_sub_header_input_field().send_keys(input_field.SUB_HEADER_SHRUBS)
    shrub_description_textbox().send_keys(input_field.SHRUBS_DESCRIPTION)
    select_view_only_permissions().click()
    select_view_only_permissions().click()
    select_allow_resharing_permissions().click()
    select_download_save_permissions().click()
    shrub_project_icon_btn().click()
    select_random_icon()
    thumbnail_icon_cancel_btn().click()


def test_valid_my_computer_image_flow():
    select_thumbnail_image_btn().click()
    upload_random_image("image")
    next_image_btn().click()
    zoomin_image_btn()
    zoom_out_image_btn()
    save_crop_image_btn().click()

def test_valid_my_files_image_flow():
    overlay_spinner()
    select_thumbnail_image_btn().click()
    upload_image_my_files_btn().click()
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "img.thumbnail-height"))
    # )
    select_random_image(driver)
    next_image_btn().click()
    zoomin_image_btn()
    zoom_out_image_btn()
    save_crop_image_btn().click()
    logger.info("Valid shrub created")

def test_valid_my_shrubs_image_flow():
    select_thumbnail_image_btn().click()
    upload_image_my_shrubs_btn().click()
    select_random_my_shrub()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='thumbnail']"))
    )

    select_thumbnail_folder().click()
    next_image_btn().click()
    zoomin_image_btn()
    zoom_out_image_btn()
    save_crop_image_btn().click()
    logger.info("Valid shrub created")
# save_new_shrub_btn().click()

# def test_shrub_style():
#     logger.info("Testing shrub styling")
#     background_color_dropdown().click()
#     select_color_picker_btn().click()
#     select_color_from_color_picker().click()
#     save_style_btn().click()
#     save_header_style_btn().click()
#     logger.info("Shrub styling applied successfully")
#