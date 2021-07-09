class MyTicketPage():
    def __init__(self, driver):
        self._driver = driver

    def clickMyticketPG(self):
        self.driver.find_element_by_xpath(self.button_My_ticketpg_xpath).click()