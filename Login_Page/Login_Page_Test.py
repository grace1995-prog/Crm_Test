from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from Login_Locator.Login_Locator_Test import Login_Locator_Test


class Login_Page_Test:

    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def email_address(self, email_address):
        enter_email_address = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Login_Locator_Test.ENTER_EMAIL_ADDRESS))
        enter_email_address.send_keys(email_address)

    def enter_password(self, enter_password):
        password_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Login_Locator_Test.ENTER_PASSWORD))
        password_field.send_keys(enter_password)

    def check_box(self):
        checkbox_field = WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(Login_Locator_Test.REMEMBER_CHECK_BOX))
        checkbox_field.click()

    def submit_button(self):
        button_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Login_Locator_Test.CLICK_SUBMIT_BUTTON))
        button_field.click()
