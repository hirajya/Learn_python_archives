numbers = [5, 3, 7, 1, 8, 3, 34, 5, 64, 234, 767, 34, 87, 142, 234, 4, 5, 999]
numbers = sorted(numbers)
print(numbers)


def binary_search_idx(data_list, found_number):
    left_idx = 0
    right_idx = len(data_list) - 1
    mid_idx = 0

    list_idx = []
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        mid_number = data_list[mid_idx]

        if mid_number == found_number:
            return mid_idx

        if mid_number < found_number:
            left_idx = mid_idx + 1

        else:
            right_idx = mid_idx - 1

    return -1


def find_all_occurances(data_list, found_data):
    index = binary_search_idx(data_list, found_data)
    list_occurances = [index]

    i = index - 1

    while i >= 0:
        if numbers[i] == found_data:
            list_occurances.append(i)
        else:
            break
        i -= 1

    i = index + 1

    while i < len(data_list):
        if numbers[i] == found_data:
            list_occurances.append(i)
        else:
            break
        i += 1

    return sorted(list_occurances)


def binary_search_idx_recursive(data_list, number_to_find, left_idx, right_idx):
    mid_idx = (left_idx + right_idx) // 2
    mid_number = data_list[mid_idx]

    if right_idx < left_idx:
        return -1

    if mid_number == number_to_find:
        return mid_idx

    if mid_number < number_to_find:
        left_idx = mid_idx + 1

    else:
        right_idx = mid_idx - 1

    return binary_search_idx_recursive(data_list, number_to_find, left_idx, right_idx)


print(find_all_occurances(numbers, 5))
