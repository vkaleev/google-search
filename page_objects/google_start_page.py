from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

SEARCH_INPUT_FIELD = (By.CSS_SELECTOR, 'input[name="q"]')
BUTTON_SEARCH = (By.CSS_SELECTOR, 'input[name="btnK"]')
SEARCH_RESULTS_STATS = (By.ID, 'result-stats')


class GooglePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://google.com/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def fill_search_field(self, text):
        search_field = self.find_element(SEARCH_INPUT_FIELD)
        search_field.click()
        search_field.send_keys(text)
        return search_field

    def do_search(self, text):
        search_field = self.find_element(SEARCH_INPUT_FIELD)
        search_field.click()
        search_field.send_keys(text)
        search_field.send_keys(Keys.ENTER)
        return search_field

    def press_enter_in_element(self, element):
        element.send_keys(Keys.ENTER)
        return element

    def get_title(self):
        return self.driver.title

    def is_search_results_available(self):
        try:
            self.find_element(SEARCH_RESULTS_STATS)
            return True
        except Exception as e:
            return False

