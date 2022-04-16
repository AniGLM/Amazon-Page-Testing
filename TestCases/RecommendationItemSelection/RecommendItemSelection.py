import unittest
from Pages.Common.BaseClassForTestes import BaseClassForTestes
from Pages.Main.NavBar.AccountAndLists import AccountAndListsClass


class RecommendItemSelectClass(unittest.TestCase, BaseClassForTestes):

    def setUp(self):
        self.general_vars_for_testcases()
        self.accountLists = AccountAndListsClass(self.driver)

    def test_recItemSelection(self):
        self.driver.get(
            r"https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
        self.loginPage.fill_login_field()
        self.loginPage.press_continue_button()

        self.passwordPage.fill_password_field()
        self.passwordPage.keep_me_signIn()
        self.passwordPage.click_into_signIn_button()

        self.navigationBar.account_and_lists()
        self.accountLists.recommendation_field()
        self.accountLists.choosing_3th_item()
        self.navigationBar.open_cart()

    def tearDown(self):
        self.navigationBar.account_and_lists()
        self.passwordPage.sign_out_button()
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
