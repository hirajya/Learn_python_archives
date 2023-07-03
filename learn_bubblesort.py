def bubble_sort(elements):
    size = len(elements)

    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
                swapped = True

        if not swapped:
            break


if __name__ == '__main__':
    elements = [5, 9, 2, 1, 67, 34, 88, 34]
    elements = [1, 2, 3, 4, 2]
    elements = ["mona", "dhaval", "aamir", "tina", "chang"]

    # def bubble_sort(data_list, key):
    #     size = len(data_list)
    #     for i in range(size - 1):
    #         swapped = False
    #         for j in range(size - 1 - i):
    #             if data_list[j][key] > data_list[j + 1][key]:
    #                 data_list[j][key], data_list[j + 1][key] = data_list[j + 1][key], data_list[j][key]
    #                 swapped = True
    #
    #         if not swapped:
    #             break
    #
    #     return data_list
    #
    #
    # if __name__ == '__main__':
    #     elements = [
    #         {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
    #         {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
    #         {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
    #         {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
    #     ]
    #
    #     print(bubble_sort(elements, 'device'))
