import time

from PageObjects.HintCityPageObject import HintCityPageObject
from PageObjects.main_page_object import MainPageObject
from Utilities.base_class import BaseClass




class TestOrder(BaseClass):

    def test_order_one(self):
        hintCityPageObject = HintCityPageObject(self.driver)
        hintCityPageObject.wait_for_pop_up()
        print("Pop-up is appeared")
        main_page_object=hintCityPageObject.click_on_button('Да')
        # hintCityPageObject.wait_for_invisibility_pop_up
        # print('Pop-up is desapeared')
        # main_page_object = MainPageObject(self.driver)
        main_page_object.waiting_for_main_page()
        print("Site is opened")

        string_set = main_page_object.find_all_menu_points()
        print("All menu points was found")
        for element in string_set:
            text = element.text
            print(text)
            if text == 'Частным лицам':
                element.click()
                break
            else:
                continue
        time.sleep(10)

