from testCases.conftest import pytest_configure
from pageObjects.homePage import HomePage
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
from ultilities.Constant.Constant import Constant

class TC04(LOGGER):

    def test_LoginPage_Displayed_When_Select_Book_Ticket_Tab(self):
        driver = self.driver

        LOGGER.info("1.Navigate to QA Railway Website")
        driver.get("http://railway.ges.guru/Page/HomePage.cshtml")

        homePage = HomePage(driver)

        LOGGER.info("2.Click on Login tab")
        homePage.selectBookTicketMenu()

        LOGGER.info("Verify: Message welcome should be displayed correctly")
        self.assertEqual(homePage.getPageTitle(), Constant.LOGIN_PAGE, "Error Message should be displayed correctly")