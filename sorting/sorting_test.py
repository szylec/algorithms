import sys
import unittest
import sorting
from unittest import mock

class TestSorting(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.sorting = sorting.Sorting()
		cls.mock_list_to_sort = [3, 8, 3, 6, 1]
		cls.mock_sorted_list = [1, 3, 3, 6, 8]

	def test_count_number_of_elements(self):
		self.assertEqual(
			self.sorting.count_number_of_elements(self.mock_list_to_sort), 5)

	def test_prepare_to_print(self):
		string_list = self.sorting.prepare_to_print(self.mock_list_to_sort)
		self.assertEqual(string_list[0], "[")  # If first char is "["
		self.assertEqual(string_list[-1], "]")  # If last char is "]"

	@mock.patch.object(sorting.Sorting, "bubble_sort")
	def test_execute_and_show_results(self, mock_bubble_sort):
		self.sorting.execute_and_show_results(
			'bubble', mock_bubble_sort, self.mock_list_to_sort)
		self.assertTrue(mock_bubble_sort.called)

	def test_bubble_sort(self):
		sorted_list = self.sorting.bubble_sort(
			self.mock_list_to_sort)
		self.assertEqual(sorted_list, self.mock_sorted_list)

	def test_selection_sort(self):
		sorted_list = self.sorting.selection_sort(
			self.mock_list_to_sort)
		self.assertEqual(sorted_list, self.mock_sorted_list)

	def test_insertion_sort(self):
		sorted_list = self.sorting.insertion_sort(
			self.mock_list_to_sort)
		self.assertEqual(sorted_list, self.mock_sorted_list)
		
if __name__ == "__main__":
	unittest.main()
