from .base import FunctionalTest


class LayoutAndSytlingTest(FunctionalTest):

	def test_layout_and_styling(self):
		# Edith goes to the home page
		self.browser.get(self.server_url)
		## The dimensions are different than what is in the book because there
		## was some odd aspect ratio thing going on that would cause the test
		## to fail
		self.browser.set_window_size(1044, 768)

		# She notices the input box is nicely centered
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(
			inputbox.location['x'] + inputbox.size['width'] / 2,
			512,
			delta=5
		)

		# She starts a new list and sees the input is nicely
		# centered there too
		inputbox.send_keys('testing\n')
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(
			inputbox.location['x'] + inputbox.size['width'] / 2,
			512,
			delta=5
		)




