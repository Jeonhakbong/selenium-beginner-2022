# selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


KEYWORD = "buy domain"  # key word we want to search.

options = webdriver.ChromeOptions()
options.add_experimental_option(
    "excludeSwitches", ["enable-logging"]
)  # handling usb device error.
options.add_experimental_option("detach", True)  # option to be kept open.

browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
browser.get("https://google.com")

search_bar = browser.find_element_by_class_name("gLFyf")

search_bar.send_keys(KEYWORD)  # type hello on search bar.
search_bar.send_keys(Keys.ENTER)  # press enter.

# selenium wait until class="g" located on browser.
shitty_element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "g"))
)

# find search results.
search_box = browser.find_element_by_id("search")
search_results = search_box.find_elements_by_class_name("g")

for index, search_result in enumerate(search_results):
    title = search_result.find_element_by_tag_name("h3")
    class_name = search_result.get_attribute("class")
    if len(title.text) > 0:
        search_result.screenshot(f"screenshots/{KEYWORD}x{index}.png")

browser.quit()
