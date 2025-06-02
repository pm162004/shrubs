import random
import time, os, datetime

import selenium
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
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


def display_analytics_after_login():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-signin']")))


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
    def password_mask_button():
        try:
            password_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//*[name()='path' and contains(@d,'M12 7c2.76')]"))
            )
            if password_button.is_displayed() and password_button.is_enabled():
                password_button.click()
            else:
                raise Exception("Password mask button not interactable.")
        except TimeoutException:
            driver.save_screenshot("error_password_button_not_clickable.png")
            print("TimeoutException: The password mask button was not clickable.")
            raise
        except Exception as e:
            print(f"Exception: {str(e)}")
            raise


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
    driver.save_screenshot(f"{folder}/{filename}")
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
    return wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-close-modal' and contains(., 'Cancel')]")))


def upload_files_orange_btn():
    return wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-view' and contains(., 'Upload Files')]")))


def save_new_shrub_btn():
    logger.info("Waiting for save shrub button to be clickable")
    overlay_spinner()
    new_shrub_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btn-save")))
    return new_shrub_btn.click()


def next_image_btn():
    wait = WebDriverWait(driver, 20)

    try:
        wait.until(EC.invisibility_of_element_located((By.ID, "overlay-spinner")))

        next_button = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//button[.//div[normalize-space(text())='Next']]")))
        next_button.click()
        logger.info("Clicked 'Next' button")
    except TimeoutException:
        logger.error("TimeoutException: 'Next' button was not clickable within the timeout.")
        raise
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise


def save_crop_image_btn():
    overlay_spinner()
    return wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='button' and .//div[@class='md-button-content' and normalize-space()='Save']]")))


def upload_image_my_files_btn(driver, wait):
    element = wait.until(EC.presence_of_element_located(
        (By.XPATH,
         "//div[contains(@class, 'sidebar-card') and .//p[normalize-space(text())='My Files']]//a[contains(@class, 'menu-list-item')]")))

    # Scroll into view and click using ActionChains
    ActionChains(driver).move_to_element(element).click().perform()
    return element


def upload_image_my_shrubs_btn():
    return wait.until(EC.element_to_be_clickable(
        (By.XPATH,
         "//div[contains(@class, 'sidebar-card') and .//p[normalize-space(text())='My Shrubs']]//a[contains(@class, 'menu-list-item')]")))


def select_thumbnail_folder():
    try:
        element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[span[text()[normalize-space()='thumbnail']]]")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

        ActionChains(driver).move_to_element(element).double_click().perform()
        print("[INFO] Double-clicked on 'thumbnail' folder.")

    except Exception as e:
        print(f"[ERROR] Could not double-click thumbnail folder: {e}")
        driver.save_screenshot("error_thumbnail_doubleclick.png")
        raise


def select_random_image(driver):
    try:
        try:
            WebDriverWait(driver, 20).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "md-overlay"))
            )
        except TimeoutException:
            logger.warning("Overlay did not disappear – continuing anyway")

        images = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img.object-cover"))
        )

        logger.info(f"Found {len(images)} images")

        selected_image = random.choice(images)

        driver.execute_script(
            "window.scrollTo(0, arguments[0].getBoundingClientRect().top + window.scrollY - 100);",
            selected_image
        )

        try:
            ActionChains(driver).move_to_element(selected_image).pause(0.2).click().perform()
        except Exception as e:
            logger.warning(f"ActionChains click failed: {e} — trying JS click")
            driver.execute_script("arguments[0].click();", selected_image)

        logger.info("Random image selected successfully")

    except Exception as e:
        logger.error(f"Failed to select random image: {e}")


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
    zoom_out_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'icons')]//img[contains(@src, 'zoom-out')]"))
    )
    assert zoom_out_button.is_displayed()
    assert zoom_out_button.is_enabled()
    return zoom_out_button.click()


def wait_for_spinner_to_disappear(driver, timeout=10, short_wait=2):
    try:
        spinner = WebDriverWait(driver, short_wait).until(
            EC.presence_of_element_located((By.CLASS_NAME, "v-overlay__content"))
        )
        if spinner:
            WebDriverWait(driver, timeout).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "v-overlay__content"))
            )
    except TimeoutException:
        pass


def overlay_spinner():
    import selenium
    try:
        spinner = driver.find_elements(By.ID, "overlay-spinner")
        if spinner:
            WebDriverWait(driver, 30).until(
                EC.invisibility_of_element_located((By.ID, "overlay-spinner"))
            )
    except selenium.common.exceptions.InvalidSessionIdException:
        logger.error("Driver session invalid during overlay_spinner call")
        raise


def wait_for_overlay_to_disappear(driver, timeout=10):
    WebDriverWait(driver, timeout).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "md-overlay"))
    )


