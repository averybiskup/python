from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.slither.io")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# # elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source

# driver.findElement(By.linkText('play')).click()
driver.find_element_by_css_selector('div.btnt.nsi.sadg1').click()
time.sleep(3)
game = driver.find_element_by_css_selector('body')


time.sleep(30)
driver.close()
