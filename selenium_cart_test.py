from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# Setup
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Add first product to cart
driver.find_element(By.CLASS_NAME, "btn_inventory").click()

# Wait for the cart badge to appear
try:
    cart_count = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    ).text
    print("Cart count found:", cart_count)
    assert cart_count == "1", "Cart count is not correct!"
    print("Test Passed: Item successfully added to cart.")
except TimeoutException:
    print("Cart badge did not appear within 10 seconds.")
except NoSuchElementException:
    print("Could not locate the cart badge element.")
finally:
    time.sleep(2)  # Just to visually confirm before closing
    driver.quit()
