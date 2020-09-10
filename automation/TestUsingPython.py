from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

# driver = webdriver.Chrome("C:/Users/muku3/tools/web-driver/chromedriver.exe")
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

# This example requires Selenium WebDriver 3.13 or newer
with webdriver.Chrome("C:/Users/muku3/tools/web-driver/chromedriver.exe") as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://google.com/ncr")
    assert "Google" in driver.title
    driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
    first_result = wait.until(presence_of_element_located(By.CSS_SELECTOR))
    print(first_result.get_attribute("textContent"))
