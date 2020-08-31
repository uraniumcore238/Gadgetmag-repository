from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MainPageObject:
    def __init__(self, driver):
        self.driver = driver

    MAIN_BANNER_LOCATOR = (By.XPATH, "//div[@id='main-menu-block']//span[@class='main-logo']")
    ALL_MENU_ELEMENTS_LOCATOR = (By.XPATH, "//div[@id='main-menu-block']/ul[@class='nav navbar-nav main-nav']/li")
    H1_LOCATOR = (By.XPATH, "//body/div[@class='site-wrapper']/div[@class='site-content']//h1")


    def waiting_for_main_page(self):
        main_banner = WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located((MainPageObject.MAIN_BANNER_LOCATOR)))

    def find_all_menu_points(self):
        string_set = self.driver.find_elements(*MainPageObject.ALL_MENU_ELEMENTS_LOCATOR)
        return string_set

    def click_on_maim_menu_point(self):
        title_text = WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((MainPageObject.H1_LOCATOR))
        title_name = title_text.text()






