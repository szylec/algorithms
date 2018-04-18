import sys
import unittest
import sorting

class TestSorting(unittest.TestCase):

	def setUp(self):
		self.list_to_sort = [3,8,3,6,1]

	def test_prepare_to_print(self):
		string_list = sorting.prepare_to_print(self.list_to_sort)
		self.assertEqual(string_list[0], "[")  # If first char is "["
		self.assertEqual(string_list[-1], "]")  # If last char is "]"

	def test_calculate_and_show_results(self):
		pass

	def test_bubble_sort(self):
		sorted_list = sorting.bubble_sort(self.list_to_sort)
		self.assertEqual(sorted_list, [1,3,3,6,8])


if __name__ == "__main__":
	unittest.main()
