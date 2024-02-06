import logging
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import yaml

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    url = testdata['address']



class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = url

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), 
                                                             message=f"Can't find element dy locator {locator}")
        except:
            logging.exception('Find element exception')   
            element = None
        return element
  
    def get_element_property(self, locator, property):
        element = self.driver.find_element(locator)
        if element:
          return element.value_of_css_property(property)
        else:
          logging.exception(f'Property {property} nit found in elevent with {locator}')
          return None

    def go_to_site(self):
        try:
            start__browsing = self.driver.get(self.base_url)
        except:
            logging.exception('Exception whle open site')
            start__browsing = None
        return start__browsing


