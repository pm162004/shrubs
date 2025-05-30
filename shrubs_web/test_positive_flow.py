import random
import time, os, datetime
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from shrubs_setup.config import config
from constant import validation_assert, input_field, error
from log_config import setup_logger
from selenium.webdriver.common.action_chains import ActionChains

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
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))


def display_myfiles_after_login():
    wait.until(EC.visibility_of_element_located((By.XPATH,
                                                 "//a[@href='/platform/files' and contains(@class, 'nav-item') and contains(@class, 'active') and contains(., 'My Files')]")))

    return wait.until(EC.presence_of_element_located((By.XPATH,
                                                      "//a[@href='/platform/files' and contains(@class, 'nav-item') and contains(@class, 'active') and contains(., 'My Files')]")))


def email_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "email")))


def password_input_field():
    return wait.until(EC.presence_of_element_located((By.NAME, "password")))


def login_button():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-signin']")))


def refresh_page():
    logger.info("Refreshing page")
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
    return driver.refresh()


def password_mask_button():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//*[name()='path' and contains(@d,'M12 7c2.76')]")))


def check_logout_btn():
    return wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Logout' and contains(@class, 'user-menu')]")))


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
    return wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='md-button-content' and text()='New Shrub']")))


def shrub_title_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='shrub-name']")))


def shrub_sub_header_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='shrub-sub-header']")))


def shrub_description_textbox():
    return wait.until(EC.presence_of_element_located(
        (By.XPATH, "(//div[contains(@class, 'ck-editor__editable') and @contenteditable='true'])[1]")))


def select_view_only_permissions():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='View Only']")))


def select_allow_resharing_permissions():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Allow Resharing']")))


def select_download_save_permissions():
    return wait.until(
        EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Download and save to Shrubdrive']")))


def shrub_project_icon_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Shrub Project Icon']")))


def select_thumbnail_image_btn():
    overlay_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Thumbnail Image']")))


def select_thumbnail_icon():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//h6[normalize-space()='alert-octagon']")))


def thumbnail_icon_cancel_btn():
    overlay_spinner()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Cancel')]")))
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Cancel')]")))


def save_new_shrub_btn():
    logger.info("Waiting for save shrub button to be clickable")
    overlay_spinner()
    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btn-save")))


def next_image_btn():
    overlay_spinner()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[.//div[normalize-space(text())='Next']]")))
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//div[normalize-space(text())='Next']]")))


def save_crop_image_btn():
    overlay_spinner()
    return wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='button' and .//div[@class='md-button-content' and normalize-space()='Save']]")))


def upload_image_my_files_btn():
    return wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         "//div[contains(@class, 'sidebar-card') and .//p[normalize-space(text())='My Files']]//a[contains(@class, 'menu-list-item')]")))


def upload_image_my_shrubs_btn():
    return wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         "//div[contains(@class, 'sidebar-card') and .//p[normalize-space(text())='My Shrubs']]//a[contains(@class, 'menu-list-item')]")))


def select_thumbnail_folder():
    try:
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[span[text()[normalize-space()='thumbnail']]]")
        ))

        # Scroll the element into view
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

        # Perform double-click using ActionChains
        ActionChains(driver).move_to_element(element).double_click().perform()
        print("[INFO] Double-clicked on 'thumbnail' folder.")

    except Exception as e:
        print(f"[ERROR] Could not double-click thumbnail folder: {e}")
        driver.save_screenshot("error_thumbnail_doubleclick.png")
        raise


