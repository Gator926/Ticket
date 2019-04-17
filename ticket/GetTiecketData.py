from selenium import webdriver
from selenium.webdriver import ActionChains


class GetTicketData:
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)
        self.high_speed_list = ["G", "D"]

    def __del__(self):
        self.browser.close()

    def open_target_page(self, target_url):
        self.browser.get(target_url)
        return self.browser

    def input_station(self, station_type, station_name):
        if station_type == "start":
            self.__put_input_value("fromStationText", station_name)
            self.__select_specific_station(station_name)
        elif station_type == "end":
            self.__put_input_value("toStationText", station_name)
            self.__select_specific_station(station_name)
        else:
            print("非法车站类型, 可用值: start|end")
            raise ValueError

    def input_date(self, date):
        self.__remove_attribute("train_date", "readonly")
        self.browser.find_element_by_id("train_date").clear()
        self.__put_input_value("train_date", date)

    def only_high_speed(self):
        elements = self.browser.find_element_by_id("cc_train_type_btn_all").find_elements_by_tag_name("input")
        for each in elements:
            if each.get_attribute("value") in self.high_speed_list:
                each.click()

    def click_button_by_id(self, element_id):
        self.browser.find_element_by_id(element_id).click()

    def __select_specific_station(self, station_name):
        city_sets = self.browser.find_element_by_id("panel_cities").find_elements_by_tag_name('div')
        for each in city_sets:
            if each.text.split("\n")[0] == station_name:
                each.click()
                break

    def __remove_attribute(self, element_id, attribute):
        js = "document.getElementById(\"%s\").removeAttribute(\"%s\")" % (element_id, attribute)
        self.browser.execute_script(js)

    def __put_input_value(self, element_id, value):
        ActionChains(self.browser).send_keys_to_element(self.browser.find_element_by_id(element_id), value).perform()
