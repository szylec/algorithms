import sys

class Sorting(object):

    def __init__(self):
        self.example_list_to_sort = [5, 4, 2, 6, 7, 1, 9, 3, 7, 2]

    @staticmethod
    def prepare_to_print(list):
        """Prepares list to be print nicely."""
        return '[{}]'.format(', '.join(map(str, list)))

    @staticmethod   
    def count_number_of_elements(list_to_count):
        return len(list_to_count)

    def execute_and_show_results(self, algorithm_name, algorithm_fn, list_to_sort):
        """Executes sorting algorithm and shows results."""
        print("Algorithm: {} sort. Sorted list.".format(algorithm_name))
        sorted_list = algorithm_fn(list_to_sort)
        print(self.prepare_to_print(sorted_list))
        print("\n")

    def bubble_sort(self, list_to_sort):
        """Bubble sort algorithm."""
        number_of_elements = self.count_number_of_elements(list_to_sort)
        sorted_list = list(list_to_sort)  # list() to make sure this is a real copy
        is_changed = True
        while is_changed:
            is_changed = False
            for i in range(number_of_elements - 1):
                temp = sorted_list[i]
                if sorted_list[i] > sorted_list[i + 1]:
                    sorted_list[i] = sorted_list[i + 1]
                    sorted_list[i + 1] = temp
                    is_changed = True
        return sorted_list

    def selection_sort(self, list_to_sort):
        """Selection sort algorithm."""
        number_of_elements = self.count_number_of_elements(list_to_sort)
        list_to_sort_copy = list(list_to_sort)
        sorted_list = []
        for element in range(number_of_elements):
            current_min = min(list_to_sort_copy)
            sorted_list.append(current_min)
            list_to_sort_copy.remove(current_min)
        return sorted_list

    def insertion_sort(self, list_to_sort):
        """Insertion sort algorithm."""
        number_of_elements = self.count_number_of_elements(list_to_sort)
        sorted_list = list(list_to_sort)
        for iterator in range(number_of_elements):
            comparator = iterator - 1
            while comparator >= 0:
                if sorted_list[iterator] < sorted_list[comparator]:
                    temp = sorted_list[iterator]
                    sorted_list[iterator] = sorted_list[comparator]
                    sorted_list[comparator] = temp
                comparator -= 1
                iterator -= 1
        return sorted_list


def main(argv):
    sorting = Sorting()
    LIST_TO_SORT = sorting.example_list_to_sort

    print("List to sort.")
    print(sorting.prepare_to_print(LIST_TO_SORT))
    print("\n")

    # Bubble sort.
    sorting.execute_and_show_results('bubble', sorting.bubble_sort, LIST_TO_SORT)

    # Selection sort.
    sorting.execute_and_show_results('selection', sorting.selection_sort, LIST_TO_SORT)    

    # Insertion sort.
    sorting.execute_and_show_results('insertion', sorting.insertion_sort, LIST_TO_SORT)


if __name__ == "__main__":
    main(sys.argv)
