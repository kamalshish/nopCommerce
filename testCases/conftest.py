from selenium import webdriver
import pytest

# @pytest.fixture()
# def setup():
#     driver=webdriver.Chrome()
#     return driver

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("launching chrome browser.......")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("launching firefox browser.......")
    else:
        driver=webdriver.Firefox()
    return driver

def pytest_addoption(parser):       # this will get value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):               # this will return browser value to setup method
    return request.config.getoption("--browser")

 # pytest -v -s testCases/test_login.py --browser firefox
# pytest -s -v testCases/test_login.py --browser chrome
# pytest -s -v -n=2 testCases/test_login.py --browser chrome
# pytest -s -v -n=2 testCases/test_login.py --browser firefox
# pytest -s -v -n=2 --html=Reports\report.html testCases/test_login.py --browser chrome
# pytest -s -v  --html=Reports\report.html testCases/test_login_ddt.py --browser chrome
# pytest -v  --html=Reports\report.html testCases/test_login_ddt.py --browser chrome
# pytest -v  --html=Reports\report.html testCases/test_addCustomer.py --browser chrome
# pytest -v  --html=Reports\report.html testCases/test_searchCustomerByEmail.py --browser chrome
# pytest -v  --html=Reports\report.html testCases/test_searchCustomerByName.py --browser chrome

# pytest -v -m "sanity" --html=Reports\report.html testCases/  --browser chrome                     #marker
# pytest -v -m "regression" --html=Reports\report.html testCases/  --browser chrome                 #marker
# pytest -v -m "sanity or regression" --html=Reports\report.html testCases/  --browser chrome       #marker
# pytest -v -m "sanity and regression" --html=Reports\report.html testCases/  --browser chrome      #marker


##################### pytest html report ######################
# this is hook for adding environment info into html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Kamalshish'

# this is hook for delete/modify environment info into html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)

