from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from SignOut_Locator.SignOut_Locator_Test import SignOut_Locator_Test


class SignOut_Page_Test:

    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def sign_out_button(self, driver):
        sign_out_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(SignOut_Locator_Test.SIGN_OUT_BUTTON))
        sign_out_field.click()
