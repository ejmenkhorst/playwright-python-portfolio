from playwright.sync_api import Page, expect

from models.admin_login_component import AdminLoginPage
from models.admin_menu_component import AdminMenuComponent


def test_successful_login_role_admin(page: Page):
	# ARRANGE
	login_page = AdminLoginPage(page)
	admin_menu = AdminMenuComponent(page)
	login_page.navigate()

	# ACT
	login_page.fill_username("admin")
	login_page.fill_password("password")
	login_page.click_login_button()

	# ASERT
	expect(admin_menu.frontpage_link).to_be_visible()
