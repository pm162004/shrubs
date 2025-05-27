import time,os,datetime
from selenium import webdriver
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
    return wait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='My Shrubs']")))


def get_new_shrub():
    time.sleep(5)
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='md-button-content' and text()='New Shrub']")))


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
        quit_browser()

def test_my_shrubs():
    logger.info("Navigating to My Shrubs")
    get_my_shrubs().click()
    get_new_shrub().click()
    logger.info("Clicked on new shrub button")
