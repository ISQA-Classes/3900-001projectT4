import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class AddActivityAdminATS(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor"
        pwd = "instructor1a"

        # Create profile in admin page
        driver = self.driver
        driver.maximize_window()
        driver.get("https://blai.pythonanywhere.com/admin/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.get("https://blai.pythonanywhere.com/admin/volunnet/activity/add/")

        # Inputs for activity
        elem = driver.find_element_by_id("id_title")
        elem.send_keys("Picking up litter in Dundee!")
        elem = driver.find_element_by_id("id_description")
        elem.send_keys("Looking for 3 volunteers who want to help my non-profit! We plan on doing it muliple times a"
                       "month, so keep any eye out for more future posts!")
        select = Select(driver.find_element_by_id("id_type"))
        time.sleep(2)
        select.select_by_value("Environmental")
        elem = driver.find_element_by_id("id_start_time_0").clear()
        time.sleep(1)
        elem = driver.find_element_by_id("id_start_time_0")
        elem.send_keys("2019-05-15")
        elem = driver.find_element_by_id("id_start_time_1").clear()
        time.sleep(1)
        elem = driver.find_element_by_id("id_start_time_1")
        elem.send_keys("8:00:00")
        elem = driver.find_element_by_id("id_end_time_0").clear()
        time.sleep(1)
        elem = driver.find_element_by_id("id_end_time_0")
        elem.send_keys("2019-05-15")
        elem = driver.find_element_by_id("id_end_time_1").clear()
        time.sleep(1)
        elem = driver.find_element_by_id("id_end_time_1")
        elem.send_keys("12:00:00")
        time.sleep(2)
        elem = driver.find_element_by_name("_save").click()

        # Show in pythonanywhere
        driver.get("https://blai.pythonanywhere.com/")
        time.sleep(2)
        driver.get("https://blai.pythonanywhere.com/activity_list")

        assert "New activity Created"
        time.sleep(3)

        def tearDown(self):
            self.driver.close()


if __name__ == "__main__":
    unittest.main()
