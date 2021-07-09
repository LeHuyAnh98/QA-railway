class BooktickerPage():
    textbox_Depart_date_name = "Date"
    textbox_Depart_from_name = "DepartStation"
    textbox_Arrive_name = "ArriveStation"
    textbox_Seat_type_name = "SeatType"
    textbox_Ticket_name = "TicketAmount"
    button_Book_ticket_xpath = "//body/div[@id='page']/div[@id='content']/div[1]/form[1]/fieldset[1]/input[1]"
    button_Book_ticketpg_xpath = "//span[contains(text(),'Book ticket')]"

    def __init__(self,driver):
        self.driver=driver

    def setDepartDate(self, Date):
            self.driver.find_element_by_name(self.textbox_Depart_date_name).clear()
            self.driver.find_element_by_name(self.textbox_Depart_date_name).send_keys(Date)

    def setDepartName(self, DepartStation):
        self.driver.find_element_by_name(self.textbox_Depart_from_name).clear()
        self.driver.find_element_by_name(self.textbox_Depart_from_name).send_keys(DepartStation)

    def setArriveName(self, ArriveStation):
        self.driver.find_element_by_name(self.textbox_Depart_from_name).clear()
        self.driver.find_element_by_name(self.textbox_Depart_from_name).send_keys(ArriveStation)

    def setSeatType(self, SeatType):
        self.driver.find_element_by_name(self.textbox_Depart_from_name).clear()
        self.driver.find_element_by_name(self.textbox_Depart_from_name).send_keys(SeatType)

    def setTicketName(self, TicketAmount):
        self.driver.find_element_by_name(self.textbox_Depart_from_name).clear()
        self.driver.find_element_by_name(self.textbox_Depart_from_name).send_keys(TicketAmount)

    def clickBookticket(self):
        self.driver.find_element_by_xpath(self.button_Book_ticket_xpath).click()

    def clickBookticketPG(self):
        self.driver.find_element_by_xpath(self.button_Book_ticketpg_xpath).click()

