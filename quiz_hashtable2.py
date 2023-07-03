import csv

with open("C:\\Users\\user\\Downloads\\nyc.txt", "r") as f:
    file_reader = csv.DictReader(f)
    date = []
    temp = []
    for line in file_reader:
        date.append(line['date'])
        temp.append(line['temperature(F)'])



class HashTable:
    def __init__(self):
        self.Max = 100
        self.arr = [[] for i in range(self.Max)]

    def get_hash(self, key):
        hash_key = 0
        for char in key:
            hash_key += ord(char)
        return hash_key % self.Max

    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]

    def __setitem__(self, key, value):
        arr_index = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[arr_index]):
            if len(element) == 2 and element == 0:
                self.arr[arr_index][idx] = (key, value)
                found = True
        if not found:
            self.arr[arr_index].append((key, value))

    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for idx, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print('del', idx)
                del self.arr[arr_index][idx]

    def insert_data_list(self, x_list, y_list):
        for i in range(len(x_list)):
            self.__setitem__(x_list[i], y_list[i])


ht = HashTable()
ht.insert_data_list(date, temp)
print(ht.__getitem__('Jan 9'))
print(ht.__getitem__('Jan 4'))

