from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]').text
print(articles_count)

# talk_link = driver.find_element(By.LINK_TEXT, "Talk")
# talk_link.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
# search.submit()
search.send_keys(Keys.ENTER)

driver.quit()
