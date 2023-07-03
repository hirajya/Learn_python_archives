import statistics as s


def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = anchor


def running_median(data_list):
    arr_data = []
    for i in range(0, len(data_list)):
        arr_data.append(data_list[i])
        insertion_sort(arr_data)
        print(s.median(arr_data))


if __name__ == '__main__':
    tests = [2, 1, 5, 7, 2, 0, 5]

    running_median(tests)
