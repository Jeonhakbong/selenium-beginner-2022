# selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class GoogleKeywordScreenShooter:
    def __init__(self, keyword, screeshots_dir):  # constructor.
        self.set_options()
        self.browser = webdriver.Chrome(
            ChromeDriverManager().install(), options=self.options
        )  # set browser.
        self.keyword = keyword
        self.screenshots_dir = screeshots_dir

    def set_options(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option(
            "excludeSwitches", ["enable-logging"]
        )  # handling usb device error.
        self.options.add_experimental_option("detach", True)  # option to be kept open.

    def start(self):
        self.browser.get("https://google.com")  # get browser.

        # input keyword.
        search_bar = self.browser.find_element_by_class_name("gLFyf")
        search_bar.send_keys(self.keyword)  # type hello on search bar.
        search_bar.send_keys(Keys.ENTER)  # press enter.

        # selenium wait until class="ULSxyf" located on browser.
        except_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ULSxyf"))
        )

        # can excecute js command and send arguments by using excute_script().
        # browser.execute_script("alert('hello')")
        self.browser.execute_script(
            """
            const except = arguments[0]
            except.parentElement.removeChild(except)
            """,
            except_element,
        )

        # find search results.
        search_box = self.browser.find_element_by_id("search")
        search_results = search_box.find_elements_by_class_name("g")  # return list.

        for index, search_result in enumerate(search_results):
            search_result.screenshot(
                f"{self.screenshots_dir}/{self.keyword}x{index}.png"
            )

    def finish(self):
        self.browser.quit()


domain_competitors = GoogleKeywordScreenShooter("buy domain", "screenshots")
domain_competitors.start()
domain_competitors.finish()

python_competitors = GoogleKeywordScreenShooter("python book", "screenshots")
python_competitors.start()
python_competitors.finish()
