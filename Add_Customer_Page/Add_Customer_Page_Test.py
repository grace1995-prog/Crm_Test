from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from Add_Customer_Locator.Add_Customer_Locator_Test import Add_Customer_Locator


class Add_Customer_Page_Test:
    def __init__(self, driver):
        self.driver = driver

    def customer_field(self):
        add_user = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Add_Customer_Locator.Add_New))
        add_user.click()
