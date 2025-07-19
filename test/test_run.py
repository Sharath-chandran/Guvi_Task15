import pytest
from pages.login_page import LoginPage
from utils.excel_utils import ExcelUtil

excel = ExcelUtil("C:\\Users\\Admin\\PycharmProjects\\Guvi_Task15\\Excel_data\\testdata.xlsx")
test_data = excel.get_data()


@pytest.mark.parametrize("test_id, username, password", test_data)
def test_login_details(driver, test_id, username, password):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username, password)
    success = login_page.is_login_successful()

    row_num = int(test_id) + 1  # Assuming row starts from 2
    result = "Pass" if success else "Fail"
    excel.write_result(row=row_num, result=result)
    assert success, f"Login failed for Username: {username}"