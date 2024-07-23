from selenium import webdriver
from selenium.webdriver.common.by import By


class Login_Locator_Test:
    ENTER_EMAIL_ADDRESS = (By.XPATH, "/html/body/section/div/div/div/div/form/div[1]/input")
    ENTER_PASSWORD = (By.XPATH, "/html/body/section/div/div/div/div/form/div[2]/input")
    REMEMBER_CHECK_BOX = (By.XPATH, "/html/body/section/div/div/div/div/form/div[3]/label/input")
    CLICK_SUBMIT_BUTTON = (By.XPATH, "/html/body/section/div/div/div/div/form/button")
