from playwright.sync_api import Page


class AdminMenuComponent:

	def __init__(self, page: Page):
		self.page = page
		self.rooms_link = page.locator('text=Rooms')
		self.report_link = page.locator('id=reportLink')
		self.branding_link = page.locator('id=brandingLink')
		self.inbox_link = page.locator('css=fa fa-inbox')
		self.frontpage_link = page.get_by_role("link", name="Front Page")
		self.logout_link = page.locator('text=Logout')

	def press_rooms_link(self):
		self.rooms_link.click()

	def press_report_link(self):
		self.report_link.click()

	def press_branding_link(self):
		self.branding_link.click()

	def press_inbox_link(self):
		self.inbox_link.click()

	def press_frontpage_link(self):
		self.frontpage_link.click()

	def press_logout_link(self):
		self.logout_link.click()
