from task_2.pages.example_page import ExamplePage
import pytest

@pytest.mark.xfail(reason="Не до конца понятное условие шага", strict=False)
def test(browser):
    example_page = ExamplePage(browser)
    example_page.open_example()
    assert example_page.title_is_change(browser, 'Example') == True, "Заголовок страницы отличается от Example"
    example_page.information_click()
    assert example_page.get_page_url() == "https://www.iana.org/domains/example" , \
        'URL страницы отличается от ожидаемого'
    # Из-за не до конца понятного условия по перенаправлению на страницу с URL "https://www.iana.org/domains/example".
    # Промаркировал тест как ignored