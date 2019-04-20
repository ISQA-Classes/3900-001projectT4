import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class AddActivity_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_add_activity(self):
       user = "instructor"
       pwd = "instructor1a"

       driver = self.driver
       driver.maximize_window()
       driver.get("https://blai.pythonanywhere.com/login")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       driver.get("https://blai.pythonanywhere.com")
       assert "Logged In"
       time.sleep(2)

       #path to view activity list
       driver.get("https://blai.pythonanywhere.com/activity_list")
       time.sleep(2)

       # path for Add activity
       elem = driver.find_element_by_xpath("html/body/div/div/div/div[3]/div/a/span").click()
       time.sleep(2)

       elem = driver.find_element_by_id("id_title")
       elem.send_keys("Serving food to Street people")
       time.sleep(1)

       elem = driver.find_element_by_id("id_description")
       elem.send_keys(" Help our Organization to serve street people in Downtown, Omaha on May 12, 2019.")
       select = Select(driver.find_element_by_id("id_type"))
       time.sleep(1)

       select.select_by_value("Community")
       time.sleep(1)

       elem = driver.find_element_by_id("id_start_time").clear()
       time.sleep(1)

       elem = driver.find_element_by_id("id_start_time")
       elem.send_keys("2019-05-12 10:00:00")
       time.sleep(1)

       elem = driver.find_element_by_id("id_end_time").clear()
       time.sleep(1)

       elem = driver.find_element_by_id("id_end_time")
       elem.send_keys("2019-05-12 14:00:00")
       time.sleep(2)

        #path for Save the new activity
       elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
       time.sleep(2)
       assert "New activity Created"

       driver.get("https://blai.pythonanywhere.com/activity_list")
       time.sleep(3)

       def tearDown(self):
           self.driver.close()

   if __name__ == "__main__":
       unittest.main()


