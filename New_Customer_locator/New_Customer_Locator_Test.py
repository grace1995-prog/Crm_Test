from selenium import webdriver
from selenium.webdriver.common.by import By


class New_Customer_Locator_Test:
    ENTER_EMAIL_ADDRESS_FIELD = (By.ID, "")
    ENTER_FIRSTNAME = (By.ID, "")
    ENTER_LASTNAME = (By.ID, "")
    ENTER_CITY = (By.ID, "")
    SELECT_STATE = (By.XPATH, "")
    SELECT_GENDER = (By.XPATH, " ")
    ADD_PROMOTION_LIST = (By.XPATH, "")
    SUBMIT_BUTTON = (By.XPATH, "")
