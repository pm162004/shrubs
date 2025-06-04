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
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

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
wait = WebDriverWait(driver, 60)
# driver.implicitly_wait(5)
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


def click_element_with_retry(get_element_func, retries=3):
    for _ in range(retries):
        try:
            element = get_element_func()
            element.click()
            return
        except StaleElementReferenceException:
            time.sleep(0.5)
    raise Exception("Failed to click element due to stale reference")


def thumbnail_icon_cancel_btn():
    return wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-close-modal' and contains(., 'Cancel')]")))


# Usage:
def select_font(driver):
    wait = WebDriverWait(driver, 20)

    try:
        # Step 1: Click the dropdown
        dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='multiselect__select'])[2]")))
        dropdown.click()

        # Step 2: Wait for the list to appear
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "multiselect__content")))

        # Step 3: Get all font options
        font_elements = driver.find_elements(By.CSS_SELECTOR, ".multiselect__element .option__title")
        font_names = [elem.text.strip() for elem in font_elements if elem.text.strip()]

        if not font_names:
            raise Exception("No fonts found in the dropdown.")

        # Step 4: Pick a random font
        selected_font = random.choice(font_names)
        print(f"Randomly selected font: {selected_font}")

        # Step 5: Wait for the input field and type the font name
        input_field = wait.until(
            EC.visibility_of_element_located((By.XPATH, "(//input[@placeholder='Select your font'])[1]")))

        # Ensure input field is cleared before typing

        # Type and select the font
        input_field.send_keys(selected_font)
        input_field.send_keys(Keys.ENTER)

        # Step 6: Close the dropdown (this might help trigger the font selection correctly)
        try:
            close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='multiselect__close']")))
            close_button.click()
        except Exception:
            print("No close button found.")



    except Exception as e:
        print(f"Error occurred while selecting font: {e}")
        raise e  # Re-raise the exception for further debugging


def select_font_branch(driver):
    wait = WebDriverWait(driver, 20)

    try:
        # Step 1: Click the dropdown
        dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='multiselect__select'])[3]")))
        dropdown.click()

        # Step 2: Wait for the list to appear
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "multiselect__content")))

        # Step 3: Get all font options
        font_elements = driver.find_elements(By.CSS_SELECTOR, ".multiselect__element .option__title")
        font_names = [elem.text.strip() for elem in font_elements if elem.text.strip()]

        if not font_names:
            raise Exception("No fonts found in the dropdown.")

        # Step 4: Pick a random font
        selected_font = random.choice(font_names)
        print(f"Randomly selected font: {selected_font}")

        # Step 5: Wait for the input field and type the font name
        input_field = wait.until(
            EC.visibility_of_element_located((By.XPATH, "(//input[@placeholder='Select your font'])[1]")))

        # Ensure input field is cleared before typing

        # Type and select the font
        input_field.send_keys(selected_font)
        input_field.send_keys(Keys.ENTER)

        # Step 6: Close the dropdown (this might help trigger the font selection correctly)
        try:
            close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='multiselect__close']")))
            close_button.click()
        except Exception:
            print("No close button found.")



    except Exception as e:
        print(f"Error occurred while selecting font: {e}")
        raise e  # Re-raise the exception for further debugging


def select_font_header(driver):
    wait = WebDriverWait(driver, 20)

    try:
        # Step 1: Click the dropdown
        dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='multiselect__select'])[5]")))
        dropdown.click()

        # Step 2: Wait for the list to appear
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "multiselect__content")))

        # Step 3: Get all font options
        font_elements = driver.find_elements(By.CSS_SELECTOR, ".multiselect__element .option__title")
        font_names = [elem.text.strip() for elem in font_elements if elem.text.strip()]

        if not font_names:
            raise Exception("No fonts found in the dropdown.")

        # Step 4: Pick a random font
        selected_font = random.choice(font_names)
        print(f"Randomly selected font: {selected_font}")

        # Step 5: Wait for the input field and type the font name
        input_field = wait.until(
            EC.visibility_of_element_located((By.XPATH, "(//input[@placeholder='Select your font'])[2]")))

        # Ensure input field is cleared before typing

        # Type and select the font
        input_field.send_keys(selected_font)
        input_field.send_keys(Keys.ENTER)

        # Step 6: Close the dropdown (this might help trigger the font selection correctly)
        try:
            close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='multiselect__close']")))
            close_button.click()
        except Exception:
            print("No close button found.")



    except Exception as e:
        print(f"Error occurred while selecting font: {e}")
        raise e  # Re-raise the exception for further debugging


