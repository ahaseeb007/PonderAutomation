import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium.webdriver.chrome.options import Options as ChromeOptions
from config.config import config

def pytest_html_report_title(report):
    ''' modifying the title of html report '''
    report.title = "Automation Report"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    outcome._result.custom_description = item.function.__doc__

@pytest.fixture(params=["chrome"], scope='function')
def setup(request):
    if request.param=="chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("user-data-dir=F:\\testing\\Ponder")
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        web_driver.get(config.app_url)
        web_driver.maximize_window()
    request.cls.driver = web_driver
    yield
    web_driver.quit()