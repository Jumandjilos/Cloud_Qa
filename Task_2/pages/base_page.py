from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait as webdw, WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find_elem(self, locator, time=10):
        try:
            element = webdw(self.browser, time).until(
                ec.presence_of_element_located(locator),
                message=f"Отсутствует возможность найти локатор {locator}"
            )
            return element
        except TimeoutException as e:
            print(e.msg)
            pass

    def new_window(self, browser):
        return self.browser.switch_to.window(browser.window_handles[1])

    def title_is_change(self,browser, word):
        title = WebDriverWait(browser, 5).until(ec.title_contains(word))
        return title

    def scroll(self, btn):
        return self.browser.execute_script("return arguments[0].scrollIntoView(true);", btn)

    def get_page_url(self) -> str:
        return self.browser.current_url

    def open(self, url):
        return self.browser.get(url)