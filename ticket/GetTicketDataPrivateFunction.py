from ticket.GetTiecketData import GetTicketData


class GetTicketDataPrivateFunction(GetTicketData):

    @staticmethod
    def get_station_code(target_url, station_name):
        ticket_data = GetTicketData()
        ticket_data.open_target_page(target_url)
        ticket_data.input_station("start", station_name)
        station_code = ticket_data.browser.find_element_by_id("fromStation").get_attribute("value")
        return station_code
