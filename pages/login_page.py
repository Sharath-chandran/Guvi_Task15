from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Creating a POM class file (login_page) which contains locators and functions to be executed in that page.
# Class contains methods specific to the actions that can be performed on that page.
class LoginPage:
    # def - Constructor method used to initialize an object when it is created
    # __init__: This is a special method in Python classes. It runs automatically when you create a new object from the class.
    # Self: Refers to the current instance of the class. It allows the object to store and access its own data and methods.
    # driver: This is a parameter passed when creating the object. In Selenium, it's usually a WebDriver instance (like webdriver.Chrome()).
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        # XPATH for the username input field
        self.username_input = (By.XPATH, "//input[@name='username']")
        # XPATH for the password input field
        self.password_input = (By.XPATH, "//input[@name='password']")
        # XPATH for the sign-in button in the Login page
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.dashboard_text = (By.XPATH, "//h6[text()='Dashboard']")

    # Opens the login page in the browser.
    def load(self):
        # Uses the Selenium WebDriver to navigate to the URL stored in self.url.
        self.driver.get(self.url)

    # Login Method
    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_input)).send_keys(username)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_input)).send_keys(password)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.login_button)).click()

    # Method to validate login is successful or not
    def is_login_successful(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.dashboard_text))
            return True
        except:
            return False