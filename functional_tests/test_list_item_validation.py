from .base import FunctionalTest
from unittest import skip


class ItemValidationTest(FunctionalTest):

	def test_cannot_add_empty_list_items(self):
		# Edit goes to teh home page and accidentally tries to submit
		# an empty list item. She hits Enter on the empty input box

		# The home page refreshes, and there is an error message saying
		# that list items cannot be blank

		# She tries again with some text for the item, which now works

		# Perversely, she now decides to submit a second blank list item

		# She receives a similar warning on the last page

		# And she can correct it by filling in some text
		self.fail('write me!')
