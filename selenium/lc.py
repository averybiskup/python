from selenium import webdriver

driver = webdriver.Safari()
driver.get("https://www.leetcode.com")

sign_in_button = driver.find_element("xpath", '//a[@href="/accounts/login/"]')

driver.execute_script("arguments[0].click();", sign_in_button);
