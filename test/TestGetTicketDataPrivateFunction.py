from unittest import TestCase
from ticket.GetTicketDataPrivateFunction import GetTicketDataPrivateFunction


class TestGetTicketData(TestCase):
    def setUp(self):
        self.url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"
        self.ticket_data = GetTicketDataPrivateFunction()
        self.target_page = self.ticket_data.open_target_page(target_url=self.url)

    def test_station_code(self):
        target_url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"
        station_code = self.ticket_data.get_station_code(target_url, "成都")
        self.assertEqual(station_code, "CDW")
