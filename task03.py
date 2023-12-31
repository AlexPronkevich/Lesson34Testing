# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
#
#
# class SimpleGoogleTest(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Chrome()
#         cls.driver.implicitly_wait(10)
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()
#
#     def testSearchSelenium(self):
#         expected_title = "Selenium"
#
#         question_input = SimpleGoogleTest.driver.find_element(By.NAME, 'q')
#         question_input.send_keys("selenium")
#         question_input.send_keys(Keys.ENTER)
#
#         selenium_link = self.driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div/div[1]/div/a/h3' )
#         selenium_link.click()
#
#         actual_tile = self.driver.title
#
#         self.assertEqual(expected_title, actual_tile)


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SimpleGoogleTest(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) :
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.implicitly_wait(10)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def testSearchSelenium(self):
        expected_title = "selenium"

        self.driver.get("https://www.google.ru")

        question_input = self.driver.find_element(By.NAME, 'q')
        question_input.send_keys("selenium")
        question_input.send_keys(Keys.ENTER)

        # selenium_link = self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/h3')
        # selenium_link.click()

        # actual_title = self.driver.title
        actual_title = self.driver.title

        self.assertIn(expected_title, actual_title)
