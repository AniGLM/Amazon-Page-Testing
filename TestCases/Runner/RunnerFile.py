import unittest
from TestCases.AddItem.AddItemTestCase import AddItemClass
from TestCases.EmptyCart.EmptyTheCartTestCase import EmptyCartClass
from TestCases.RecommendationItemSelection.RecommendItemSelection import RecommendItemSelectClass
from TestCases.LogInLogOut.SignInSignOutTestCase import LogInLogOut
from TestCases.TotalTestes.TotalTestCase import TotalClass


def suite():
    suite = unittest.TestSuite()

    suite.addTest(AddItemClass("test_addItem"))
    suite.addTest(RecommendItemSelectClass("test_recItemSelection"))
    suite.addTest(EmptyCartClass("test_emptyCart"))
    suite.addTest(LogInLogOut("test_logInLogOut"))
    suite.addTest(TotalClass("test_totalTest"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