def select_font_description(driver):
    wait = WebDriverWait(driver, 20)

    try:
        # Step 1: Click the dropdown
        dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='multiselect__select'])[8]")))
        dropdown.click()

        # Step 2: Wait for the list to appear
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "multiselect__content")))

        # Step 3: Get all font options
        font_elements = driver.find_elements(By.CSS_SELECTOR, ".multiselect__element .option__title")
        font_names = [elem.text.strip() for elem in font_elements if elem.text.strip()]

        if not font_names:
            raise Exception("No fonts found in the dropdown.")

        # Step 4: Pick a random font
        selected_font = random.choice(font_names)
        print(f"Randomly selected font: {selected_font}")

        # Step 5: Wait for the input field and type the font name
        input_field = wait.until(
            EC.visibility_of_element_located((By.XPATH, "(//input[@placeholder='Select your font'])[3]")))

        # Ensure input field is cleared before typing

        # Type and select the font
        input_field.send_keys(selected_font)
        input_field.send_keys(Keys.ENTER)

        # Step 6: Close the dropdown (this might help trigger the font selection correctly)
        try:
            close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='multiselect__close']")))
            close_button.click()
        except Exception:
            print("No close button found.")



    except Exception as e:
        print(f"Error occurred while selecting font: {e}")
        raise e  # Re-raise the exception for further debugging


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
    time.sleep(2)
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Thumbnail Image']")))


def select_thumbnail_icon():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//h6[normalize-space()='alert-octagon']")))


def upload_files_orange_btn():
    return wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-view' and contains(., 'Upload Files')]")))

def upload_image_orange_btn():
    return wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-view' and contains(., 'Upload Images')]")))
def upload_video_orange_btn():
    return wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-view' and contains(., 'Upload Videos')]")))

def upload_audio_orange_btn():
    return wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-view' and contains(., 'Upload Audios')]")))

def save_new_shrub_btn():
    time.sleep(2)
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
        # Wait for overlay to disappear (if any)
        try:
            WebDriverWait(driver, 20).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "md-overlay"))
            )
        except TimeoutException:
            logger.warning("Overlay did not disappear – continuing anyway")

        # Wait for images to load
        images = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img.object-cover"))
        )

        logger.info(f"Found {len(images)} images")

        # Randomly select an image
        selected_image = random.choice(images)

        # Scroll to the selected image to bring it into view
        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", selected_image
        )

        # Click on the image using ActionChains or JS click
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
    zoom_in_button = zoom_in_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'icons')]//img[contains(@src, 'zoom-in')]"))
    )
    driver.execute_script("arguments[0].click();", zoom_in_button)
    driver.execute_script("arguments[0].scrollIntoView(true);", zoom_in_button)
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
    try:
        WebDriverWait(driver, 60).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, 'overlay-spinner-class'))
        )
    except TimeoutException:
        logger.error("Spinner did not disappear in time!")
        raise


def wait_for_overlay_to_disappear(driver):
    try:
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".md-overlay"))
        )
    except TimeoutException:
        print("Overlay still visible after waiting.")


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


def upload_random_files(relative_folder):
    folder_path = os.path.abspath(relative_folder)
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.xlsx', '.pdf', '.doc', '.pptx'))]
    if not files:
        raise Exception(f"No images found in {folder_path}")

    file_path = os.path.join(folder_path, random.choice(files))

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


def upload_random_audio(relative_folder):
    folder_path = os.path.abspath(relative_folder)
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.mp3'))]
    if not files:
        raise Exception(f"No images found in {folder_path}")

    file_path = os.path.join(folder_path, random.choice(files))

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


def upload_random_video(relative_folder):
    folder_path = os.path.abspath(relative_folder)
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.mp4'))]
    if not files:
        raise Exception(f"No images found in {folder_path}")

    file_path = os.path.join(folder_path, random.choice(files))

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
        # Wait for all shrub cards to be present
        shrub_cards = wait.until(EC.presence_of_all_elements_located((
            By.CSS_SELECTOR,
            "div.cursor-pointer.flex.flex-wrap.items-center.justify-center.rounded-lg"
        )))

        # Randomly select a shrub
        selected_shrub = random.choice(shrub_cards)

        # Scroll the selected shrub into view
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", selected_shrub)

        # Wait until the shrub is clickable
        wait.until(EC.element_to_be_clickable(selected_shrub))

        # Perform the double-click action
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
        (By.XPATH, "(//span[@class='md-list-item-text' and text()='Select your font size'])[3]")))


