
from pageObjects.homePage import HomePage
from pageObjects.LoginPage import Login
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
from ultilities.Constant.Constant import Constant

class TC03(LOGGER):

    def test_Login_To_Railway_With_Username_Invalid(self):
        driver = self.driver

        LOGGER.info("1.Navigate to QA Railway Website")
        driver.get("http://railway.ges.guru/Page/HomePage.cshtml")

        homePage = HomePage(driver)
        loginPage = Login(driver)

        LOGGER.info("2.Click on Login tab")
        LOGGER.info("3.Enter invalid Email and valid Password")
        homePage.selectLoginMenu()\
            .loginPage("", Constant.PASSWORD)

        LOGGER.info("Verify: Message welcome should be displayed correctly")
        self.assertEqual(loginPage.getErrorMessage(), Constant.ERROR_MESSAGE, "Error Message should be displayed correctly")

