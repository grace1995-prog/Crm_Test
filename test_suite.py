import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

from Add_Customer_Page.Add_Customer_Page_Test import Add_Customer_Page_Test
from Login_Page.Login_Page_Test import Login_Page_Test
from New_Customer_Page.New_Customer_Page_Test import New_Customer_Page_Test

from SignOut_Page.SignOut_Page_Test import SignOut_Page_Test


@pytest.fixture(scope="session")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def login(driver_setup):
    driver = driver_setup
    login_page = Login_Page_Test(driver)
    login_page.login_url("https://automationplayground.com/crm/login.html")
    return login_page


def test_login_page(login):
    login.email_address("graceuko@gmail.com")
    login.enter_password("grace")
    login.check_box()
    login.submit_button()


def test_click_on_add_customer(login):
    add_new_customer = Add_Customer_Page_Test(login.driver)
    add_new_customer.customer_field()


def test_add_customer(login):
    new_add_customer = New_Customer_Page_Test(login.driver)
    new_add_customer.email_field("ukomonday@gmail.com")
    new_add_customer.firstname_field("Esther")
    new_add_customer.lastname_field("Julian")
    new_add_customer.city_field("lagos")
    new_add_customer.gender_field()
    new_add_customer.promotion_field()
    new_add_customer.submit_field()


def test_sign_out(login):
    sign_in = SignOut_Page_Test(login.driver)
    sign_in.sign_out_button()
