class RegisterPage:
    textbox_email_id = "email"
    textbox_password_id = "password"
    textbox_confirm_id = "confirmPassword"
    textbox_pid_id = "pid"
    button_register_xpath = "//body/div[@id='page']/div[@id='content']/div[1]/form[1]/fieldset[1]/input[1]"



    def __init__(self,driver):
        self.driver = driver

    def clickRegisterPG(self):
        self.driver.find_element_by_xpath(self.button_registerpg_xpath).click()

    def setEmail(self,email):
        self.driver.find_element_by_id(self.textbox_email_id).clear()
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def setConfirm(self,confirm):
        self.driver.find_element_by_id(self.textbox_confirm_id).clear()
        self.driver.find_element_by_id(self.textbox_confirm_id).send_keys(confirm)

    def setPID(self,pid):
        self.driver.find_element_by_id(self.textbox_pid_id).clear()
        self.driver.find_element_by_id(self.textbox_pid_id).send_keys(pid)

    def clickRegisterBTN(self):
        self.driver.find_element_by_xpath(self.button_register_xpath).click()