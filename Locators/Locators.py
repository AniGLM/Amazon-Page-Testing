from selenium.webdriver.common.by import By


class LocatorsClass():
    # LoginPage Locators
    loginPageLoginFieldLocator = (By.ID, "ap_email")
    loginPageContinuePageLocator = (By.ID, "continue")

    # PasswordPage Locators
    passwordPagePasswordFieldLocator = (By.ID, "ap_password")
    passwordPageSignInButtonLocator = (By.ID, "signInSubmit")
    keepMeSignedInLocator = (By.NAME, "rememberMe")

    # SearchField Locators
    navigationBarSearchButtonLocator = (By.ID, "twotabsearchtextbox")
    navigationBarEnterButtonLocator = (By.ID, "nav-search-submit-button")
    # Item Locators
    itemSelectionChosenItemLocator = (By.CLASS_NAME, "s-image")
    itemSelectionSizeChartLocator = (By.ID, "dropdown_selected_size_name")
    itemSelectionSizeFitLocator = (By.LINK_TEXT, "7")

    # Cart Locators
    navigationBarAddCartLocator = (By.ID, "add-to-cart-button")
    navigationBarCheckingCartLocator = (By.ID, "nav-cart")
    navigationBarDeleteContent = (By.XPATH, '//input[@value="Delete"]')
    navigationBarGetCartItemsCount = (By.XPATH, '//span[@id="nav-cart-count"]')

    # Account and Lists
    navigationBarAccountAndLists = (By.XPATH, '//a[@id="nav-link-accountList"]')
    accountAndListsRecommendations = (By.LINK_TEXT, "Recommendations")
    recommendationsItemsChoosing = (By.XPATH, '//div[@id="gridItemRoot"]')
    recommendationsAddToCartButton = (By.XPATH, '//input[@name="submit.addToCart"]')
    recommendationItemsSeeAllBuyingOptions = (By.LINK_TEXT, "See all buying options")
    accountAndListSignOutButton = (By.XPATH, '//a[@id="nav-item-signout"]')
