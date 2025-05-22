import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Constants
WEB_URL = "https://app.dev-shrubs.com/"
CORRECT_EMAIL = "testp679@yopmail.com"
CORRECT_PASSWORD = "Test@123"

# Setup
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.maximize_window()
wait = WebDriverWait(driver, 20)

def login():
    driver.get(WEB_URL)
    wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(CORRECT_EMAIL)
    wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(CORRECT_PASSWORD)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='My Shrubs']")))

def navigate_to_new_shrub():
    wait.until(EC.element_to_be_clickable((By.XPATH, "//p[normalize-space()='My Shrubs']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'New Shrub')]"))).click()

def fill_shrub_form():
    wait.until(EC.presence_of_element_located((By.NAME, "shrub-name"))).send_keys("Automation Test Shrub")

    title_checkbox = wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(.,'Do you want to show the title?')]/preceding-sibling::input")))
    if not title_checkbox.is_selected():
        title_checkbox.click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Sub Header']"))).send_keys("Auto Subheader")
    wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Enter text here']"))).send_keys("This shrub was created via Selenium test script.")

    for permission in ["View Only", "Allow Resharing"]:
        checkbox = wait.until(EC.presence_of_element_located((By.XPATH, f"//label[contains(.,'{permission}')]/preceding-sibling::input")))
        if not checkbox.is_selected():
            checkbox.click()

    thumbnail_checkbox = wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(.,'Do you want to show thumbnail?')]/preceding-sibling::input")))
    if not thumbnail_checkbox.is_selected():
        thumbnail_checkbox.click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Shrub Project Icon']/preceding-sibling::input"))).click()

def select_thumbnail_image_btn():
    return wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='cursor-pointer relative box-square-50 profile-bg br6']")))

def upload_image_from_my_files():
    # Click the 'My Files' tab
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='My Files']"))).click()

    # Wait and click the first file in the list (screenshot thumbnail)
    wait.until(EC.element_to_be_clickable((
        By.XPATH, "//div[contains(@class, 'md-image-preview') or contains(@class, 'md-list-item')]"
    ))).click()

    # Click the Save/OK button
    wait.until(EC.element_to_be_clickable((
        By.XPATH, "//button[.//div[normalize-space()='Save'] or normalize-space()='OK']"
    ))).click()

    # Wait for upload confirmation toast (optional)
    wait.until(EC.presence_of_element_located((
        By.XPATH, "//div[contains(text(),'Uploads completed') or @class='text-success']"
    )))
    print("✅ File selected and uploaded from My Files.")

def submit_form():
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Save']"))).click()
    try:
        success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Shrub saved')]")))
        print("✅ Shrub saved successfully.")
    except:
        print("❌ Shrub creation might have failed.")

def test_create_shrub():
    login()
    navigate_to_new_shrub()
    fill_shrub_form()
    select_thumbnail_image_btn().click()
    upload_image_from_my_files()
    submit_form()
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    test_create_shrub()