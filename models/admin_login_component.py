from playwright.sync_api import Page


class AdminLoginPage:

	def __init__(self, page: Page):
		self.page = page
		self._username_input = page.locator('id=username')
		self._password_input = page.locator('id=password')
		self._login_button = page.get_by_test_id('submit')

	def navigate(self):
		self.page.goto('https://automationintesting.online/#/admin')

	def fill_username(self, u_name):
		self._username_input.fill(u_name)

	def fill_password(self, p_word):
		self._password_input.fill(p_word)

	def click_login_button(self):
		self._login_button.click()
