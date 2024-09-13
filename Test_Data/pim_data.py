# This file consists of test datas.
# Python Class for Username and Password
class LoginData:
    url = "https://opensource-demo.orangehrmlive.com"
    username = "Admin"
    password = "admin123"


# Python Class for Selenium Selectors
class ElementLocators:
    # default login locators
    xpath_username = '//input[@name="username"]'
    xpath_password = '//input[@type="password"]'
    xpath_login = '//button[@type="submit"]'

    # xpath of menu items
    xpath_menu_items = '//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]'

    # click user management
    xpath_of_user_management = '//li[@class="oxd-topbar-body-nav-tab --parent --visited"]'
    # click user menu
    xpath_of_user_menu = '//a[@role="menuitem"]'
    xpath_of_user_role_dropdown = '//div[@class="oxd-grid-4 orangehrm-full-width-grid"]//div[2]//div//div[2]//div//div//div//i'
    xpath_of_admin_value = '//div[@class="oxd-grid-item oxd-grid-item--gutters"][2]/div/div[2]/div/div[2]/div[2]'
    xpath_of_ess_value = '//div[@class="oxd-grid-item oxd-grid-item--gutters"][2]/div/div[2]/div/div[2]/div[3]'
    xpath_of_status_dropdown = '//div[@class="oxd-grid-4 orangehrm-full-width-grid"]//div[4]//div//div[2]//div//div//div//i'
    xpath_of_enabled_dropdown = '//div[@class="oxd-grid-item oxd-grid-item--gutters"][4]/div/div[2]/div/div[2]/div[2]'
    xpath_of_disabled_dropdown = '//div[@class="oxd-grid-item oxd-grid-item--gutters"][4]/div/div[2]/div/div[2]/div[3]'

   # Forgot Password test locators
    xpath_forgot_password_link = '//p[@class="oxd-text oxd-text--p orangehrm-login-forgot-header"]'
    xpath_username_textbox = '//input[@name="username"]'
    xpath_reset_password_button = '//button[@type="submit"]'
    xpath_reset_success_message = '//p[contains(text(),"Reset Password link sent successfully")]'

    # locators for header options on Admin page 
    xpath_of_job_header = '//a[contains(text(),"Job")]'
    xpath_of_organization_header = '//a[contains(text(),"Organization")]'
    xpath_of_qualifications_header = '//a[contains(text(),"Qualifications")]'
    xpath_of_nationalities_header = '//a[contains(text(),"Nationalities")]'
    xpath_of_corporate_banking_header = '//a[contains(text(),"Corporate Banking")]'
    xpath_of_configuration_header = '//a[contains(text(),"Configuration")]'

    # locators for side menu options on Admin page 
    xpath_of_admin_menu = '//a[@class="oxd-main-menu-item active" and @href="/web/index.php/admin/viewAdminModule"]'
    xpath_of_pim_menu = '//a[@class="oxd-main-menu-item" and @href="/web/index.php/pim/viewPimModule"]'
    xpath_of_leave_menu = '//a[@class="oxd-main-menu-item" and @href="/web/index.php/leave/viewLeaveModule"]'
    xpath_of_time_menu = '//a[@class="oxd-main-menu-item" and @href="/web/index.php/time/viewTimeModule"]'
    xpath_of_recruitment_menu = '//a[@class="oxd-main-menu-item" and @href="/web/index.php/recruitment/viewRecruitmentModule"]'
    xpath_of_my_info_menu = '//a[@class="oxd-main-menu-item" and @href="/web/index.php/pim/viewMyDetails"]'
    xpath_of_performance_menu = '//a[@class="oxd-main-menu-item" and @href="/web/index.php/performance/viewPerformanceModule"]'
    xpath_of_dashboard_menu = '//a[@class="oxd-main-menu-item" and @href="/web/index.php/dashboard/index"]'
    xpath_of_directory_menu = '//a[@class="oxd-main-menu-item" and @href="/web/index.php/directory/viewDirectory"]'
    xpath_of_maintenance_menu = '//a[@class="oxd-main-menu-item" and @href="/web/index.php/maintenance/viewMaintenanceModule"]'
    xpath_of_buzz_menu = '//a[@class="oxd-main-menu-item" and @href="/web/index.php/buzz/viewBuzz"]'
