import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def browser():
    s = Service(executable_path="C:\\Users\\Nail\\PycharmProjects\\TenzorTests\\chromedriver\\chromedriver.exe")
    Options = webdriver.ChromeOptions()
    Options.add_argument('headless')
    # Options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(service=s, options=Options)
    yield driver
    driver.close()
    driver.quit()
