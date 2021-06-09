
from pageObjects.homePage import HomePage
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
from ultilities.Constant.Constant import Constant

class TC05(LOGGER):

    def test_Warning_Message_Displayed(self):
        driver = self.driver

        LOGGER.info("1.Navigate to QA Railway Website")
        driver.get("http://railway.ges.guru/Page/HomePage.cshtml")

        homePage = HomePage(driver)

        LOGGER.info("2.Click on Login tab")
        LOGGER.info("3.Enter valid Email and invalid Password 3 times")
        homePage.selectLoginMenu().loginPage(Constant.LOGIN_PAGE, "")
        homePage.selectLoginMenu().loginPage(Constant.LOGIN_PAGE, "")
        homePage.selectLoginMenu().loginPage(Constant.LOGIN_PAGE, "")

        LOGGER.info("Verify: Message welcome should be displayed correctly")
        self.assertEqual(homePage.getPageTitle(), Constant.LOGIN_PAGE, "Error Message should be displayed correctly")