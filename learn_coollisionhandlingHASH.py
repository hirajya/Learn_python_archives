# import csv
# import statistics as stat
#
# with open("C:\\Users\\user\\Downloads\\nyc.txt", "r") as f:
#     file_reader = csv.reader(f)
#     next(f)
#     date = []
#     temp = []
#     for line in file_reader:
#         date.append(line[0])
#         temp.append(int(line[1]))
#
#
# def avg_temp_1stWeek():
#     temp_first_week = []
#     for i in range(0, 8):
#         temp_first_week.append((temp[i]))
#     mean = round(stat.mean(temp_first_week), 2)
#     print("The average temperature in first week of Jan is", mean, "Fahrenheit")
#
#
# def max_temp_first_10days():
#     temp_first_week = []
#     for i in range(0, 10):
#         temp_first_week.append((temp[i]))
#     print (max(temp_first_week))
#
#
# avg_temp_1stWeek()
# max_temp_first_10days()

# import csv
#
# with open("C:\\Users\\user\\Downloads\\nyc.txt", "r") as f:
#     file_reader = csv.reader(f)
#     next(f)
#     temp_forecast = {}
#     for line in file_reader:
#         temp_forecast[line[0]] = int(line[1])
#
#
# class HashTable:
#     def __init__(self):
#         self.Max = 100
#         self.arr = [[] for i in range(self.Max)]
#
#     def get_hash(self, key):
#         hash_key = 0
#         for char in key:
#             hash_key += ord(char)
#         return hash_key % self.Max
#
#     def __getitem__(self, key):
#         arr_index = self.get_hash(key)
#         for kv in self.arr[arr_index]:
#             if kv[0] == key:
#                 return kv[1]
#
#     def __setitem__(self, key, value):
#         arr_index = self.get_hash(key)
#         found = False
#         for idx, element in enumerate(self.arr[arr_index]):
#             if len(element) == 2 and element == 0:
#                 self.arr[arr_index][idx] = (key, value)
#                 found = True
#         if not found:
#             self.arr[arr_index].append((key, value))
#
#     def __delitem__(self, key):
#         arr_index = self.get_hash(key)
#         for idx, kv in enumerate(self.arr[arr_index]):
#             if kv[0] == key:
#                 print('del', idx)
#                 del self.arr[arr_index][idx]
#
#     def insert_data_list(self, x_list, y_list):
#         for i in range(len(x_list)):
#             self.__setitem__(x_list[i], y_list[i])
#
#     def dict_add(self, dict_kv):
#         for words, count in dict_kv.items():
#             self.__setitem__(words, count)
#
#
# ht = HashTable()
# ht.dict_add(temp_forecast)
# print(ht.__getitem__('Jan 9'))
# print(ht.__getitem__('Jan 4'))

# with open('C:\\Users\\user\\Downloads\\poem.txt', 'r') as f:
#     word_stats = {}
#     for line in f:
#         tokens = line.split(' ')
#         for token in tokens:
#             token = token.replace('\n', '')
#             if token in word_stats:
#                 word_stats[token] += 1
#             else:
#                 word_stats[token] = 1


# class HashTable:
#     def __init__(self):
#         self.Max = 100
#         self.arr = [[] for i in range(self.Max)]
#
#     def get_hash(self, key):
#         hash_key = 0
#         for char in key:
#             hash_key += ord(char)
#         return hash_key % self.Max
#
#     def __getitem__(self, key):
#         arr_index = self.get_hash(key)
#         for kv in self.arr[arr_index]:
#             if kv[0] == key:
#                 return kv[1]
#
#     def __setitem__(self, key, value):
#         arr_index = self.get_hash(key)
#         found = False
#         for idx, element in enumerate(self.arr[arr_index]):
#             if len(element) == 2 and element == 0:
#                 self.arr[arr_index][idx] = (key, value)
#                 found = True
#         if not found:
#             self.arr[arr_index].append((key, value))
#
#     def __delitem__(self, key):
#         arr_index = self.get_hash(key)
#         for idx, kv in enumerate(self.arr[arr_index]):
#             if kv[0] == key:
#                 print('del', idx)
#                 del self.arr[arr_index][idx]
#
#     def dict_add(self, dict_kv):
#         for words, count in dict_kv.items():
#             self.__setitem__(words, count)
#
#
# ht = HashTable()
# ht.dict_add(word_stats)
# print(ht.__getitem__('diverged'))
# print(ht.__getitem__('in'))
# print(ht.__getitem__('I'))
#


class HashTable:
    def __init__(self):
        self.MAX = 10  # I am keeping size very low to demonstrate linear probing easily but usually the size should be high
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, val)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key, val)
        print(self.arr)

    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]

    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("Hashmap full")

    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return  # item not found so return. You can also throw exception
            if self.arr[prob_index][0] == key:
                self.arr[prob_index] = None

        print(self.arr)


ht = HashTable()

list_value = [3, 4, 2, 7, 8, 3, 5, 6, 9, 4, 5, 7, 8]
final_output = [n*2 for n in list_value if n % 2 == 0]
print(final_output)

