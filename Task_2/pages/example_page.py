from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ExampleLocator:
    more_information = (By.CSS_SELECTOR, "a[href='https://www.iana.org/domains/example']")

class ExamplePage(BasePage):
    def __init__(self,browser):
        super().__init__(browser)

    def open_example(self):
        return self.open("https://example.com")

    def information(self):
        return self.find_elem(ExampleLocator.more_information)

    def information_click(self):
        return self.information().click()

    def get_page_url(self) -> str:
        return self.browser.current_url