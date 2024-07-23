from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from New_Customer_locator.New_Customer_Locator_Test import New_Customer_Locator_Test


class NewCustomer_Page_Test:

    def __int__(self, driver):
        self.driver = driver

    def email_field(self, email_field):
        enter_email_address = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(New_Customer_Locator_Test.ENTER_EMAIL_ADDRESS_FIELD))
        enter_email_address.send_keys(email_field)

    def firstname_field(self, firstname_field):
        enter_firstname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(New_Customer_Locator_Test.ENTER_FIRSTNAME))
        enter_firstname.send_keys(firstname_field)

    def lastname_field(self, firstname_field):
        enter_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(New_Customer_Locator_Test.ENTER_LASTNAME))
        enter_lastname.send_keys(firstname_field)

    def city_field(self, city_field):
        enter_city = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(New_Customer_Locator_Test.ENTER_CITY))
        enter_city.send_keys(city_field)

    def state_field(self, state_field):
        enter_state = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(New_Customer_Locator_Test.SELECT_STATE))
        enter_state.send_keys(state_field)

    def gender_field(self):
        enter_gender = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(New_Customer_Locator_Test.SELECT_GENDER))
        enter_gender.click()

    def promotion_field(self):
        enter_promotion = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(New_Customer_Locator_Test.ADD_PROMOTION_LIST))
        enter_promotion.click()

    def submit_field(self):
        submit_button_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(New_Customer_Locator_Test.SUBMIT_BUTTON))
        submit_button_field.click()