def select_random_alignment(driver):
    wait = WebDriverWait(driver, 20)

    # Wait until the alignment buttons are visible
    alignment_buttons = wait.until(EC.presence_of_all_elements_located((
        By.XPATH,
        "//h5[contains(text(),'Horizontal font alignment')]/following::div[contains(@class,'justify-around')]/span"
    )))

    # Filter out any elements that are hidden or not enabled
    visible_buttons = [button for button in alignment_buttons if button.is_displayed() and button.is_enabled()]

    if not visible_buttons:
        print("No visible and enabled alignment buttons found.")
        return

    # Randomly select a button from the visible ones
    random_button = random.choice(visible_buttons)

    # Scroll the button into view
    driver.execute_script("arguments[0].scrollIntoView(true);", random_button)

    # Wait until the button is clickable
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(random_button))

    # Click the button
    random_button.click()

    # Log the selected alignment
    print(f"Random alignment selected: {random_button.text}")


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
        By.XPATH, "(//div[@class='multiselect__select'])[3]"
    )))
    font_weight_dropdown.click()

    bold_option = wait.until(EC.element_to_be_clickable((
        By.XPATH, "(//span[@class='option__title'][normalize-space()='Bold'])[1]"
    )))
    bold_option.click()

    print("Bold font weight selected.")


def select_bold_font_weight_branch(driver):
    wait = WebDriverWait(driver, 10)

    font_weight_dropdown = wait.until(EC.element_to_be_clickable((
        By.XPATH, "(//div[@class='multiselect__select'])[4]"
    )))
    font_weight_dropdown.click()

    bold_option = wait.until(EC.element_to_be_clickable((
        By.XPATH, "(//span[@class='option__title'][normalize-space()='Bold'])[1]"
    )))
    bold_option.click()

    print("Bold font weight selected.")


def select_bold_font_weight_header(driver):
    wait = WebDriverWait(driver, 10)

    font_weight_dropdown = wait.until(EC.element_to_be_clickable((
        By.XPATH, "(//div[@class='multiselect__select'])[6]"
    )))
    font_weight_dropdown.click()

    bold_option = wait.until(EC.element_to_be_clickable((
        By.XPATH, "(//span[@class='option__title'][normalize-space()='Bold'])[2]"
    )))
    bold_option.click()

    print("Bold font weight selected.")


def select_bold_font_weight_description(driver):
    wait = WebDriverWait(driver, 10)

    font_weight_dropdown = wait.until(EC.element_to_be_clickable((
        By.XPATH, "(//div[@class='multiselect__select'])[9]"
    )))
    font_weight_dropdown.click()

    bold_option = wait.until(EC.element_to_be_clickable((
        By.XPATH, "(//span[@class='option__title'][normalize-space()='Bold'])[3]"
    )))
    bold_option.click()

    print("Bold font weight selected.")


