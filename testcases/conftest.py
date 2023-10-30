from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver = webdriver.Chrome()
        print("---- Launching Chrome browser ------")
    elif browser=="firefox":
        driver=webdriver.firefox()
        print("---- Launching firefox browser ------")
    else:
        driver=webdriver.Ie()
        print("---- Launching Ie browser ------")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# def pytest_configure(config):
#     config._metadata["project name"] ="Register page"
#     config._metadata["Module name"] = "Customer registration"
#     config._metadata["tester"] = "Rezwana"
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME",None)
#     metadata.pop("Plugins",None)
