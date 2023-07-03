def shell_sort(arr):
    size = len(arr)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j - gap] > anchor:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2


if __name__ == '__main__':
    test = [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1, 34, 54, 1, 2, 32, 12, 7, 1, 23, 5, 456, 7, 1, 35, 6, 8,
            234, 23, 4, 234, 23, 4, 34, 1]

    shell_sort(test)
    print(test)

#
# def shell_sort(arr):
#     n = len(arr)
#     div = 2
#     gap = n // div
#     while gap > 0:
#         index_to_delete = []
#         for i in range(gap, n):
#             temp = arr[i]
#             j = i
#             while j >= gap and arr[j - gap] >= temp:
#                 if arr[j - gap] == temp:
#                     index_to_delete.append(j)
#                 arr[j] = arr[j - gap]
#                 j -= gap
#             arr[j] = temp
#         index_to_delete = list(set(index_to_delete))
#         index_to_delete.sort()
#         if index_to_delete:
#             for i in index_to_delete[-1::-1]:
#                 del arr[i]
#         div *= 2
#         n = len(arr)
#         gap = n // div
#
#
# if __name__ == '__main__':
#     elements = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
#
#     print(f'Given unsorted list: {elements}')
#     shell_sort(elements)
#     print(f'List after Sorting : {elements}')
