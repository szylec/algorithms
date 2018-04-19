
import sys

LIST_TO_SORT = [5,4,2,6,7,1,9,3,7,2]

def prepare_to_print(list):
    """Prepares list to be print nicely."""
    return '[{}]'.format(', '.join(map(str, list)))


def count_number_of_elements(list_to_count):
    return len(list_to_count)


def calculate_and_show_results(
        algorithm_name,
        algorithm_fn,
        list_to_sort):
    """Present results of sorting algorithm."""
    print("Algorithm: {}. Sorted list.".format(algorithm_name))
    sorted_list = algorithm_fn(list_to_sort)
    print(prepare_to_print(sorted_list))
    print("\n")


def bubble_sort(list_to_sort):
    """Bubble sort algorithm."""
    number_of_elements = count_number_of_elements(list_to_sort)
    sorted_list = list(list_to_sort)
    is_changed = True
    while is_changed:
        is_changed = False
        for i in range(number_of_elements - 1):
            current_value = sorted_list[i]
            if sorted_list[i] > sorted_list[i + 1]:
                sorted_list[i] = sorted_list[i + 1]
                sorted_list[i + 1] = current_value
                is_changed = True
    return sorted_list


def selection_sort(list_to_sort):
    """Selection sort algorithm."""
    number_of_elements = count_number_of_elements(list_to_sort)
    sorted_list = []
    for element in range(number_of_elements):
        current_min = min(list_to_sort)
        sorted_list.append(current_min)
        list_to_sort.remove(current_min)
    return sorted_list


def insertion_sort():
    return True


def main(argv):
    print("List to sort.")
    print(prepare_to_print(LIST_TO_SORT))
    print("\n")

    calculate_and_show_results(
        'bubble',
        bubble_sort,
        LIST_TO_SORT)    
    calculate_and_show_results(
        'selection',
        selection_sort,
        LIST_TO_SORT)    


if __name__ == "__main__":
    main(sys.argv)
