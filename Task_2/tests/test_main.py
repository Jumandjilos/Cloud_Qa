from pages.example_page import ExamplePage
from tests import conftest


def test(browser):
    example_page = ExamplePage(browser)
    example_page.open_example()
    assert example_page.title_is_change(browser, 'Example') == True
    example_page.information_click()
    assert example_page.get_page_url() == "https://www.iana.org/domains/example"