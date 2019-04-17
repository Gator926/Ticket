import time
from unittest import TestCase
from ticket.GetTiecketData import GetTicketData


class TestGetTicketData(TestCase):
    def setUp(self):
        self.url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"
        self.tag = "table"
        self.date = "2019-05-01"
        self.ticket_data = GetTicketData()
        self.target_page = self.ticket_data.open_target_page(target_url=self.url)

    def test_open_url(self):
        page_title = self.target_page.title
        self.assertIn("中国铁路12306", page_title)

    def test_input_start_station(self):
        self.ticket_data.input_station("start", "成都")
        input_value = self.target_page.find_element_by_id("fromStationText").get_attribute("value")
        self.assertEqual("成都", input_value)

    def test_input_date(self):
        self.ticket_data.input_date(self.date)
        attribute = self.ticket_data.browser.find_element_by_id("train_date").get_attribute("value")
        self.assertEqual(self.date, attribute)

    def test_only_high_speed(self):
        self.ticket_data.only_high_speed()
        elements = self.ticket_data.browser.find_element_by_id("cc_train_type_btn_all").find_elements_by_tag_name(
            "input")
        number = 0
        for each in elements:
            if each.is_selected():
                number += 1
        self.assertEqual(number, 2)

    def test_before_click_query_button(self):
        elements = self.ticket_data.browser.find_element_by_id("queryLeftTable").find_elements_by_tag_name("tr")
        self.assertEqual(len(elements), 0)

    def test_after_click_query_button(self):
        self.ticket_data.input_station("start", "成都")
        self.ticket_data.input_station("end", "广元")
        self.ticket_data.input_date(self.date)
        self.ticket_data.only_high_speed()
        self.ticket_data.click_button_by_id("query_ticket")
        time.sleep(10)
        elements = self.ticket_data.browser.find_element_by_id("queryLeftTable").find_elements_by_tag_name("tr")
        self.assertGreater(len(elements), 0)
