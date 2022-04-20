from selenium.webdriver.firefox import webdriver

from django.test import LiveServerTestCase

class TitleTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()
        cls.selenium = webdriver()
        cls.selenium.implicity_wait(10)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.selenium.quit()
        return super().tearDownClass()

    def test_title_on_home_page(self):
        self.selenium.get(self.live_server_url)
        self.selenium('Travel Wishlist', self.selenium.title)

class AddPlacesTest(LiveServerTestCase):

    fixtures = ['test_places']

    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()
        cls.selenium = webdriver()
        cls.selenium.implicity_wait(10)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.selenium.quit()
        return super().tearDownClass()

    def test_add_ne_place(self):

        self.selenium.get(self.live_server_url)
        input_name = self.selenium.finde_element_by_id('id_name')
        input_name.send_keys('Denver')

        add_button = self.selenium.find_element_by_id('add-new-place')
        add_button.click
    
        denver = self.selenium.find_element_by_id('place_name_5')
        self.assertEqual('Denver', denver.text)

        self.assertIn('Denver', self.selenium.page_source)
        self.assertIn('New York', self.selenium.page_source)
        self.assertIn('Tokyo', self.selenium.page_source)
        


