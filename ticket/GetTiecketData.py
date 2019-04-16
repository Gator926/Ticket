from selenium import webdriver


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
        elif station_type == "end":
            self.__put_input_value("toStationText", station_name)
        else:
            print("非法车站类型, 可用值: start|end")
            raise ValueError

    def input_date(self, date):
        self.__remove_attribute("train_date", "readonly")
        self.__put_input_value("train_date", date)

    def only_high_speed(self):
        elements = self.browser.find_element_by_id("cc_train_type_btn_all").find_elements_by_tag_name("input")
        for each in elements:
            if each.get_attribute("value") in self.high_speed_list:
                each.click()

    def click_button_by_id(self, element_id):
        self.browser.find_element_by_id(element_id).click()

    def __remove_attribute(self, element_id, attribute):
        js = "document.getElementById(\"%s\").removeAttribute(\"%s\")" % (element_id, attribute)
        self.browser.execute_script(js)

    def __put_input_value(self, element_id, value):
        self.browser.find_element_by_id(element_id).clear()
        self.browser.find_element_by_id(element_id).send_keys(value)
