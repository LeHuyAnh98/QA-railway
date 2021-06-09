class Login:
    textbox_username_id = "username"
    textbox_password_id = "password"
    button_login_xpath = "/html/body/div/div[2]/form/fieldset/p/input"
    link_logout_linktext = "Log out"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
            self.driver.find_element_by_id(self.textbox_username_id).clear()
            self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()
