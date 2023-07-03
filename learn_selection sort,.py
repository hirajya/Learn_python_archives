from timeit import timeit


def selection_algo(arr):
    size = len(arr)
    for i in range(size - 1):
        min_idx = i
        for j in range(min_idx + 1, size):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if i != min_idx:
            arr[min_idx], arr[i] = arr[i], arr[min_idx]


def selection_dict(arr, key):
    size = len(arr)
    for i in range(size - 1):
        min_idx = i
        for j in range(min_idx + 1, size):
            if arr[j][key] < arr[min_idx][key]:
                min_idx = j

        if i != min_idx:
            arr[min_idx], arr[i] = arr[i], arr[min_idx]


def multilevel_selection_sort(elements, sort_by_list):
    for sort_by in sort_by_list[-1::-1]: #LAST NAME
        for x in range(len(elements)): #DICTIONARIES
            min_index = x
            for y in range(x, len(elements)):
                if elements[y][sort_by] < elements[min_index][sort_by]:
                    min_index = y
            if x != min_index:
                elements[x], elements[min_index] = elements[min_index], elements[x]


if __name__ == '__main__':
    # elements = [
    #     {'First Name': 'Raj', 'Last Name': 'Nayyar', 'Middle Initial': 'Q.'},
    #     {'First Name': 'Suraj', 'Last Name': 'Sharma', 'Middle Initial': 'Y.'},
    #     {'First Name': 'Karan', 'Last Name': 'Kumar', 'Middle Initial': 'V.'},
    #     {'First Name': 'Jade', 'Last Name': 'Canary', 'Middle Initial': 'P.'},
    #     {'First Name': 'Raj', 'Last Name': 'Thakur', 'Middle Initial': 'O.'},
    #     {'First Name': 'Raj', 'Last Name': 'Sharma', 'Middle Initial': 'K.'},
    #     {'First Name': 'Kiran', 'Last Name': 'Kamla', 'Middle Initial': 'G.'},
    #     {'First Name': 'Armaan', 'Last Name': 'Kumar', 'Middle Initial': 'M.'},
    #     {'First Name': 'Jaya', 'Last Name': 'Sharma', 'Middle Initial': 'Z.'},
    #     {'First Name': 'Ingrid', 'Last Name': 'Galore', 'Middle Initial': 'N.'},
    #     {'First Name': 'Jaya', 'Last Name': 'Seth', 'Middle Initial': 'V.'},
    #     {'First Name': 'Armaan', 'Last Name': 'Dadra', 'Middle Initial': 'A.'},
    #     {'First Name': 'Ingrid', 'Last Name': 'Maverick', 'Middle Initial': 'A.'},
    #     {'First Name': 'Aahana', 'Last Name': 'Arora', 'Middle Initial': 'S.'}
    # ]

    elements = [
        {'First Name': 'Rod', 'Last Name': 'Est', 'Middle Initial': 'D.'},
        {'First Name': 'Ara', 'Last Name': 'Tenorio', 'Middle Initial': 'D.'},
        {'First Name': 'Ang', 'Last Name': 'Boo', 'Middle Initial': 'T.'},
        {'First Name': 'Foo', 'Last Name': 'Ele', 'Middle Initial': 'P.'}
    ]

    print(f'Given unsorted array:', *elements, sep='\n')
    multilevel_selection_sort(
        elements, ['Last Name', 'First Name', 'Middle Initial'])
    print(f'Array after Multi-Level Sorting:', *elements, sep='\n')

    selection_dict(elements, 'First Name')
    print(*elements, sep='\n')

    code_basic_time = timeit(lambda: multilevel_selection_sort(elements, ['First Name', 'Last Name']), number=10000)
    my_code_time = timeit(lambda: selection_dict(elements, 'First Name'), number=10000)

    print(f'My fucking code time{my_code_time:.3f}')
    print(f'My code basic time{code_basic_time:.3f}')