def select_random_image(driver):
    try:
        try:
            logger.info("Waiting for overlay to disappear or become invisible...")
            WebDriverWait(driver, 20).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "md-overlay"))
            )
        except TimeoutException:
            logger.warning("Overlay did not disappear – continuing anyway")

        logger.info("Waiting for images to be visible...")
        images = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img.object-cover"))
        )

        logger.info(f"Found {len(images)} images")

        selected_image = random.choice(images)
        driver.execute_script("window.scrollTo(0, arguments[0].getBoundingClientRect().top + window.scrollY - 100);",
                              selected_image)

        # Use JavaScript click as fallback if ActionChains fails
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(selected_image)
            )
            ActionChains(driver).move_to_element(selected_image).click().perform()
        except Exception as e:
            logger.warning(f"ActionChains click failed: {e} — trying JS click")
            driver.execute_script("arguments[0].click();", selected_image)

        logger.info("Random image selected successfully")

    except Exception as e:
        logger.error(f"Failed to select random image: {e}")
        driver.save_screenshot("screenshots/select_random_image_error.png")
        raise


def zoomin_image_btn():
    overlay_spinner()
    zoom_in_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'icons')]//img[contains(@src, 'zoom-in')]"))
    )

    return zoom_in_button.click()


def ok_btn():
    overlay_spinner()
    ok = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='content' and normalize-space()='Ok']"))
    )

    return ok.click()


def zoom_out_image_btn():
    overlay_spinner()
    zoom_out_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'icons')]//img[contains(@src, 'zoom-out')]"))
    )
    return zoom_out_button.click()


def overlay_spinner():
    return WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "overlay-spinner")))


def select_random_font(driver):
    wait = WebDriverWait(driver, 10)

    # Open the font dropdown first (click the combobox area)
    combobox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.multiselect")))
    combobox.click()

    # Wait for all visible font options to load
    font_options = wait.until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, "li.multiselect__element:not([style*='display: none']) > span.multiselect__option")
    ))

    if not font_options:
        raise Exception("No fonts found in the dropdown.")

    # Randomly select and click a font
    selected_font = random.choice(font_options)
    font_name = selected_font.text.strip()
    selected_font.click()

    print(f"Selected random font: {font_name}")
    return font_name


def select_random_icon():
    icons = wait.until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, "div.icon-hover")
    ))

    if not icons:
        raise Exception("No icons found in the modal.")

    random_icon = random.choice(icons)
    random_icon.click()


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


def select_random_my_shrub(driver, wait):
    try:
        shrub_cards = wait.until(EC.presence_of_all_elements_located((
            By.CSS_SELECTOR,
            "div.cursor-pointer.flex.flex-wrap.items-center.justify-center.rounded-lg"
        )))

        selected_shrub = random.choice(shrub_cards)

        # Scroll into view using JavaScript
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", selected_shrub)

        # Wait for the element to be clickable
        wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            "div.cursor-pointer.flex.flex-wrap.items-center.justify-center.rounded-lg"
        )))

        # Perform double-click using ActionChains
        actions = ActionChains(driver)
        actions.move_to_element(selected_shrub).double_click().perform()

        print("[INFO] Random shrub double-clicked.")

        # Handle "File already exists!" popup if it appears
        handle_file_exists_popup(driver)

    except Exception as e:
        print(f"[ERROR] Failed to select shrub: {e}")
        driver.save_screenshot("error_select_shrub.png")
        raise


def handle_file_exists_popup(driver):
    try:
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//h5[normalize-space()='File upload option']"))
        )
        print("[INFO] 'File already exists!' popup detected.")

        ok_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Ok']"))
        )
        ok_button.click()
        print("[INFO] Clicked on 'Ok' button.")
    except Exception:
        print("[INFO] 'File already exists!' popup not found — skipping.")


def background_color_dropdown(driver, timeout=20):
    overlay_spinner()  # Assuming this handles any overlay spinner present before interaction

    try:
        # Wait until the 'Background' element is visible on the page
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Background']")))
    except TimeoutException:
        # On timeout, save screenshot and print page source for debugging
        driver.save_screenshot("timeout_background.png")
        print(driver.page_source)
        raise  # Reraise exception so caller can handle it if needed

    # Once visible, wait until the element is clickable and return it
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Background']")))


def header_dropdown():
    overlay_spinner()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Header']")))
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Header']")))


def header_background_dropdown():
    overlay_spinner()
    wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[normalize-space()='Background'])[1]")))
    return wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[normalize-space()='Background'])[1]")))