def select_random_font(driver):
    wait = WebDriverWait(driver, 30)
    actions = ActionChains(driver)

    try:
        try:
            wait.until_not(EC.presence_of_element_located((By.CSS_SELECTOR, ".loading-overlay")))
        except:
            pass

        combobox = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.multiselect")))
        driver.execute_script("arguments[0].scrollIntoView(true);", combobox)
        actions.move_to_element(combobox).click().perform()

        font_options = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "li.multiselect__element:not([style*='display: none']) > span.multiselect__option")
        ))

        if not font_options:
            raise Exception("No fonts found in the dropdown.")

        selected_font = random.choice(font_options)
        font_name = selected_font.text.strip()
        actions.move_to_element(selected_font).click().perform()
        return font_name

    except TimeoutException:
        driver.save_screenshot("error_combobox_not_found.png")
        raise
    except Exception as e:
        raise


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

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", selected_shrub)

        wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            "div.cursor-pointer.flex.flex-wrap.items-center.justify-center.rounded-lg"
        )))

        actions = ActionChains(driver)
        actions.move_to_element(selected_shrub).double_click().perform()

        print("[INFO] Random shrub double-clicked.")

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


def background_color_dropdown():
    overlay_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Background']")))


def embedded_website_url_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Embedded Website URL']")))


def thumbnail_image_dropdown():
    overlay_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Thumbnail Image']")))


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


def select_font_banner_background_dropdown():
    return wait.until(EC.element_to_be_clickable(
        (By.XPATH, "(//span[@class='md-list-item-text' and text()='Font Banner Background'])[1]")))


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

    alignment_buttons = wait.until(EC.presence_of_all_elements_located((
        By.XPATH,
        "//h5[contains(text(),'Horizontal font alignment')]/following::div[contains(@class,'justify-around')]/span"
    )))

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

    font_weight_dropdown = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//label[contains(text(), 'Select your font weight')]/following-sibling::div"
    )))
    font_weight_dropdown.click()

    bold_option = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//span[@class='multiselect__option' and normalize-space(text())='Bold']"
    )))
    bold_option.click()

    print("Bold font weight selected.")


def select_random_font_size(driver):
    wait = WebDriverWait(driver, 10)

    font_size_dropdown = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//label[contains(text(), 'Select your font size')]/following-sibling::div"
    )))
    font_size_dropdown.click()

    font_size_options = wait.until(EC.presence_of_all_elements_located((
        By.XPATH, "//span[@class='multiselect__option']"
    )))

    random_option = random.choice(font_size_options)
    print(f"Randomly selected font size: {random_option.text}")

    random_option.click()


def shrub_description_dropdown():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Shrub Description']")))


def select_color_picker_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "(//img[contains(@src, 'color-picker')])[1]")))


def select_header_color_picker_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "(//img[contains(@src, 'color-picker')])[1]")))


def select_banner_color_picker_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "(//img[contains(@src, 'color-picker')])[2]")))


def select_background_color_picker_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "(//img[contains(@src, 'color-picker')])[3]")))


def select_background_image_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//img[contains(@src, 'background-image')]")))


def select_icon_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH,
                                                  "//i[contains(@class, 'feather--arrow-down-left')]/ancestor::div[contains(@class, 'cursor-pointer')]")))


def select_header_background_image_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "(//img[contains(@src, 'background-image')])[1]")))


def select_no_background_btn():
    logger.info("Waiting for 'No Background' button")
    wait_for_overlay_to_disappear(driver)
    wait_for_spinner_to_disappear(driver)
    element = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//img[contains(@src, 'no-background')]/parent::div")
    ))
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//img[contains(@src, 'no-background')]/parent::div")
    ))
    return element


def select_no_banner_background_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "(//img[contains(@src, 'no-background')]/parent::div)[1]")))


def select_no_color_background_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "(//img[contains(@src, 'no-background')]/parent::div)[2]")))


def select_no_thumbnail_background_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "(//img[contains(@src, 'no-background')]/parent::div)[3]")))


def select_no_header_background_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "(//img[contains(@src, 'no-background')]/parent::div)[1]")))


def select_color_from_color_picker():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Color:#BD10E0']")))


def select_random_preset_color(driver, wait):
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class*='vc-sketch']")))

        preset_colors = wait.until(EC.presence_of_all_elements_located((
            By.XPATH, "//div[contains(@class, 'vc-sketch-presets-color')]"
        )))

        if not preset_colors:
            raise Exception("No preset colors found.")

        random_color = random.choice(preset_colors)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", random_color)
        ActionChains(driver).move_to_element(random_color).click().perform()
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


def new_branch_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-new-branch']")))


def save_as_template_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Save As Template')]")))


def create_links_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='Create Links']")))


def embedded_code_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='Embedded Code']")))


def upload_files_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='Upload Files']")))


def upload_images_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='Upload Images']")))


def upload_videos_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='Upload Videos']")))


def upload_audio_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='Upload Audio']")))


def save_new_branch_btn():
    overlay_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Save')]")))


def link_branch_title_validation():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//small[@class='text-danger']")))


def link_branch_title_input_field():
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Branch Title']")))


def branch_add_link_btn():
    progress_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-upload-image']")))


def branch_add_code_btn():
    progress_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-upload-image']")))


