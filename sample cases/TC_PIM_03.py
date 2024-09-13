from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSideMenuValidation:
    def tc_pim_03(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)

        # Load OrangeHRM webpage
        orange_hrm_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(orange_hrm_url)

        # Login as Admin
        driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("Admin")
        driver.find_element(By.XPATH, '//input[@type="password"]').send_keys("admin123")
        driver.find_element(By.XPATH, '//button[@type="submit"]').click()

        # Click Admin button to navigate to Admin page
        admin_button = driver.find_element(By.XPATH, '//a[@class="oxd-main-menu-item" and @href="/web/index.php/admin/viewAdminModule"]')
        admin_button.click()

        # Validate all side menu options
        menu_options = {
            "Admin": '//a[@class="oxd-main-menu-item active" and @href="/web/index.php/admin/viewAdminModule"]',
            "PIM": '//a[@class="oxd-main-menu-item" and @href="/web/index.php/pim/viewPimModule"]',
            "Leave": '//a[@class="oxd-main-menu-item" and @href="/web/index.php/leave/viewLeaveModule"]',
            "Time": '//a[@class="oxd-main-menu-item" and @href="/web/index.php/time/viewTimeModule"]',
            "Recruitment": '//a[@class="oxd-main-menu-item" and @href="/web/index.php/recruitment/viewRecruitmentModule"]',
            "My Info": '//a[@class="oxd-main-menu-item" and @href="/web/index.php/pim/viewMyDetails"]',
            "Performance": '//a[@class="oxd-main-menu-item" and @href="/web/index.php/performance/viewPerformanceModule"]',
            "Dashboard": '//a[@class="oxd-main-menu-item" and @href="/web/index.php/dashboard/index"]',
            "Directory": '//a[@class="oxd-main-menu-item" and @href="/web/index.php/directory/viewDirectory"]',
            "Maintenance": '//a[@class="oxd-main-menu-item" and @href="/web/index.php/maintenance/viewMaintenanceModule"]',
            "Buzz": '//a[@class="oxd-main-menu-item" and @href="/web/index.php/buzz/viewBuzz"]'
        }

        for menu, xpath in menu_options.items():
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            assert element.is_displayed(), f"{menu} menu option not visible"
            print(f"SUCCESS # {menu} MENU OPTION IS VISIBLE")

        driver.close()

TD = TestSideMenuValidation()
TD.tc_pim_03()
