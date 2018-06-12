from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from values import strings


class HomeScreen:

    def __init__(self, driver):
        self.driver = driver
        self.register_link = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//a[@href='/watchshop/sign-up/']")))
        self.card_title = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "card-title")))
        self.login_button = WebDriverWait(self.driver.instance, 10).until(
            EC.presence_of_element_located((
                By.TAG_NAME, "button")))
        self.user_field = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.ID, "id_username")))
        self.password_field = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.ID, "id_password")))

    def validate_title_is_present(self):
        assert self.title.is_displayed()

    def validate_card_title_is_present(self):
        assert self.card_title.is_displayed()

    def validate_login_button_is_present(self):
        assert self.login_button.is_displayed()

    def validate_credential_fields_are_present(self):
        assert self.user_field.is_displayed()
        assert self.password_field.is_displayed()

    def validate_register_link_is_present(self):
        assert self.register_link.is_displayed()
