# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestUntitled():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.driver.get("https://www.qa.com")
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_untitled(self):
    assert self.driver.title == "Contact us | QA"
  
test = TestUntitled()
test.setup_method()
test.test_untitled()