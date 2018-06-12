import unittest
from webdriver import Driver
from values import strings
from pageobjects.homescreen import HomeScreen


class TestWatch(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_home_screen_components(self):
        home_screen = HomeScreen(self.driver)
        home_screen.validate_card_title_is_present()
        home_screen.validate_login_button_is_present()
        home_screen.validate_credential_fields_are_present()
        home_screen.validate_register_link_is_present()

    def tearDown(self):
        self.driver.instance.quit()

if __name__ == '__main__':
    unittest.main()
