import pytest
from pages.login_page import LoginPage
from utils.excel_utils import ExcelUtil

excel = ExcelUtil("C:\\Users\\Admin\\PycharmProjects\\Guvi_Task15\\Excel_data\\testdata.xlsx")
# Fetches a list of tuples with test_id, username, and password from the Excel sheet.
test_data = excel.get_data()

#  By using the below method we can run the same test function multiple times with different data sets.
# Each time, it injects test_id, username, and password from the Excel rows.
@pytest.mark.parametrize("test_id, username, password", test_data)
# Actual test function, driver is a fixture that initializes the WebDriver (usually handled in conftest.py).
def test_login_details(driver, test_id, username, password):
    login_page = LoginPage(driver)
    login_page.load() # loads the login page.
    login_page.login(username, password) # performs the login action.
    success = login_page.is_login_successful() # checks if login was successful (returns True or False).

# Result Handling and Assertion
    row_num = int(test_id) + 1  # Assuming row starts from 2
    # # write "Pass" else "Fail" to the Excel sheet.
    result = "Pass" if success else "Fail"
    excel.write_result(row=row_num, result=result)
    # assert success, ensures that failed logins are marked as test failures.
    assert success, f"Login failed for Username: {username}"