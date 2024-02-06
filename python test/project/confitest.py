import requests
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.core import manager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from check_post import get_login
from src.api_actions import APIActions
from src.ui_actions import UIActions

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']

@pytest.fixture
def token():
      return get_login()


@pytest.fixture(scope="session")
def browser():
 
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)

        yield driver
        driver.quit()



@pytest.fixture(scope="session")
def setup_api():
    base_url = "https://test-stand.gb.ru/gateway/login"
    api_actions = APIActions(base_url)
    yield api_actions


@pytest.fixture(scope="session")
def setup_api_with_auth(setup_api):
    token = setup_api.authenticate("username", "password")
    setup_api.set_auth_header(token)
    yield setup_api

@pytest.mark.parametrize("url", [
    ("https://test-stand.gb.ru/gateway/login")])
def test_api(url):
    response = requests.equest.get(url)
    assert response.status_code == 200
    assert response.json()["success"] == True


@pytest.fixture(scope="session")
def setup_ui():
    driver = webdriver.Chrome()
    ui_actions = UIActions(driver)
    yield ui_actions
    driver.quit()
