from selenium import webdriver
from selenium.webdriver.common.by import By


class New_Customer_Locator_Test:
    ENTER_EMAIL_ADDRESS_FIELD = (By.XPATH, "/html/body/section/div/div/div/div/form/div[1]/input")
    ENTER_FIRSTNAME = (By.XPATH, "/html/body/section/div/div/div/div/form/div[2]/input")
    ENTER_LASTNAME = (By.XPATH, "/html/body/section/div/div/div/div/form/div[3]/input")
    ENTER_CITY = (By.XPATH, "/html/body/section/div/div/div/div/form/div[4]/input")
    SELECT_STATE = (By.XPATH, "/html/body/section/div/div/div/div/form/div[5]/select")
    SELECT_GENDER = (By.XPATH, "/html/body/section/div/div/div/div/form/div[6]/input[1] ")
    ADD_PROMOTION_LIST = (By.XPATH, "/html/body/section/div/div/div/div/form/div[7]/input")
    SUBMIT_BUTTON = (By.XPATH, "/html/body/section/div/div/div/div/form/button")
