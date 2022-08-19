from selenium import webdriver

driver = webdriver.Safari()
driver.get("https://www.leetcode.com")

sign_in_button = driver.find_element("xpath", '//a[@href="/accounts/login/"]')

# TODO:
#   complete sign in
#   navigate to problem types page
#   gather all problem names 
#   from all the names, gather all descriptions
#   create SQL db to store data



driver.execute_script("arguments[0].click();", sign_in_button);
