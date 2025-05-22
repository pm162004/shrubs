import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WEB_URL = "https://app.dev-shrubs.com/"
CORRECT_EMAIL = "testp679@yopmail.com"
CORRECT_PASSWORD = "Test@123"

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(WEB_URL)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 20)

def test_fill_shrub_form(driver, wait):
    # --- Login ---
    wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys(CORRECT_EMAIL)
    wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(CORRECT_PASSWORD)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]"))).click()

    # --- Wait for dashboard/home ---
    wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Dashboard') or contains(text(),'Projects')]")))

    # Navigate to form if needed (depends on app flow)
    # Example: wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='New Shrub']"))).click()

    # --- Fill Shrub Form ---
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Shrub Title']"))).send_keys("My Automation Test Shrub")

    # Checkbox: Show Title (already checked, skip or validate)
    # Optional: toggle off then on again for test
    title_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(.,'Do you want to show the title?')]/preceding-sibling::input")))
    if not title_checkbox.is_selected():
        title_checkbox.click()

    # Fill Sub Header
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Sub Header']"))).send_keys("This is a sub header")

    # Fill Description
    wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Enter text here']"))).send_keys("Automated description input.")

    # Permissions: Check View Only and Resharing
    for label in ["View Only", "Allow Resharing"]:
        checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, f"//label[contains(.,'{label}')]/preceding-sibling::input")))
        if not checkbox.is_selected():
            checkbox.click()

    # Show Thumbnail: Already checked
    thumb_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(.,'Do you want to show thumbnail?')]/preceding-sibling::input")))
    if not thumb_checkbox.is_selected():
        thumb_checkbox.click()

    # Select Thumbnail Type: Shrub Project Icon
    wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(.,'Shrub Project Icon')]/preceding-sibling::input"))).click()

    # Save
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Save']"))).click()

    # Optional: Verify success message
    success = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Shrub saved') or contains(text(),'successfully')]")))
    assert success.is_displayed(), "Shrub creation failed or no confirmation shown"
