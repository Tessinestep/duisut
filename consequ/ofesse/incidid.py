from selenium.webdriver import Chrome
from selenium.webdriver.common.alert import Alert

driver = Chrome()
driver.get("http://example.com")

# Click a button that triggers an alert
driver.find_element_by_id("trigger_alert").click()

# Accept the alert
alert = Alert(driver)
alert.accept()
