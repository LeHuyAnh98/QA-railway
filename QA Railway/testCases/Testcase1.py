import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_01_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_login(self,setup):

        self.logger.info("*********** TC_01_Login **************")
        self.logger.info("***** Verify User can log into Railway with valid username and password *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.clickLoginPage()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickBookticketPage()
        self.lp.setDepartDate(self.Date)
        self.lp.setDepartName(self.DepartStation)
        self.lp.setArriveName(self.ArriveStation)
        self.lp.setSeatType(self.SeatType)
        self.lp.setTicketName(self.TicketAmount)
        self.lp.clickMyticketPG()


        act_title = self.driver.title

        if act_title == "Safe Railway - Selenium Automation":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.logger.error("******* Test_01_Login is failed *******")
            assert False
