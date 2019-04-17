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
        """
        打开目标页面
        :param target_url: 目标页面
        :return:
        """
        self.browser.get(target_url)
        return self.browser

    def input_station(self, station_type, station_name):
        """
        输入车站
        :param station_type: 车站类型, 可用值: start|end
        :param station_name: 车站名称
        :return:
        """
        if station_type == "start":
            element_id = "fromStationText"
        elif station_type == "end":
            element_id = "toStationText"
        else:
            print("非法车站类型, 可用值: start|end")
            raise ValueError
        self.__put_input_value(element_id, station_name)
        self.__select_specific_station(station_name)

    def input_date(self, date):
        """
        输入日期
        :param date: 日期(2019-01-01)
        :return:
        """
        self.__remove_attribute("train_date", "readonly")
        self.browser.find_element_by_id("train_date").clear()
        self.__put_input_value("train_date", date)

    def only_high_speed(self):
        """
        是否仅选择高铁
        :return:
        """
        elements = self.browser.find_element_by_id("cc_train_type_btn_all").find_elements_by_tag_name("input")
        for each in elements:
            if each.get_attribute("value") in self.high_speed_list:
                each.click()

    def click_button_by_id(self, element_id):
        """
        点击查询按钮
        :param element_id: 查询按钮的元素id
        :return:
        """
        self.browser.find_element_by_id(element_id).click()

    def __select_specific_station(self, station_name):
        """
        在输入车站时, 选择指定的车站
        :param station_name: 车站名
        :return:
        """
        city_sets = self.browser.find_element_by_id("panel_cities").find_elements_by_tag_name('div')
        for each in city_sets:
            if each.text.split("\n")[0] == station_name:
                each.click()
                break

    def __remove_attribute(self, element_id, attribute):
        """
        去除元素的某个属性
        :param element_id: 元素的id
        :param attribute:  待去除的属性
        :return:
        """
        js = "document.getElementById(\"%s\").removeAttribute(\"%s\")" % (element_id, attribute)
        self.browser.execute_script(js)

    def __put_input_value(self, element_id, value):
        """
        文本框模拟键盘输入
        :param element_id: 文本框元素的id
        :param value:      文本框待输入的值
        :return:
        """
        ActionChains(self.browser).send_keys_to_element(self.browser.find_element_by_id(element_id), value).perform()