def shrub_title_dropdown():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Shrub Title']")))


def shrub_header_dropdown():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[normalize-space()='Sub Header'])[2]")))


def font_color_dropdown():
    return wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//span[@class='md-list-item-text' and text()='Font Color'])[1]")))


def sub_header_font_color_dropdown():
    return wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//span[@class='md-list-item-text' and text()='Font Color'])[2]")))


def description_font_color_dropdown():
    return wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//span[@class='md-list-item-text' and text()='Font Color'])[3]")))


def select_font_style_dropdown():
    return wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//span[@class='md-list-item-text' and text()='Select your font'])[1]")))


def select_sub_header_font_style_dropdown():
    return wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//span[@class='md-list-item-text' and text()='Select your font'])[2]")))


def select_description_font_style_dropdown():
    return wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//span[@class='md-list-item-text' and text()='Select your font'])[3]")))


def select_font_weight_dropdown():
    return wait.until(EC.element_to_be_clickable(
        (By.XPATH, "(//span[@class='md-list-item-text' and text()='Select your font weight'])[1]")))


def select_sub_header_font_weight_dropdown():
    return wait.until(EC.element_to_be_clickable(
        (By.XPATH, "(//span[@class='md-list-item-text' and text()='Select your font weight'])[2]")))


def select_description_font_weight_dropdown():
    return wait.until(EC.element_to_be_clickable(
        (By.XPATH, "(//span[@class='md-list-item-text' and text()='Select your font weight'])[3]")))


def select_font_size_dropdown():
    return wait.until(EC.element_to_be_clickable(
        (By.XPATH, "(//span[@class='md-list-item-text' and text()='Select your font size'])[1]")))


def select_sub_header_font_size_dropdown():
    return wait.until(EC.element_to_be_clickable(
        (By.XPATH, "(//span[@class='md-list-item-text' and text()='Select your font size'])[2]")))


def select_description_font_size_dropdown():
    return wait.until(EC.element_to_be_clickable(
        (By.XPATH, "(//span[@class='md-list-item-text' and text()='Select your font size'])[2]")))


def select_random_alignment(driver):
    wait = WebDriverWait(driver, 10)

    # Locate all alignment buttons (left, center, right)
    alignment_buttons = wait.until(EC.presence_of_all_elements_located((
        By.XPATH,
        "//h5[contains(text(),'Horizontal font alignment')]/following::div[contains(@class,'justify-around')]/span"
    )))

    # Pick a random button and click it
    random_button = random.choice(alignment_buttons)
    alignment_name = random_button.find_element(By.TAG_NAME, "i").text
    random_button.click()

    print(f"Random alignment selected: {alignment_name}")


def select_font_alignment_dropdown():
    return wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//span[@class='md-list-item-text' and text()='Font Alignment'])[1]")))


def select_sub_header_font_alignment_dropdown():
    return wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//span[@class='md-list-item-text' and text()='Font Alignment'])[2]")))


def select_description_font_alignment_dropdown():
    return wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//span[@class='md-list-item-text' and text()='Font Alignment'])[3]")))


def select_bold_font_weight(driver):
    wait = WebDriverWait(driver, 10)

    # Click to open the 'Select your font weight' dropdown
    font_weight_dropdown = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//label[contains(text(), 'Select your font weight')]/following-sibling::div"
    )))
    font_weight_dropdown.click()

    # Wait for the 'Bold' option to be visible and click it
    bold_option = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//span[@class='multiselect__option' and normalize-space(text())='Bold']"
    )))
    bold_option.click()

    print("Bold font weight selected.")


def select_random_font_size(driver):
    wait = WebDriverWait(driver, 10)

    # Open the font size dropdown
    font_size_dropdown = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//label[contains(text(), 'Select your font size')]/following-sibling::div"
    )))
    font_size_dropdown.click()

    # Get all font size options
    font_size_options = wait.until(EC.presence_of_all_elements_located((
        By.XPATH, "//span[@class='multiselect__option']"
    )))

    # Pick a random option
    random_option = random.choice(font_size_options)
    print(f"Randomly selected font size: {random_option.text}")

    # Click the selected option
    random_option.click()


