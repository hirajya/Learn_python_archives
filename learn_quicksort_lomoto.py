# def swap(a, b, arr):
#     arr[b], arr[a] = arr[a], arr[b]
#
#
# def quicksort_lomoto(data_list):
#     i = 0
#     p_index = 0
#     pivot = len(data_list) - 1
#
#     while p_index < pivot:
#         while data_list[p_index] > data_list[pivot]:
#             p_index += 1
#             i = p_index
#
#         while data_list[i] < data_list[pivot]:
#             i += i
#
#     swap(p_index, i, data_list)
#
#
# if __name__ == '__main__':
#     elements = [11, 9, 29, 7, 2, 15, 28]
#     quicksort_lomoto(elements)
#     print(elements)

# def swap(a, b, arr):
#     arr[b], arr[a] = arr[a], arr[b]
#
#
# def quicksort_lomoto(a, lo, hi):
#     if hi <= lo < 0:
#         return
#
#     p = partition(a, lo, hi)
#     quicksort_lomoto(a, lo, p - 1)
#     quicksort_lomoto(a, p + 1, hi)
#
#
# def partition(a, lo, hi):
#     pivot = a[hi]
#     i = lo - 1
#
#     for j in range(lo, hi):
#         if a[j] <= pivot:
#             i += 1
#
#         swap(i, j, a)
#     i += 1
#     swap(i, hi, a)
#     return i
#
#
# if __name__ == '__main__':
#     elements = [11, 9, 29, 7, 2, 15, 28]
#     quicksort_lomoto(elements, 0, len(elements) - 1)
#     print(elements)

# This implements quick sort using lomuto partition scheme

def swap(a, b, arr):
    if a != b:
        arr[b], arr[a] = arr[a], arr[b]


def quick_sort(elements, start, end):
    if len(elements) == 1:
        return
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi - 1)
        quick_sort(elements, pi + 1, end)


def partition(elements, start, end):
    pivot = elements[end]
    p_index = start

    for i in range(start, end):
        if elements[i] <= pivot:
            swap(i, p_index, elements)
            p_index += 1

    swap(p_index, end, elements)

    return p_index


if __name__ == '__main__':
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]

    for elements in tests:
        quick_sort(elements, 0, len(elements) - 1)
        print(f'sorted array: {elements}')
