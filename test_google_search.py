import pytest
from page_objects.google_start_page import GooglePage


@pytest.fixture()
def browser(chrome_driver):
    google_page = GooglePage(chrome_driver)
    google_page.go_to_site()
    return google_page


@pytest.mark.parametrize("text_to_search", ["найдется всё", "latest fashion trends"])
def test_google_search_sample(browser, text_to_search):
    # fill search
    search_field = browser.fill_search_field(text_to_search)
    assert text_to_search == search_field.get_attribute("value")

    # do search
    browser.press_enter_in_element(search_field)

    # check for open search page
    assert text_to_search in browser.get_title()

    # check for available search results
    assert browser.is_search_results_available()


@pytest.mark.parametrize("text_to_search", ["-12", "!#@$"])
def test_google_negative_search_cases(browser, text_to_search):
    # fill search
    search_field = browser.fill_search_field(text_to_search)
    assert text_to_search == search_field.get_attribute("value")

    # do search
    browser.press_enter_in_element(search_field)

    # check for open search page
    assert text_to_search in browser.get_title()

    # check for no search results
    assert not browser.is_search_results_available()


