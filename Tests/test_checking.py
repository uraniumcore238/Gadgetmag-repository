import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestOne:

    print("2222222222222222222222222222")


    def test_e2e(self):
        driver = webdriver.Chrome(executable_path="D:\\Programming\\Gadgetmag\\Sourse\\chromedriver.exe")
        driver.get("https://www.gadgetmag.su/")
        driver.maximize_window()
        print("22222222222222222222222222222222222222222222222")

        # MAIN_BANNER_LOCATOR = (By.XPATH, "//div[@id='page']/section/div[@class='main-slider-banner lapping']")
        main_banner = WebDriverWait(driver, 22).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='page']/section/div[@class='main-slider-banner lapping']")))

        print("2222222222222222222222222222222222222222")
        time.sleep(22)
        driver.close()
        driver.quit()