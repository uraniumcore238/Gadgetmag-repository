from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects import main_page_object
from PageObjects.main_page_object import MainPageObject


class HintCityPageObject:
    def __init__(self, driver):
        self.driver = driver

    ALL_BUTTONS = (By.CSS_SELECTOR, ".navbar-nav .hint-city__btns [type='button']")
    POP_UP_ELEMENT = (By.CSS_SELECTOR, ".navbar-nav .hint-city")

    def click_on_button(self, button_name):
        set_of_buttons = self.driver.find_elements(*HintCityPageObject.ALL_BUTTONS)
        for element in set_of_buttons:
            name_of_the_button = element.text
            print(name_of_the_button)
            if name_of_the_button == button_name:
                element.click()
                main_page_object = MainPageObject(self.driver)
                return main_page_object
                break
            else:
                continue

    def wait_for_pop_up(self):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located(HintCityPageObject.POP_UP_ELEMENT))

    def wait_for_invisibility_pop_up(self):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.invisibility_of_element_located(HintCityPageObject.POP_UP_ELEMENT))
