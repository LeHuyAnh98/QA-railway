from selenium.webdriver.common.by import By

class HomePage():
    def __init__(self, driver):
        self._driver = driver

        self._btnLogin = "//a[.='Login']"
        self._btnBookTicket = "//a[.='Book ticket']"
        self._btnLogout = "//a[.='Log out']"
        self._btnMyTicket = "//a[.='My ticket']"
        self._btnChangePassword = "//a[.='Change password']"
        self._txtPageTitle = "//div[@id='page']//div[@id='content']/h1"

    def selectLoginMenu(self):
        self._driver.find_element(By.XPATH, self._btnLogin).click()
        from pageObjects.LoginPage  import Login
        return Login(self._driver)

    def selectBookTicketMenu(self):
        self._driver.find_element(By.XPATH, self._btnBookTicket).click()
        from pageObjects.LoginPage import  Login
        return Login(self._driver)

    def getPageTitle(self):
        return self._driver.find_element(By.XPATH, self._txtPageTitle).text

    def isLogoutButtonDisplayed(self):
        return self._driver.find_element(By.XPATH, self._btnLogout).is_displayed()

    def isMyTicketButtonDisplayed(self):
        return self._driver.find_element(By.XPATH, self._btnMyTicket).is_displayed()

    def isChangePasswordButtonDisplayed(self):
        return self._driver.find_element(By.XPATH, self._btnChangePassword).is_displayed()

    def selectMyTicketMenu(self):
        self._driver.find_element(By.XPATH, self._btnMyTicket).click()
        from pageObjects.myTicketPage import MyTicketPage
        return MyTicketPage(self._driver)

    def selectChangePasswordMenu(self):
        self._driver.find_element(By.XPATH, self._btnChangePassword).click()
        from pageObjects.changePasswordPage import ChangePasswordPage
        return ChangePasswordPage(self._driver)