def shrub_description_dropdown():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Shrub Description']")))


def select_color_picker_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='thumbnail']")))


def select_header_color_picker_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "(//img[contains(@src, 'color-picker')])[1]")))


def select_background_image_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//img[contains(@src, 'background-image')]")))


def select_header_background_image_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "(//img[contains(@src, 'background-image')])[1]")))


def select_no_background_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//img[contains(@src, 'no-background')]/parent::div")))


def select_no_header_background_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "(//img[contains(@src, 'no-background')]/parent::div)[1]")))


def select_color_from_color_picker():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Color:#BD10E0']")))


def select_random_preset_color(driver, wait):
    try:
        # Wait for all preset color elements
        preset_colors = wait.until(EC.presence_of_all_elements_located((
            By.XPATH, "//div[contains(@class, 'vc-sketch-presets-color')]"
        )))

        # Choose one randomly
        random_color = random.choice(preset_colors)

        # Scroll into view and click using ActionChains
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", random_color)
        ActionChains(driver).move_to_element(random_color).click().perform()

        # Optional: Print the color being selected
        print(f"[INFO] Selected preset color: {random_color.get_attribute('aria-label')}")

    except Exception as e:
        print(f"[ERROR] Failed to select preset color: {e}")
        driver.save_screenshot("error_preset_color.png")
        raise


def save_header_style_btn():
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "overlay-spinner")))
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Save')]")))


def save_style_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Save')]")))


# ============================== TEST CASES ==============================