def select_random_font_size(driver):
    wait = WebDriverWait(driver, 20)

    try:
        font_size_dropdown = wait.until(EC.element_to_be_clickable((
            By.XPATH, "(//div[@role='combobox'])[4]"
        )))
        font_size_dropdown.click()

        font_size_options = wait.until(EC.presence_of_all_elements_located((
            By.XPATH, "//li[@class='multiselect__element']"
        )))

        if not font_size_options:
            print("No font size options found!")
            return

        random_option = random.choice(font_size_options)
        print(f"Randomly selected font size: {random_option.text}")

        random_option.click()

    except TimeoutException:
        print("TimeoutException: Could not load font size options.")
    except NoSuchElementException:
        print("NoSuchElementException: Could not find the font size dropdown or options.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


def select_random_font_size_branch(driver):
    wait = WebDriverWait(driver, 20)

    try:
        font_size_dropdown = wait.until(EC.element_to_be_clickable((
            By.XPATH, "(//div[@role='combobox'])[5]"
        )))
        font_size_dropdown.click()

        font_size_options = wait.until(EC.presence_of_all_elements_located((
            By.XPATH, "//li[@class='multiselect__element']"
        )))

        if not font_size_options:
            print("No font size options found!")
            return

        random_option = random.choice(font_size_options)
        print(f"Randomly selected font size: {random_option.text}")

        random_option.click()

    except TimeoutException:
        print("TimeoutException: Could not load font size options.")
    except NoSuchElementException:
        print("NoSuchElementException: Could not find the font size dropdown or options.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


def select_random_header_font_size(driver):
    wait = WebDriverWait(driver, 20)

    try:
        font_size_dropdown = wait.until(EC.element_to_be_clickable((
            By.XPATH, "(//div[@role='combobox'])[7]"
        )))
        font_size_dropdown.click()

        font_size_options = wait.until(EC.presence_of_all_elements_located((
            By.XPATH, "//li[@class='multiselect__element']"
        )))

        if not font_size_options:
            print("No font size options found!")
            return

        random_option = random.choice(font_size_options)
        print(f"Randomly selected font size: {random_option.text}")

        random_option.click()

    except TimeoutException:
        print("TimeoutException: Could not load font size options.")
    except NoSuchElementException:
        print("NoSuchElementException: Could not find the font size dropdown or options.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


def select_random_description_font_size(driver):
    wait = WebDriverWait(driver, 20)

    try:
        font_size_dropdown = wait.until(EC.element_to_be_clickable((
            By.XPATH, "(//div[@role='combobox'])[10]"
        )))
        font_size_dropdown.click()

        font_size_options = wait.until(EC.presence_of_all_elements_located((
            By.XPATH, "//li[@class='multiselect__element']"
        )))

        if not font_size_options:
            print("No font size options found!")
            return

        random_option = random.choice(font_size_options)
        print(f"Randomly selected font size: {random_option.text}")

        random_option.click()

    except TimeoutException:
        print("TimeoutException: Could not load font size options.")
    except NoSuchElementException:
        print("NoSuchElementException: Could not find the font size dropdown or options.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


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


def select_description_color_picker_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "(//img[contains(@src, 'color-picker')])[4]")))


def select_background_image_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//img[contains(@src, 'background-image')]")))


def select_icon_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH,
                                                  "//img[@alt='thumbnail' and contains(@src, 'tick.b42a347e.svg')]")))


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
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "overlay-spinner")))
    return wait.until(EC.element_to_be_clickable((By.XPATH,
                                                  "(//button[contains(@class, 'md-button') and .//div[@class='md-button-content' and text()=' Save ']])[2]")))


def new_branch_btn():
    WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.ID, "overlay-spinner")))
    time.sleep(5)
    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-new-branch']")))


def save_as_template_btn():
    save_template = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Save As Template')]")))
    save_template.click()

    input = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class, 'md-field')]//input[@class='md-input'])[5]")))
    input.send_keys(input_field.VALID_SHRUBS)

    save = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[contains(., 'Save')])[5]")))
    save.click()


def save_as_template_btn_branch():
    save_template = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Save As Template')]")))
    save_template.click()

    input = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class, 'md-field')]//input[@class='md-input'])[1]")))
    input.send_keys(input_field.VALID_SHRUBS)

    save = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[contains(., 'Save')])[3]")))
    save.click()


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
    return wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[contains(., 'Save')])[2]")))


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
    wait_for_overlay_to_disappear(driver)  # Ensure any overlay is gone

    return WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-save' and contains(., 'Save')]")))


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
    wait_for_overlay_to_disappear(driver)
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-save' and contains(., 'Back')]")))


def bank_branch_btn():
    progress_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-save' and contains(., 'Back')]")))


def back_code_btn():
    progress_spinner()
    return wait.until(EC.element_to_be_clickable((By.XPATH, "// button[ @ name = 'btn-save' and contains(., 'Back')]")))


def back_link_btn():
    wait_for_overlay_to_disappear(driver)
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='btn-save' and contains(., 'Back')]")))


def wait_time():
    return time.sleep(5)


def switch_to_window(driver, window_index=0):
    windows = driver.window_handles
    if windows:
        driver.switch_to.window(windows[window_index])  # Switch to the first window
    else:
        raise Exception("No windows are open.")

