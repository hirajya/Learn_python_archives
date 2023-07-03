def swap(a, b, data_list):
    data_list[b], data_list[a] = data_list[a], data_list[b]


def partition(data_list, start_idx, end_idx):
    pivot_idx = start_idx

    while start_idx < end_idx:
        while start_idx < len(data_list) and data_list[start_idx] <= data_list[pivot_idx]:
            start_idx += 1

        while data_list[end_idx] > data_list[pivot_idx]:
            end_idx -= 1

        if start_idx < end_idx:
            swap(start_idx, end_idx, data_list)

    swap(end_idx, pivot_idx, data_list)

    return end_idx


def quicksort(data_list, start_idx, end_idx):
    if start_idx < end_idx:
        pi = partition(data_list, start_idx, end_idx)
        quicksort(data_list, start_idx, pi - 1)         # left part
        quicksort(data_list, pi + 1, end_idx)           # right part


if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    quicksort(elements, 0, len(elements) - 1)
    print(elements)
