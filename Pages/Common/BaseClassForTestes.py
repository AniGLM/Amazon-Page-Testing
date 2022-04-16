from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.Login.LogInPage import LogInClass
from Pages.Login.PasswordPage import PasswordClass
from Common.Variables.Variables import VariablesClass
from Pages.Main.NavBar.NavigationBar import NavigationBarClass


class BaseClassForTestes():

    def general_vars_for_testcases(self):
        self.variables = VariablesClass()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.loginPage = LogInClass(self.driver)
        self.passwordPage = PasswordClass(self.driver)
        self.navigationBar = NavigationBarClass(self.driver)