class TestPositiveFlow:

    def test_valid_login_flow(self):
        logger.info("Running test: Valid login flow")
        refresh_page()
        logger.info("Refreshing page completed")
        logger.info("Entering email")
        email_input_field().send_keys(config.CORRECT_EMAIL)
        logger.info("Entering password")
        password_input_field().send_keys(config.CORRECT_PASSWORD)
        logger.info("Clicking password visibility toggle")
        password_mask_button().click()
        logger.info("Clicking login button")
        login_button().click()
        my_files_text = display_myfiles_after_login().text
        logger.info(f"Login complete, checking for 'My Files' text: Found '{my_files_text}'")
        assert my_files_text == validation_assert.MY_FILES
        logger.info("Valid login passed, 'My Files' is visible")

    def test_my_shrubs(self):
        logger.info("Navigating to 'My Shrubs'")
        get_my_shrubs().click()
        wait.until(EC.invisibility_of_element_located((By.ID, "overlay-spinner")))
        logger.info("Overlay spinner disappeared after navigating to 'My Shrubs'")
        get_new_shrub().click()
        logger.info("Clicked 'New Shrub' button")

    def test_valid_shrubs(self):
        logger.info("Testing valid shrub creation")
        shrub_title_input_field().send_keys(input_field.VALID_SHRUBS)
        logger.info(f"Entered shrub title: {input_field.VALID_SHRUBS}")
        shrub_sub_header_input_field().send_keys(input_field.SUB_HEADER_SHRUBS)
        logger.info(f"Entered shrub sub-header: {input_field.SUB_HEADER_SHRUBS}")
        shrub_description_textbox().send_keys(input_field.SHRUBS_DESCRIPTION)
        logger.info(f"Entered shrub description")
        select_view_only_permissions().click()
        logger.info("Selected 'View Only' permission (first click)")
        select_view_only_permissions().click()
        logger.info("Selected 'View Only' permission (second click)")
        select_allow_resharing_permissions().click()
        logger.info("Selected 'Allow Resharing' permission")
        select_download_save_permissions().click()
        logger.info("Selected 'Download and save to Shrubdrive' permission")
        shrub_project_icon_btn().click()
        logger.info("Clicked 'Shrub Project Icon' option")
        select_random_icon()
        logger.info("Selected random icon")
        thumbnail_icon_cancel_btn().click()
        logger.info("Cancelled thumbnail icon selection")

    def test_valid_my_computer_image_flow(self):
        logger.info("Starting 'My Computer' image upload and crop flow")
        select_thumbnail_image_btn().click()
        logger.info("Clicked 'Thumbnail Image' button")
        upload_random_image("image")
        logger.info("Uploaded random image from 'image' folder")
        next_image_btn().click()
        logger.info("Clicked 'Next' button after image upload")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        logger.info("Clicked 'Save' button to save cropped image")

    def test_valid_my_files_image_flow(self):
        logger.info("Starting 'My Files' image upload and crop flow")
        overlay_spinner()
        logger.info("Overlay spinner disappeared")
        select_thumbnail_image_btn().click()
        logger.info("Clicked 'Thumbnail Image' button")
        upload_image_my_files_btn().click()
        logger.info("Clicked 'My Files' folder upload button")
        logger.info("Thumbnail images loaded in 'My Files' folder")
        select_random_image(driver)
        logger.info("Selected a random image from 'My Files'")
        next_image_btn().click()
        logger.info("Clicked 'Next' button")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        logger.info("Clicked 'Save' button for cropped image")
        logger.info("Valid shrub created in 'My Files' image flow")

    def test_valid_my_shrubs_image_flow(self):
        logger.info("Starting 'My Shrubs' image upload and crop flow")
        select_thumbnail_image_btn().click()
        logger.info("Clicked 'Thumbnail Image' button")
        upload_image_my_shrubs_btn().click()
        logger.info("Clicked 'My Shrubs' folder upload button")
        select_random_my_shrub(driver, wait)
        logger.info("Selected a random shrub from 'My Shrubs'")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='thumbnail']")))
            logger.info("Thumbnail span appeared after shrub selection")
        except Exception as e:
            logger.warning(f"Thumbnail label not found: {e}")
            driver.save_screenshot("error_thumbnail_label_missing.png")
            raise
        logger.info("Thumbnail span appeared after shrub selection")
        select_thumbnail_folder()
        select_random_image(driver)
        logger.info("Clicked on thumbnail folder")
        next_image_btn().click()
        logger.info("Clicked 'Next' button")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        logger.info("Clicked 'Save' button to save cropped image")
        logger.info("Valid shrub created in 'My Shrubs' image flow")
        try:
            ok_btn()
        except TimeoutException:
            print("[INFO] OK button not found or not clickable — skipping.")

        save_new_shrub_btn().click()
        logger.info("Clicked 'Save New Shrub' button to finalize creation")

    def test_shrub_style_background(self):

        logger.info("Testing shrub styling")
    background_color_dropdown(driver).click()
    select_background_image_btn().click()
    upload_random_image("image")
    logger.info("Uploaded random image from 'image' folder")
    next_image_btn().click()
    logger.info("Clicked 'Next' button after image upload")
    zoomin_image_btn()
    logger.info("Zoomed in image")
    zoom_out_image_btn()
    logger.info("Zoomed out image")
    save_crop_image_btn().click()
    save_screenshot("Background_image")
    time.sleep(1)
    select_no_background_btn().click()
    select_color_picker_btn().click()
    select_random_preset_color(driver, wait)
    save_screenshot("Color_pick")
    time.sleep(1)
    select_no_background_btn().click()
    background_color_dropdown(driver).click()


def test_shrub_style_shrub_title():
    shrub_title_dropdown().click()
    select_random_preset_color(driver, wait)
    font_color_dropdown().click()
    select_font_style_dropdown().click()
    select_random_font(driver)
    select_font_style_dropdown().click()
    select_font_weight_dropdown().click()
    select_bold_font_weight(driver)
    select_font_weight_dropdown().click()
    select_font_size_dropdown().click()
    select_random_font_size(driver)
    select_font_size_dropdown().click()
    select_font_alignment_dropdown().click()
    select_random_alignment(driver)
    select_font_alignment_dropdown().click()
    logger.info("Shrub styling applied successfully")


