import unittest


class TestWatch(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_home_screen_components(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
