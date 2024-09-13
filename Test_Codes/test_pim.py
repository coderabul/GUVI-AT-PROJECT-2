from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_Data import pim_data
import pytest


class TestPIM:
    url = pim_data.LoginData.url

    # Launching driver for running the Python Tests
    @pytest.fixture
    def launch_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        # login to orangeHRM webpage
        self.driver.get(self.url)
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_username).send_keys(pim_data.LoginData.username)
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_password).send_keys(pim_data.LoginData.password)
        self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_login).click()
        yield
        self.driver.close()

    def test_pim1(self, launch_driver):
        try:
            # Click "Forgot Password" link
            self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_forgot_password_link).click()

            # Validate that the Username textbox is visible
            username_textbox = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_username_textbox)
            assert username_textbox.is_displayed(), "Username textbox is not visible"
            print("SUCCESS # USERNAME TEXTBOX IS VISIBLE")

            # Provide the username
            username_textbox.send_keys("Admin")

            # Click the "Reset Password" button
            self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_reset_password_button).click()

            # Use WebDriverWait to ensure success message is displayed
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, pim_data.ElementLocators.xpath_reset_success_message))
            )

            # Validate that the "Reset Password link sent successfully" message is displayed
            reset_success_message = self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_reset_success_message)
            assert reset_success_message.is_displayed(), "Reset Password success message not displayed"
            print("SUCCESS # RESET PASSWORD LINK SENT SUCCESSFULLY")

        except Exception as e:
            print(f"Test failed: {e}")
            raise

    def test_pim2(self, launch_driver):
        try:
            # click Admin button
            self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_admin_button).click()

            # validate the page title
            assert self.driver.title == "OrangeHRM", "Page title is incorrect"
            print("SUCCESS # PAGE TITLE IS OrangeHRM")

            # Validate header options on Admin page
            header_options = {
                "User Management": pim_data.ElementLocators.xpath_of_user_management,
                "Job": pim_data.ElementLocators.xpath_of_job_header,  
                "Organization": pim_data.ElementLocators.xpath_of_organization_header,  
                "Qualifications": pim_data.ElementLocators.xpath_of_qualifications_header,  
                "Nationalities": pim_data.ElementLocators.xpath_of_nationalities_header,  
                "Corporate Banking": pim_data.ElementLocators.xpath_of_corporate_banking_header,  
                "Configuration": pim_data.ElementLocators.xpath_of_configuration_header  
            }

            for option, xpath in header_options.items():
                element = self.driver.find_element(by=By.XPATH, value=xpath)
                assert element.is_displayed(), f"{option} header is not displayed"
                print(f"SUCCESS # {option} HEADER PRESENT")

            print("SUCCESS # ALL HEADERS VALIDATED ON ADMIN PAGE")

        except Exception as e:
            print(f"Test failed: {e}")
            raise

    def test_pim3(self, launch_driver):
        try:
            # click Admin button
            self.driver.find_element(by=By.XPATH, value=pim_data.ElementLocators.xpath_admin_button).click()

            # Validate side menu options on Admin page
            menu_options = {
                "Admin": pim_data.ElementLocators.xpath_of_admin_menu,
                "PIM": pim_data.ElementLocators.xpath_of_pim_menu,
                "Leave": pim_data.ElementLocators.xpath_of_leave_menu,
                "Time": pim_data.ElementLocators.xpath_of_time_menu,
                "Recruitment": pim_data.ElementLocators.xpath_of_recruitment_menu,
                "My Info": pim_data.ElementLocators.xpath_of_my_info_menu,
                "Performance": pim_data.ElementLocators.xpath_of_performance_menu,
                "Dashboard": pim_data.ElementLocators.xpath_of_dashboard_menu,
                "Directory": pim_data.ElementLocators.xpath_of_directory_menu,
                "Maintenance": pim_data.ElementLocators.xpath_of_maintenance_menu,
                "Buzz": pim_data.ElementLocators.xpath_of_buzz_menu
            }

            for menu, xpath in menu_options.items():
                element = self.driver.find_element(by=By.XPATH, value=xpath)
                assert element.is_displayed(), f"{menu} menu is not displayed"
                print(f"SUCCESS # {menu} MENU PRESENT")

            print("SUCCESS # ALL MENU OPTIONS VALIDATED ON ADMIN PAGE")

        except Exception as e:
            print(f"Test failed: {e}")
            raise
