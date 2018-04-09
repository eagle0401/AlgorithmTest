LARGE = False
SMALL = True


def bubble_sort(sort_list, sort_by=LARGE):
    if type(sort_list) is not list:
        return

    list_len = len(sort_list)
    if sort_by:
        for i in range(list_len - 1):
            for j in range(1, list_len - i):
                if sort_list[j] > sort_list[j - 1]:
                    sort_list[j - 1], sort_list[j] = sort_list[j], sort_list[j - 1]
    else:
        for i in range(list_len - 1):
            for j in range(1, list_len - i):
                if sort_list[j] < sort_list[j - 1]:
                    sort_list[j - 1], sort_list[j] = sort_list[j], sort_list[j - 1]


def exchange_sort(sort_list, sort_by=LARGE):
    if type(sort_list) is not list:
        return

    list_len = len(sort_list)
    if sort_by:
        for i in range(list_len):
            for j in range(i + 1, list_len):
                list_i, list_j = sort_list[i], sort_list[j]
                if list_i < list_j:
                    sort_list[j], sort_list[i] = list_i, list_j
    else:
        for i in range(list_len):
            for j in range(i + 1, list_len):
                list_i, list_j = sort_list[i], sort_list[j]
                if list_i > list_j:
                    sort_list[j], sort_list[i] = list_i, list_j


def selection_sort(sort_list, sort_by=LARGE):
    if type(sort_list) is not list:
        return

    list_len = len(sort_list)
    if sort_by:
        for i in range(list_len):
            biggest_index = i
            for j in range(i + 1, list_len):
                if sort_list[biggest_index] < sort_list[j]:
                    biggest_index = j
            sort_list[i], sort_list[biggest_index] = sort_list[biggest_index], sort_list[i]
    else:
        for i in range(list_len):
            smallest_index = i
            for j in range(i + 1, list_len):
                if sort_list[smallest_index] > sort_list[j]:
                    smallest_index = j
            sort_list[i], sort_list[smallest_index] = sort_list[smallest_index], sort_list[i]


def insertion_sort(sort_list, sort_by=LARGE):
    if type(sort_list) is not list:
        return

    list_len = len(sort_list)
    if sort_by:
        for i in range(list_len - 1):
            i_plus = sort_list[i + 1]
            if sort_list[i] < i_plus:
                for j in range(i + 1):
                    if sort_list[j] > i_plus:
                        continue
                    sort_list.pop(i + 1)
                    sort_list.insert(j, i_plus)
                    break
    else:
        for i in range(list_len - 1):
            i_plus = sort_list[i + 1]
            if sort_list[i] > i_plus:
                for j in range(i + 1):
                    if sort_list[j] < i_plus:
                        continue
                    sort_list.pop(i + 1)
                    sort_list.insert(j, i_plus)
                    break


def quick_sort(sort_list, sort_by=LARGE):
    if type(sort_list) is not list:
        return

    _quick_sort_(sort_list, 0, len(sort_list), sort_by)


def _quick_sort_(sort_list, from_index, to_index, sort_by):
    if to_index == from_index:
        return

    pivot_index = from_index
    pivot_value = sort_list[from_index]

    if sort_by:
        for i in range(from_index + 1, to_index):
            if sort_list[i] > pivot_value:
                pivot_index += 1
                sort_list[pivot_index], sort_list[i] = sort_list[i], sort_list[pivot_index]
    else:
        for i in range(from_index + 1, to_index):
            if sort_list[i] < pivot_value:
                pivot_index += 1
                sort_list[pivot_index], sort_list[i] = sort_list[i], sort_list[pivot_index]

    sort_list[pivot_index], sort_list[from_index] = pivot_value, sort_list[pivot_index]

    if pivot_index > from_index:
        _quick_sort_(sort_list, from_index, pivot_index, sort_by)
    if pivot_index < to_index:
        _quick_sort_(sort_list, pivot_index + 1, to_index, sort_by)


def shell_sort(sort_list, sort_by=LARGE):
    list_len = len(sort_list)
    gap = list_len // 2

    if sort_by:
        while gap > 0:
            for i in range(gap, list_len):
                temp = sort_list[i]
                j = i
                while j >= gap and sort_list[j - gap] < temp:
                    sort_list[j] = sort_list[j - gap]
                    j -= gap
                sort_list[j] = temp
            gap = gap // 2
    else:
        while gap > 0:
            for i in range(gap, list_len):
                temp = sort_list[i]
                j = i
                while j >= gap and sort_list[j - gap] > temp:
                    sort_list[j] = sort_list[j - gap]
                    j -= gap
                sort_list[j] = temp
            gap = gap // 2


def default_sort(sort_list, sort_by=LARGE):
    sort_list.sort()