from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestForgotPassword:
    def tc_pim_01(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)

        # Load OrangeHRM webpage
        orange_hrm_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(orange_hrm_url)

        # Click on "Forgot Password" link
        forgot_password_link = driver.find_element(By.XPATH, '//p[@class="oxd-text oxd-text--p orangehrm-login-forgot-header"]')
        forgot_password_link.click()

        # Validate that the Username textbox is visible
        username_textbox = driver.find_element(By.XPATH, '//input[@name="username"]')
        assert username_textbox.is_displayed(), "Username textbox is not visible"
        print("SUCCESS # USERNAME TEXTBOX IS VISIBLE")

        # Enter the username and click on Reset Password button
        username_textbox.send_keys("Admin")
        reset_password_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
        reset_password_button.click()

        # Validate that the success message is displayed
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//p[contains(text(),"Reset Password link sent successfully")]'))
        )
        assert success_message.is_displayed(), "Reset Password success message not displayed"
        print("SUCCESS # RESET PASSWORD LINK SENT SUCCESSFULLY")

        driver.close()

TD = TestForgotPassword()
TD.tc_pim_01()
