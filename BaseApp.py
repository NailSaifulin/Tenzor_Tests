from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://sbis.ru/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def visibility_of_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                      message=f"Element not visible {locator}")

    def visibility_of(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of(locator),
                                                      message=f"Element not visible {locator}")

    def element_to_be_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                      message=f"The element is not clickable {locator}")

    def invisibility_of_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator),
                                                      message=f"The element is visible {locator}")

    def go_to_site(self):
        self.driver.maximize_window()
        return self.driver.get(self.base_url)

    def switch_window(self, number):
        list_handles = self.driver.window_handles[number]
        return self.driver.switch_to.window(list_handles)

    def move_to(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()
        return actions

    def information_fields(self):
        fields_list = [self.driver.title, self.driver.current_url]
        return fields_list

    # def wait_pageload(self, time=10):
        # return WebDriverWait(self.driver, time).until(lambda driver:
        #                                               driver.execute_script('return document.readyState') == 'complete')