def test_shrub_style_header():
    shrub_header_dropdown().click()
    sub_header_font_color_dropdown().click()
    select_random_preset_color(driver, wait)
    select_sub_header_font_style_dropdown().click()
    select_random_font(driver)
    select_sub_header_font_style_dropdown().click()
    select_sub_header_font_weight_dropdown().click()
    select_bold_font_weight(driver)
    select_sub_header_font_weight_dropdown().click()
    select_sub_header_font_size_dropdown().click()
    select_random_font_size(driver)
    select_sub_header_font_size_dropdown().click()
    select_font_alignment_dropdown().click()
    select_random_alignment(driver)
    select_sub_header_font_alignment_dropdown().click()
    shrub_header_dropdown().click()
    shrub_description_dropdown().click()
    save_style_btn().click()
    logger.info("Shrub styling applied successfully")


def test_shrub_description_style():
    shrub_description_dropdown().click()
    description_font_color_dropdown().click()
    select_random_preset_color(driver, wait)
    select_description_font_style_dropdown().click()
    select_random_font(driver)
    select_description_font_style_dropdown().click()
    select_description_font_weight_dropdown().click()
    select_bold_font_weight(driver)
    select_description_font_weight_dropdown().click()
    select_description_font_size_dropdown().click()
    select_random_font_size(driver)
    select_description_font_size_dropdown().click()
    select_description_font_alignment_dropdown().click()
    select_random_alignment(driver)
    select_description_font_alignment_dropdown().click()
    shrub_description_dropdown().click()
    save_style_btn().click()
    logger.info("Shrub styling applied successfully")


def test_shrub_header_style():
    header_dropdown().click()
    header_background_dropdown().click()
    select_header_background_image_btn().click()
    upload_random_image("image")
    logger.info("Uploaded random image from 'image' folder")
    next_image_btn().click()
    logger.info("Clicked 'Next' button after image upload")
    zoomin_image_btn()
    logger.info("Zoomed in image")
    zoom_out_image_btn()
    logger.info("Zoomed out image")
    save_crop_image_btn().click()
    save_screenshot("Header Background_image")
    time.sleep(1)
    select_no_header_background_btn().click()
    select_header_color_picker_btn().click()
    select_random_preset_color(driver, wait)
    save_screenshot("Color_pick")
    time.sleep(1)
    select_no_header_background_btn().click()
    header_background_dropdown().click()
    shrub_title_dropdown().click()
    select_random_preset_color(driver, wait)
    font_color_dropdown().click()
    select_font_style_dropdown().click()
    select_random_font(driver)
    select_font_style_dropdown().click()
    select_font_weight_dropdown().click()
    select_bold_font_weight(driver)
    select_font_weight_dropdown().click()
    select_font_size_dropdown().click()
    select_random_font_size(driver)
    select_font_size_dropdown().click()
    select_font_alignment_dropdown().click()
    select_random_alignment(driver)
    select_font_alignment_dropdown().click()
    shrub_header_dropdown().click()
    shrub_description_dropdown().click()
    save_style_btn().click()
    shrub_header_dropdown().click()
    sub_header_font_color_dropdown().click()
    select_random_preset_color(driver, wait)
    select_sub_header_font_style_dropdown().click()
    select_random_font(driver)
    select_sub_header_font_style_dropdown().click()
    select_sub_header_font_weight_dropdown().click()
    select_bold_font_weight(driver)
    select_sub_header_font_weight_dropdown().click()
    select_sub_header_font_size_dropdown().click()
    select_random_font_size(driver)
    select_sub_header_font_size_dropdown().click()
    select_font_alignment_dropdown().click()
    select_random_alignment(driver)
    select_sub_header_font_alignment_dropdown().click()
    shrub_header_dropdown().click()
    shrub_description_dropdown().click()
    save_style_btn().click()
    logger.info("Shrub styling applied successfully")
    # save_header_style_btn().click()
