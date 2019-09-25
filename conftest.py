from selenium import webdriver
import pytest
import logging


def pytest_addoption(parser):
    parser.addoption("--chromedriver_path",
                     action="store",
                     default="chromedriver.exe")


@pytest.fixture
def driver(request):
    driver = None
    try:
        driver = webdriver.Chrome(
            executable_path=request.config.getoption("--chromedriver_path"))
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield driver
    except Exception as e:
        logging.fatal(str(e))
        raise e
    finally:
        if driver is not None:
            driver.quit()
