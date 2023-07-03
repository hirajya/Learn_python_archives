from collections import Counter

a = [1, 2, 3, 4, 1, 1, 2, 3, 4]
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(list(my_counter.elements()))
print(my_counter.most_common())
#
#
# from collections import namedtuple
#
# Lovers = namedtuple('Lovers', 'man, woman')
# Lovers1 = Lovers('Rodney', 'Arabella')
# print(Lovers1)
# print(Lovers1.man, Lovers1.woman)

#
# from collections import OrderedDict
#
# ordered_dict = OrderedDict()
# ordered_dict['a'] = 1
# ordered_dict['b'] = 2
# ordered_dict['c'] = 3
# ordered_dict['d'] = 4
# print(ordered_dict)
#
#
# from collections import defaultdict
#
# d = defaultdict(int)
# d['r'] = 1
# d['a'] = 2
# print(d)

#
# from collections import deque
#
# d = deque()
# d.append(1)
# d.append(2)
# d.appendleft(24)
# d.extend([4, 5, 6])
# d.extendleft([34, 25, 16])
# print(d)
# d.rotate()
# print(d)
# d.rotate(-2)
# print(d)
# collections_module

# list1 = [1, 3, 4, 56, 14, 23, 4, 19, 22]
#
# my_list = list(map(lambda x: x * x, list1))
# my_list1 = [n * n for n in list1]
# print(my_list)
# print(my_list1)
#
# my_list3 = [n for n in list1 if n % 2 == 0]
# print(my_list3)
#
# my_list4 = list(filter(lambda x: x % 2 == 0, list1))
# print(my_list4)
#
# my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(my_list)
#
# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
#
# my_dict = {}
# for name, hero in zip(names, heroes):
#     my_dict[name] = hero
# print(my_dict)
#
# my_dict = {name: hero for name, hero in zip(names, heroes)}
# print(my_dict)
#
# my_set = [n*n for n in list1]
# for i in my_set:
# print(i)
# comprehension

# *args
# def aradney(name: str, age=0, *data):
#     print(name)
#     print(age)
#     print(data)
#
#
# aradney('juanito', 23, 'male', 'caloocan', 231231)
#
#
# **kwargs
# def aradney1(name: str, age=0, **data):
#     print(name)
#     print(age)
#     print(data)
#
#
# aradney1('juanito', 23, gender='male', birthplace='caloocan', number=231231)
# *args & **kwargs







