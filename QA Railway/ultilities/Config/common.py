import configparser
from ultilities.readProperties  import ReadConfig

class Common():

    def get_project_path(self):
        import os
        return os.path.abspath(os.getcwd())

    def get_driver(self,browser):
        if browser.Chrome == browser:
            return Common.get_project_path(self) + "/Users/Asus/Downloads/chromedriver.exe"
        elif browser.FireFox == browser:
            return Common.get_project_path(self) + "/Users/Asus/Downloads/geckodriver"