def progress_spinner():
    return WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.ID, "progress-spinner")))


def add_link_input_field():
    progress_spinner()
    return wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Link']")))


def add_code_textarea():
    progress_spinner()
    return wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[contains(@class, 'pb1')]//textarea[contains(@class, 'code-area')]")))


def link_save_btn():
    progress_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Save')]")))


def code_save_btn():
    progress_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-save' and contains(., 'Save')]")))


def upload_save_btn():
    progress_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-save' and contains(., 'Save')]")))


def upload_view_btn():
    progress_spinner()
    return wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[@name='btn-upload-image']//div[@class='md-ripple md-disabled']")))


def back_branch_link_btn():
    progress_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Back')]")))


def bank_branch_btn():
    progress_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-save' and contains(., 'Save')]")))


def back_code_btn():
    progress_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "// button[ @ name = 'btn-save' and contains(., 'Back')]")))


def back_link_btn():
    progress_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Back')]")))


def wait_time():
    return time.sleep(2)


def switch_to_window(driver, window_index=0):
    windows = driver.window_handles
    if windows:
        driver.switch_to.window(windows[window_index])  # Switch to the first window
    else:
        raise Exception("No windows are open.")


# ============================== TEST CASES ==============================

class TestPositiveFlow:

    def test_valid_login_flow(self):
        try:
            logger.info("Running test: Valid login flow")
            refresh_page()
            logger.info("Refreshing page completed")
            logger.info("Entering email")
            email_input_field().send_keys(config.CORRECT_EMAIL)
            logger.info("Entering password")
            password_input_field().send_keys(config.CORRECT_PASSWORD)
            logger.info("Clicking password visibility toggle")
            password_mask_button()
            logger.info("Clicking login button")
            login_button().click()

            WebDriverWait(driver, 20).until(EC.url_contains("analytics"))

            assert "analytics" in driver.current_url, f"Login failed! Current URL is: {driver.current_url}"
            logger.info("Valid login passed, 'My Files' is visible")

        except AssertionError as e:
            logger.error(f"AssertionError: {e}")
            driver.save_screenshot("error_valid_login_flow.png")
            raise

        except Exception as e:
            logger.error(f"Exception during valid login flow: {e}")
            driver.save_screenshot("error_valid_login_flow_generic.png")
            raise

    def test_my_shrubs(self):
        logger.info("Navigating to 'My Shrubs'")
        get_my_shrubs().click()

        # Wait for spinner to disappear (increase timeout to 30 seconds)
        WebDriverWait(driver, 30).until(
            EC.invisibility_of_element_located((By.ID, "overlay-spinner"))
        )
        logger.info("Overlay spinner disappeared after navigating to 'My Shrubs'")

        # Wait for 'New Shrub' button to be clickable
        new_shrub_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='md-button-content' and text()='New Shrub']"))
        )

        # Scroll the button into view
        driver.execute_script("arguments[0].scrollIntoView(true);", new_shrub_button)

        # Small pause to avoid click interception from any lingering overlays
        import time
        time.sleep(0.5)

        # Try normal click, fallback to JS click if intercepted
        try:
            new_shrub_button.click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            logger.warning("Normal click intercepted, trying JS click")
            driver.execute_script("arguments[0].click();", new_shrub_button)

    def test_valid_shrubs(self):
        logger.info("Testing valid shrub creation")
        WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.ID, "overlay-spinner")))
        shrub_title_input_field = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='shrub-name']")))
        driver.execute_script("arguments[0].scrollIntoView(true);", shrub_title_input_field)
        shrub_title_input_field.send_keys(input_field.VALID_SHRUBS)
        logger.info(f"Entered shrub title: {input_field.VALID_SHRUBS}")
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
        wait_time()
        select_thumbnail_image_btn().click()
        logger.info("Clicked 'Thumbnail Image' button")
        upload_random_image("image")
        logger.info("Uploaded random image from 'image' folder")
        next_image_btn()
        logger.info("Clicked 'Next' button after image upload")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        wait_for_spinner_to_disappear(driver)
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
        upload_image_my_files_btn(driver, wait)
        logger.info("Clicked 'My Files' folder upload button")
        logger.info("Thumbnail images loaded in 'My Files' folder")
        select_random_image(driver)
        logger.info("Selected a random image from 'My Files'")
        next_image_btn()
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
        next_image_btn()
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
        save_new_shrub_btn()
        logger.info("Clicked 'Save New Shrub' button to finalize creation")

    def test_shrub_style_background(self):
        logger.info("Testing shrub styling")
        wait_for_overlay_to_disappear(driver)
        wait_for_spinner_to_disappear(driver)
        wait_time()
        background_color_dropdown().click()
        select_background_image_btn().click()
        upload_random_image("image")
        logger.info("Uploaded random image from 'image' folder")
        next_image_btn()
        logger.info("Clicked 'Next' button after image upload")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        save_screenshot("Background_image")
        wait_for_overlay_to_disappear(driver)
        select_no_background_btn().click()
        select_color_picker_btn().click()
        select_random_preset_color(driver, wait)
        save_screenshot("Color_pick")
        select_no_background_btn().click()
        background_color_dropdown().click()

    def test_shrub_style_shrub_title(self):
        wait_for_overlay_to_disappear(driver)
        element = shrub_title_dropdown()
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        font_color_dropdown().click()
        select_banner_color_picker_btn().click()
        select_random_preset_color(driver, wait)
        font_color_dropdown().click()
        dropdown = select_font_style_dropdown()
        driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
        dropdown.click()
        select_random_font(driver)
        dropdown.click()
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

    def test_shrub_style_header(self):
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

    def test_shrub_description_style(self):
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
        save_as_template_btn().click()
        save_style_btn().click()
        logger.info("Shrub styling applied successfully")

    def test_shrub_header_style(self):
        header_dropdown().click()
        header_background_dropdown().click()
        select_header_background_image_btn().click()
        upload_random_image("image")
        logger.info("Uploaded random image from 'image' folder")
        next_image_btn()
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
        save_header_style_btn().click()

    def test_new_branch_create_links_style(self):
        new_branch_btn().click()
        create_links_btn().click()
        link_branch_title_input_field().send_keys(input_field.VALID_SHRUBS)
        font_color_dropdown().click()
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
        select_font_banner_background_dropdown().click()
        select_banner_color_picker_btn().click()
        select_random_preset_color(driver, wait)
        select_no_banner_background_btn().click()
        select_font_banner_background_dropdown().click()
        background_color_dropdown().click()
        select_background_color_picker_btn().click()
        select_random_preset_color(driver, wait)
        select_no_color_background_btn().click()
        background_color_dropdown().click()
        thumbnail_image_dropdown().click()
        select_background_image_btn().click()
        upload_random_image("image")
        logger.info("Uploaded random image from 'image' folder")
        next_image_btn()
        logger.info("Clicked 'Next' button after image upload")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        save_screenshot("Background_image")
        wait_for_overlay_to_disappear(driver)
        select_no_thumbnail_background_btn().click()
        select_icon_btn().click()
        select_random_icon()
        logger.info("Selected random icon")
        thumbnail_icon_cancel_btn().click()
        logger.info("Cancelled thumbnail icon selection")
        thumbnail_image_dropdown().click()
        save_as_template_btn().click()
        save_new_branch_btn().click()
        logger.info("Branch created successfully")
        branch_add_link_btn().click()
        add_link_input_field().send_keys(Keys.ENTER)
        time.sleep(1)
        link_save_btn().click()
        add_link_input_field().send_keys(input_field.VALID_SHRUBS)
        link_save_btn().click()
        add_link_input_field().send_keys(Keys.CONTROL, "a")
        add_link_input_field().send_keys(Keys.DELETE)
        add_link_input_field().send_keys(input_field.LINK)
        add_link_input_field().send_keys(Keys.ENTER)
        time.sleep(2)
        link_save_btn().click()
        back_branch_link_btn().click()
        link_save_btn().click()
        back_link_btn().click()
        logger.info("Link added successfully")

    def test_new_branch_embedded_code(self):
        new_branch_btn().click()
        embedded_code_btn().click()
        link_branch_title_input_field().send_keys(input_field.VALID_SHRUBS)
        font_color_dropdown().click()
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
        select_font_banner_background_dropdown().click()
        select_banner_color_picker_btn().click()
        select_random_preset_color(driver, wait)
        select_no_banner_background_btn().click()
        select_font_banner_background_dropdown().click()
        background_color_dropdown().click()
        select_background_color_picker_btn().click()
        select_random_preset_color(driver, wait)
        select_no_color_background_btn().click()
        background_color_dropdown().click()
        thumbnail_image_dropdown().click()
        select_background_image_btn().click()
        upload_random_image("image")
        logger.info("Uploaded random image from 'image' folder")
        next_image_btn()
        logger.info("Clicked 'Next' button after image upload")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        save_screenshot("Background_image")
        wait_for_overlay_to_disappear(driver)
        select_no_thumbnail_background_btn().click()
        select_icon_btn().click()
        select_random_icon()
        logger.info("Selected random icon")
        thumbnail_icon_cancel_btn().click()
        logger.info("Cancelled thumbnail icon selection")
        thumbnail_image_dropdown().click()
        save_as_template_btn().click()
        save_new_branch_btn().click()
        branch_add_code_btn().click()
        logger.info("Branch created successfully")
        add_code_textarea().send_keys(input_field.VALID_SHRUBS)
        embedded_website_url_btn().click()
        time.sleep(1)
        code_save_btn().click()
        add_code_textarea().send_keys(Keys.CONTROL, "a")
        add_code_textarea().send_keys(Keys.DELETE)
        add_code_textarea().send_keys(input_field.LINK)
        add_code_textarea().send_keys(Keys.ENTER)
        time.sleep(2)
        code_save_btn().click()
        back_code_btn().click()
        back_link_btn().click()
        logger.info("Link added successfully")

    def test_new_branch_upload_files(self):
        new_branch_btn().click()
        upload_files_btn().click()
        link_branch_title_input_field().send_keys(input_field.VALID_SHRUBS)
        font_color_dropdown().click()
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
        select_font_banner_background_dropdown().click()
        select_banner_color_picker_btn().click()
        select_random_preset_color(driver, wait)
        select_no_banner_background_btn().click()
        select_font_banner_background_dropdown().click()
        background_color_dropdown().click()
        select_background_color_picker_btn().click()
        select_random_preset_color(driver, wait)
        select_no_color_background_btn().click()
        background_color_dropdown().click()
        thumbnail_image_dropdown().click()
        select_background_image_btn().click()
        upload_random_image("image")
        logger.info("Uploaded random image from 'image' folder")
        next_image_btn()
        logger.info("Clicked 'Next' button after image upload")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        save_screenshot("Background_image")
        wait_for_overlay_to_disappear(driver)
        select_no_thumbnail_background_btn().click()
        select_icon_btn().click()
        select_random_icon()
        logger.info("Selected random icon")
        thumbnail_icon_cancel_btn().click()
        logger.info("Cancelled thumbnail icon selection")
        thumbnail_image_dropdown().click()
        save_as_template_btn().click()
        upload_save_btn().click()
        upload_view_btn().click()
        upload_files_orange_btn().click()
        logger.info("Branch created successfully")
        logger.info("Starting 'My Computer' image upload and crop flow")
        wait_time()
        select_thumbnail_image_btn().click()
        logger.info("Clicked 'Thumbnail Image' button")
        upload_random_image("image")
        logger.info("Uploaded random image from 'image' folder")
        next_image_btn()
        logger.info("Clicked 'Next' button after image upload")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        wait_for_spinner_to_disappear(driver)
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        logger.info("Clicked 'Save' button to save cropped image")
        logger.info("Images added successfully")
        upload_files_orange_btn().click()
        overlay_spinner()
        logger.info("Overlay spinner disappeared")
        select_thumbnail_image_btn().click()
        logger.info("Clicked 'Thumbnail Image' button")
        upload_image_my_files_btn(driver, wait)
        logger.info("Clicked 'My Files' folder upload button")
        logger.info("Thumbnail images loaded in 'My Files' folder")
        select_random_image(driver)
        logger.info("Selected a random image from 'My Files'")
        next_image_btn()
        logger.info("Clicked 'Next' button")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        logger.info("Clicked 'Save' button for cropped image")
        logger.info("Valid shrub created in 'My Files' image flow")
        upload_files_orange_btn().click()
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
        raise  # re-raise exception to propagate it
        logger.info("Thumbnail span appeared after shrub selection")
        select_thumbnail_folder()
        select_random_image(driver)
        logger.info("Clicked on thumbnail folder")
        next_image_btn()
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
        save_new_shrub_btn()
        logger.info("Clicked 'Save New Shrub' button to finalize creation")
        logger.info("Testing shrub styling")
        wait_for_overlay_to_disappear(driver)
        wait_for_spinner_to_disappear(driver)
        wait_time()
        background_color_dropdown().click()
        select_background_image_btn().click()
        upload_random_image("image")
        logger.info("Uploaded random image from 'image' folder")
        next_image_btn()
        logger.info("Clicked 'Next' button after image upload")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        save_screenshot("Background_image")
        wait_for_overlay_to_disappear(driver)
        select_no_background_btn().click()
        select_color_picker_btn().click()
        select_random_preset_color(driver, wait)
        save_screenshot("Color_pick")
        select_no_background_btn().click()
        background_color_dropdown().click()
        logger.info("Starting 'My Files' image upload and crop flow")
        overlay_spinner()
        logger.info("Overlay spinner disappeared")
        select_thumbnail_image_btn().click()
        logger.info("Clicked 'Thumbnail Image' button")
        upload_image_my_files_btn(driver, wait)
        logger.info("Clicked 'My Files' folder upload button")
        logger.info("Thumbnail images loaded in 'My Files' folder")
        select_random_image(driver)
        logger.info("Selected a random image from 'My Files'")
        next_image_btn()
        logger.info("Clicked 'Next' button")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        logger.info("Clicked 'Save' button for cropped image")
        logger.info("Valid shrub created in 'My Files' image flow")
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
        next_image_btn()
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
        save_new_shrub_btn()
        logger.info("Clicked 'Save New Shrub' button to finalize creation")

    def test_new_branch_embedded_code(self):
        new_branch_btn().click()
        embedded_code_btn().click()
        link_branch_title_input_field().send_keys(input_field.VALID_SHRUBS)
        font_color_dropdown().click()
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
        select_font_banner_background_dropdown().click()
        select_banner_color_picker_btn().click()
        select_random_preset_color(driver, wait)
        select_no_banner_background_btn().click()
        select_font_banner_background_dropdown().click()
        background_color_dropdown().click()
        select_background_color_picker_btn().click()
        select_random_preset_color(driver, wait)
        select_no_color_background_btn().click()
        background_color_dropdown().click()
        thumbnail_image_dropdown().click()
        select_background_image_btn().click()
        upload_random_image("image")
        logger.info("Uploaded random image from 'image' folder")
        next_image_btn()
        logger.info("Clicked 'Next' button after image upload")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        save_screenshot("Background_image")
        wait_for_overlay_to_disappear(driver)
        select_no_thumbnail_background_btn().click()
        select_icon_btn().click()
        select_random_icon()
        logger.info("Selected random icon")
        thumbnail_icon_cancel_btn().click()
        logger.info("Cancelled thumbnail icon selection")
        thumbnail_image_dropdown().click()
        save_as_template_btn().click()
        save_new_branch_btn().click()
        branch_add_code_btn().click()
        logger.info("Branch created successfully")
        add_code_textarea().send_keys(input_field.VALID_SHRUBS)
        embedded_website_url_btn().click()
        time.sleep(1)
        code_save_btn().click()
        add_code_textarea().send_keys(Keys.CONTROL, "a")
        add_code_textarea().send_keys(Keys.DELETE)
        add_code_textarea().send_keys(input_field.LINK)
        add_code_textarea().send_keys(Keys.ENTER)
        time.sleep(2)

        code_save_btn().click()
        back_code_btn().click()
        back_link_btn().click()
        logger.info("Link added successfully")

    def test_new_branch_upload_images(self):
        new_branch_btn().click()
        upload_images_btn().click()
        link_branch_title_input_field().send_keys(input_field.VALID_SHRUBS)
        font_color_dropdown().click()
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
        select_font_banner_background_dropdown().click()
        select_banner_color_picker_btn().click()
        select_random_preset_color(driver, wait)
        select_no_banner_background_btn().click()
        select_font_banner_background_dropdown().click()
        background_color_dropdown().click()
        select_background_color_picker_btn().click()
        select_random_preset_color(driver, wait)
        select_no_color_background_btn().click()
        background_color_dropdown().click()
        thumbnail_image_dropdown().click()
        select_background_image_btn().click()
        upload_random_image("image")
        logger.info("Uploaded random image from 'image' folder")
        next_image_btn()
        logger.info("Clicked 'Next' button after image upload")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        save_screenshot("Background_image")
        wait_for_overlay_to_disappear(driver)
        select_no_thumbnail_background_btn().click()
        select_icon_btn().click()
        select_random_icon()
        logger.info("Selected random icon")
        thumbnail_icon_cancel_btn().click()
        logger.info("Cancelled thumbnail icon selection")
        thumbnail_image_dropdown().click()
        save_as_template_btn().click()
        upload_save_btn().click()
        upload_view_btn().click()
        upload_files_orange_btn().click()
        logger.info("Branch created successfully")
        logger.info("Starting 'My Computer' image upload and crop flow")
        wait_time()
        select_thumbnail_image_btn().click()
        logger.info("Clicked 'Thumbnail Image' button")
        upload_random_image("image")
        logger.info("Uploaded random image from 'image' folder")
        next_image_btn()
        logger.info("Clicked 'Next' button after image upload")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        wait_for_spinner_to_disappear(driver)
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        logger.info("Clicked 'Save' button to save cropped image")
        logger.info("Images added successfully")
        upload_files_orange_btn().click()
        overlay_spinner()
        logger.info("Overlay spinner disappeared")
        select_thumbnail_image_btn().click()
        logger.info("Clicked 'Thumbnail Image' button")
        upload_image_my_files_btn(driver, wait)
        logger.info("Clicked 'My Files' folder upload button")
        logger.info("Thumbnail images loaded in 'My Files' folder")
        select_random_image(driver)
        logger.info("Selected a random image from 'My Files'")
        next_image_btn()
        logger.info("Clicked 'Next' button")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        logger.info("Clicked 'Save' button for cropped image")
        logger.info("Valid shrub created in 'My Files' image flow")
        upload_files_orange_btn().click()
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
            raise  # re-raise exception to propagate it

        logger.info("Thumbnail span appeared after shrub selection")
        select_thumbnail_folder()
        select_random_image(driver)
        logger.info("Clicked on thumbnail folder")
        next_image_btn()
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
        save_new_shrub_btn()
        logger.info("Clicked 'Save New Shrub' button to finalize creation")
        logger.info("Testing shrub styling")
        wait_for_overlay_to_disappear(driver)
        wait_for_spinner_to_disappear(driver)
        wait_time()
        background_color_dropdown().click()
        select_background_image_btn().click()
        upload_random_image("image")
        logger.info("Uploaded random image from 'image' folder")
        next_image_btn()
        logger.info("Clicked 'Next' button after image upload")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        save_screenshot("Background_image")
        wait_for_overlay_to_disappear(driver)
        select_no_background_btn().click()
        select_color_picker_btn().click()
        select_random_preset_color(driver, wait)
        save_screenshot("Color_pick")
        select_no_background_btn().click()
        background_color_dropdown().click()
        logger.info("Starting 'My Files' image upload and crop flow")
        overlay_spinner()
        logger.info("Overlay spinner disappeared")
        select_thumbnail_image_btn().click()
        logger.info("Clicked 'Thumbnail Image' button")
        upload_image_my_files_btn(driver, wait)
        logger.info("Clicked 'My Files' folder upload button")
        logger.info("Thumbnail images loaded in 'My Files' folder")
        select_random_image(driver)
        logger.info("Selected a random image from 'My Files'")
        next_image_btn()
        logger.info("Clicked 'Next' button")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        logger.info("Clicked 'Save' button for cropped image")
        logger.info("Valid shrub created in 'My Files' image flow")
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
        next_image_btn()
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
        save_new_shrub_btn()
        logger.info("Clicked 'Save New Shrub' button to finalize creation")

    def test_new_branch_upload_videos(self):
        new_branch_btn().click()
        upload_images_btn().click()
        link_branch_title_input_field().send_keys(input_field.VALID_SHRUBS)
        font_color_dropdown().click()
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
        select_font_banner_background_dropdown().click()
        select_banner_color_picker_btn().click()
        select_random_preset_color(driver, wait)
        select_no_banner_background_btn().click()
        select_font_banner_background_dropdown().click()
        background_color_dropdown().click()
        select_background_color_picker_btn().click()
        select_random_preset_color(driver, wait)
        select_no_color_background_btn().click()
        background_color_dropdown().click()
        thumbnail_image_dropdown().click()
        select_background_image_btn().click()
        upload_random_image("image")
        logger.info("Uploaded random image from 'image' folder")
        next_image_btn()
        logger.info("Clicked 'Next' button after image upload")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        save_screenshot("Background_image")
        wait_for_overlay_to_disappear(driver)
        select_no_thumbnail_background_btn().click()
        select_icon_btn().click()
        select_random_icon()
        logger.info("Selected random icon")
        thumbnail_icon_cancel_btn().click()
        logger.info("Cancelled thumbnail icon selection")
        thumbnail_image_dropdown().click()
        save_as_template_btn().click()
        upload_save_btn().click()
        upload_view_btn().click()
        upload_files_orange_btn().click()
        logger.info("Branch created successfully")
        logger.info("Starting 'My Computer' image upload and crop flow")
        wait_time()
        select_thumbnail_image_btn().click()
        logger.info("Clicked 'Thumbnail Image' button")
        upload_random_image("image")
        logger.info("Uploaded random image from 'image' folder")
        next_image_btn()
        logger.info("Clicked 'Next' button after image upload")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        wait_for_spinner_to_disappear(driver)
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        logger.info("Clicked 'Save' button to save cropped image")
        logger.info("Images added successfully")
        upload_files_orange_btn().click()
        overlay_spinner()
        logger.info("Overlay spinner disappeared")
        select_thumbnail_image_btn().click()
        logger.info("Clicked 'Thumbnail Image' button")
        upload_image_my_files_btn(driver, wait)
        logger.info("Clicked 'My Files' folder upload button")
        logger.info("Thumbnail images loaded in 'My Files' folder")
        select_random_image(driver)
        logger.info("Selected a random image from 'My Files'")
        next_image_btn()
        logger.info("Clicked 'Next' button")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        logger.info("Clicked 'Save' button for cropped image")
        logger.info("Valid shrub created in 'My Files' image flow")
        upload_files_orange_btn().click()
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
            raise  # re-raise exception to propagate it

        driver.save_screenshot("error_thumbnail_label_missing.png")
        raise
        logger.info("Thumbnail span appeared after shrub selection")
        select_thumbnail_folder()
        select_random_image(driver)
        logger.info("Clicked on thumbnail folder")
        next_image_btn()
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
        save_new_shrub_btn()
        logger.info("Clicked 'Save New Shrub' button to finalize creation")
        logger.info("Testing shrub styling")
        wait_for_overlay_to_disappear(driver)
        wait_for_spinner_to_disappear(driver)
        wait_time()
        background_color_dropdown().click()
        select_background_image_btn().click()
        upload_random_image("image")
        logger.info("Uploaded random image from 'image' folder")
        next_image_btn()
        logger.info("Clicked 'Next' button after image upload")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        save_screenshot("Background_image")
        wait_for_overlay_to_disappear(driver)
        select_no_background_btn().click()
        select_color_picker_btn().click()
        select_random_preset_color(driver, wait)
        save_screenshot("Color_pick")
        select_no_background_btn().click()
        background_color_dropdown().click()
        logger.info("Starting 'My Files' image upload and crop flow")
        overlay_spinner()
        logger.info("Overlay spinner disappeared")
        select_thumbnail_image_btn().click()
        logger.info("Clicked 'Thumbnail Image' button")
        upload_image_my_files_btn(driver, wait)
        logger.info("Clicked 'My Files' folder upload button")
        logger.info("Thumbnail images loaded in 'My Files' folder")
        select_random_image(driver)
        logger.info("Selected a random image from 'My Files'")
        next_image_btn()
        logger.info("Clicked 'Next' button")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        logger.info("Clicked 'Save' button for cropped image")
        logger.info("Valid shrub created in 'My Files' image flow")
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
        next_image_btn()
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
        save_new_shrub_btn()
        logger.info("Clicked 'Save New Shrub' button to finalize creation")

    def test_new_branch_upload_audios(self):
        new_branch_btn().click()
        upload_images_btn().click()
        link_branch_title_input_field().send_keys(input_field.VALID_SHRUBS)
        font_color_dropdown().click()
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
        select_font_banner_background_dropdown().click()
        select_banner_color_picker_btn().click()
        select_random_preset_color(driver, wait)
        select_no_banner_background_btn().click()
        select_font_banner_background_dropdown().click()
        background_color_dropdown().click()
        select_background_color_picker_btn().click()
        select_random_preset_color(driver, wait)
        select_no_color_background_btn().click()
        background_color_dropdown().click()
        thumbnail_image_dropdown().click()
        select_background_image_btn().click()
        upload_random_image("image")
        logger.info("Uploaded random image from 'image' folder")
        next_image_btn()
        logger.info("Clicked 'Next' button after image upload")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        save_screenshot("Background_image")
        wait_for_overlay_to_disappear(driver)
        select_no_thumbnail_background_btn().click()
        select_icon_btn().click()
        select_random_icon()
        logger.info("Selected random icon")
        thumbnail_icon_cancel_btn().click()
        logger.info("Cancelled thumbnail icon selection")
        thumbnail_image_dropdown().click()
        save_as_template_btn().click()
        upload_save_btn().click()
        upload_view_btn().click()
        upload_files_orange_btn().click()
        logger.info("Branch created successfully")

        logger.info("Starting 'My Computer' image upload and crop flow")
        wait_time()
        select_thumbnail_image_btn().click()
        logger.info("Clicked 'Thumbnail Image' button")
        upload_random_image("image")
        logger.info("Uploaded random image from 'image' folder")
        next_image_btn()
        logger.info("Clicked 'Next' button after image upload")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        wait_for_spinner_to_disappear(driver)
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        logger.info("Clicked 'Save' button to save cropped image")
        logger.info("Images added successfully")
        upload_files_orange_btn().click()
        overlay_spinner()
        logger.info("Overlay spinner disappeared")
        select_thumbnail_image_btn().click()
        logger.info("Clicked 'Thumbnail Image' button")
        upload_image_my_files_btn(driver, wait)
        logger.info("Clicked 'My Files' folder upload button")
        logger.info("Thumbnail images loaded in 'My Files' folder")
        select_random_image(driver)
        logger.info("Selected a random image from 'My Files'")
        next_image_btn()
        logger.info("Clicked 'Next' button")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        logger.info("Clicked 'Save' button for cropped image")
        logger.info("Valid shrub created in 'My Files' image flow")
        upload_files_orange_btn().click()
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
            raise  # re-raise exception to propagate it

        logger.info("Thumbnail span appeared after shrub selection")
        select_thumbnail_folder()
        select_random_image(driver)
        logger.info("Clicked on thumbnail folder")
        next_image_btn()
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
        save_new_shrub_btn()
        logger.info("Clicked 'Save New Shrub' button to finalize creation")
        logger.info("Testing shrub styling")
        wait_for_overlay_to_disappear(driver)
        wait_for_spinner_to_disappear(driver)
        wait_time()
        background_color_dropdown().click()
        select_background_image_btn().click()
        upload_random_image("image")
        logger.info("Uploaded random image from 'image' folder")
        next_image_btn()
        logger.info("Clicked 'Next' button after image upload")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        save_screenshot("Background_image")
        wait_for_overlay_to_disappear(driver)
        select_no_background_btn().click()
        select_color_picker_btn().click()
        select_random_preset_color(driver, wait)
        save_screenshot("Color_pick")
        select_no_background_btn().click()
        background_color_dropdown().click()
        logger.info("Starting 'My Files' image upload and crop flow")
        overlay_spinner()
        logger.info("Overlay spinner disappeared")
        select_thumbnail_image_btn().click()
        logger.info("Clicked 'Thumbnail Image' button")
        upload_image_my_files_btn(driver, wait)
        logger.info("Clicked 'My Files' folder upload button")
        logger.info("Thumbnail images loaded in 'My Files' folder")
        select_random_image(driver)
        logger.info("Selected a random image from 'My Files'")
        next_image_btn()
        logger.info("Clicked 'Next' button")
        zoomin_image_btn()
        logger.info("Zoomed in image")
        zoom_out_image_btn()
        logger.info("Zoomed out image")
        save_crop_image_btn().click()
        logger.info("Clicked 'Save' button for cropped image")
        logger.info("Valid shrub created in 'My Files' image flow")
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
        next_image_btn()
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
        save_new_shrub_btn()
        logger.info("Clicked 'Save New Shrub' button to finalize creation")
