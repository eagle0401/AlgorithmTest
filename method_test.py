import datetime
import random

import algorithem.sort


def sort_test(test_list, sort_method, sorted_list, base_during_time=1):
    test_sort_copy = test_list.copy()
    start_time = datetime.datetime.now()
    sort_method(test_sort_copy)
    end_time = datetime.datetime.now()

    is_same = ''
    current_during_time = end_time - start_time
    if len(sorted_list) is not 0:
        is_same = True
        for index in range(object_counts):
            if test_sort_copy[index] is not sorted_list[index]:
                is_same = False
                break
    else:
        sorted_list += test_sort_copy
        base_during_time = during_time

    print(sort_method.__name__, "%.2f" % (current_during_time / base_during_time), is_same)

    return current_during_time


method_list = [
    algorithem.sort.quick_sort,
    algorithem.sort.shell_sort,
    algorithem.sort.insertion_sort,
    algorithem.sort.selection_sort,
    algorithem.sort.exchange_sort,
    algorithem.sort.bubble_sort,
]

object_counts = 5000
test_sort_list = []
for i in range(object_counts):
    test_sort_list.append(random.random())

test_sort_list_copy = []
during_time = sort_test(test_sort_list, algorithem.sort.default_sort, test_sort_list_copy)

for method in method_list:
    sort_test(test_sort_list, method, test_sort_list_copy, during_time)
