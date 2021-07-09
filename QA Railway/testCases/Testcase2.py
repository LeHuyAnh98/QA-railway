import pytest
from selenium import webdriver
from pageObjects.RegisterPage import RegisterPage


class Test_01_Login:
    baseURL = "http://railwaysg2.somee.com/Page/HomePage.cshtml"
    email = "lehuyanh98@gmail.com"
    password = "12345678"
    pid = "12345678"

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = RegisterPage(self.driver)
        self.lp.clickRegisterPG()
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.setConfirm(self.password)
        self.lp.setPID(self.pid)
        self.lp.clickRegisterBTN()
        act_title = self.driver.title

        if act_title == "Thank you for registering your account":
            assert True
        else:
            assert False