from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAdminPageHeaders:
    def tc_pim_02(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)

        # Load OrangeHRM webpage
        orange_hrm_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(orange_hrm_url)

        # Login as Admin
        driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("Admin")
        driver.find_element(By.XPATH, '//input[@type="password"]').send_keys("admin123")
        driver.find_element(By.XPATH, '//button[@type="submit"]').click()

        # Navigate to Admin page
        admin_button = driver.find_element(By.XPATH, '//a[@class="oxd-main-menu-item" and @href="/web/index.php/admin/viewAdminModule"]')
        admin_button.click()

        # Validate Page Title
        assert driver.title == "OrangeHRM", "Page title is not 'OrangeHRM'"
        print("SUCCESS # PAGE TITLE IS 'OrangeHRM'")

        # Validate Header Options
        header_options = {
            "User Management": '//li[@class="oxd-topbar-body-nav-tab --parent --visited"]',
            "Job": '//a[contains(text(),"Job")]',
            "Organization": '//a[contains(text(),"Organization")]',
            "Qualifications": '//a[contains(text(),"Qualifications")]',
            "Nationalities": '//a[contains(text(),"Nationalities")]',
            "Corporate Banking": '//a[contains(text(),"Corporate Banking")]',
            "Configuration": '//a[contains(text(),"Configuration")]'
        }

        for header, xpath in header_options.items():
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            assert element.is_displayed(), f"{header} header is not displayed"
            print(f"SUCCESS # {header} HEADER PRESENT")

        driver.close()

TD = TestAdminPageHeaders()
TD.tc_pim_02()