shrub_name = ""
def random_select_and_click_image_and_delete(driver, image_selector, delete_button_xpath, shrub_xpath, scroll_by=300):
    WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, image_selector)))
    images = driver.find_elements(By.CSS_SELECTOR, image_selector)
    if not images:
        raise Exception(f"No images found with the selector: {image_selector}")

    random_image = random.choice(images)
    driver.execute_script("arguments[0].scrollIntoView();", random_image)
    time.sleep(1)
    ActionChains(driver).move_to_element(random_image).click().perform()
    driver.execute_script(f"window.scrollBy(0, {scroll_by});")

    # Find all shrub names using the dynamic XPath
    shrub_elements = driver.find_elements(By.XPATH, shrub_xpath)
    if not shrub_elements:
        raise Exception("No shrub names found.")

    # Randomly select a shrub name
    random_shrub = random.choice(shrub_elements)
    shrub_name = random_shrub.text.strip()
    print(f"Randomly selected shrub name: {shrub_name}")

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, delete_button_xpath)))
    delete_button = driver.find_element(By.XPATH, delete_button_xpath)
    delete_button.click()

def random_select_search_and_click_shrub(driver, image_selector, search_input_selector, shrub_xpath,scroll_by=300):
    # Wait for images to load and get all the image elements
    WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, image_selector)))
    images = driver.find_elements(By.CSS_SELECTOR, image_selector)
    if not images:
        raise Exception(f"No images found with the selector: {image_selector}")

    # Select a random image and perform an action on it
    random_image = random.choice(images)
    driver.execute_script("arguments[0].scrollIntoView();", random_image)
    time.sleep(1)
    ActionChains(driver).move_to_element(random_image).click().perform()
    driver.execute_script(f"window.scrollBy(0, {scroll_by});")

    # Find all shrub elements after the search
    shrub_elements = driver.find_elements(By.XPATH, shrub_xpath)
    if not shrub_elements:
        raise Exception("No shrubs found after searching.")

    # Randomly select a shrub from the search results
    random_shrub = random.choice(shrub_elements)
    shrub_name = random_shrub.text.strip()
    print(f"Randomly selected shrub name: {shrub_name}")
    # Search for the shrub using the provided search query
    search_input = driver.find_element(By.XPATH, search_input_selector)
    search_input.send_keys(shrub_name)
    time.sleep(2)  # Wait for the results to load



    # Scroll to the selected shrub and click it
    driver.execute_script("arguments[0].scrollIntoView();", random_shrub)
    time.sleep(1)
    ActionChains(driver).move_to_element(random_shrub).click().perform()
    # time.sleep(3)
    # select_btn = driver.find_element(By.XPATH, shrub_xpath)
    # ActionChains(driver).move_to_element(select_btn).click().perform()


    print(f"Action performed on shrub: {shrub_name}")

def three_dots_button():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "// div[ @class ='flex justify-end three-dots'] / img[@ class ='action-icon-color']")))

def share_shrub_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Share')]")))

def share_dropdown():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "// div[@class ='multiselect__select']")))

def select_input_field():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='users' and @type='text' and @class='multiselect__input']")))
def checkbox_select():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='multiselect__option multiselect__option--highlight multiselect__option--selected']")))

def send_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Send')]")))



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
            wait_time()
            WebDriverWait(driver, 30).until(EC.url_contains("analytics"))

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
        overlay_spinner()
        wait_time()
        get_my_shrubs().click()

        WebDriverWait(driver, 30).until(
            EC.invisibility_of_element_located((By.ID, "overlay-spinner"))
        )
        logger.info("Overlay spinner disappeared after navigating to 'My Shrubs'")


    def test_search_shrubs(self):
        wait_time()
        # Define the selectors
        image_selector = 'img.action-icon-color'  # Update to the correct image selector
        search_input_selector = "//input[@placeholder='Search' and @class='md-input']"
        shrub_xpath = "//h5[contains(@class, 'title')]"  # XPath for shrub names
        random_select_search_and_click_shrub(driver, image_selector, search_input_selector, shrub_xpath)
        wait_time()
        three_dots_button().click()
        share_shrub_btn().click()
        share_dropdown().click()
        select_input_field().send_keys("testp567@yopmail.com")
        select_view_only_permissions().click()
        select_view_only_permissions().click()
        select_allow_resharing_permissions().click()
        select_download_save_permissions().click()
        checkbox_select().click()
        send_btn().click()




