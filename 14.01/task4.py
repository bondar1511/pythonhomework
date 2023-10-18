# a =2
# b = "вапвпа"
# print(type(a))
# print(type(b))
# import sys


# data = [54,"test_str", 2.158, True, 54]
# for idx, elem in enumerate(data,1):
#     print(idx,elem, sys.getsizeof(elem), hash(elem))
#     # print(elem)
#     # print(id(elem))
#     # print(sys.getsizeof(elem))
#     # print(hash(elem))
#     if isinstance(elem, int):
#         print("Целое число")
#     if isinstance(elem, str):
#         print("Строка")    

# number = int(input())
# print(bin(number))
# print(oct(number))
# res = ''
# for i in [2, 8]:
#   while number:
#     res = f'{number%i}' + res
#     number //=1
#   print(res)

# import math

# # площадь круга
# def circle_diameter(dim):
#     return math.pi *pow((dim/2),2)
# # длина окружности
# def circumference(diameter):
#   return 3.14*diameter
# diameter = 999 
# print(circle_diameter(diameter))
# print(circumference(diameter))

# lst = [1,2,3,4,5,4,3,2,1]
# result = []
# # print(list(set(lst)))
# for i in lst:
#     if i not in result:
#         result.append(i)
# print(result)
        
# text = input("введите данные: \n")

# if text.isnumeric():
#      print(int(text))
# elif text.replace(".", "",1).isnumeric():
#      print(float(text))    
# elif text[0] == '-' and text.replace('.','',1).replace('-','',1).isnumeric():
#      print(float(text))
# elif not text.islower():
#      print(text.lower())
# else:
#      print(text.upper())


# my_tuple = (123, 2.5, 32, 3.5, 'game', True, 'computer')
# my_dict = {}
# for i in my_tuple:
#     count = my_dict.setdefault(type(i), [])
#     count.append(i)

# print(my_dict)
# lst = sorted(input(). split())
# count = len(max(lst, key=len))

# for k, v in enumerate(lst, 1):
#     print(f'{k} {v:>{count}}')

# print(count)
# print(lst)



# text = input("Введите текст:\n")

# if text.isnumeric():
#     print(int(text))
# elif text.replace(".", "",1).isnumeric():
#     print(float(text))
# elif text[0] == "-" and text.replace(".", "",1).replace("-", "",1).isnumeric():
#     print(float(text))
# elif not text.islower():
#     print(text.lower())
# else:
#     print(text.upper())


# tuple = (123, 2.5, 32, 3.5, "game", True, "computer" ) 

# my_dict = {}

# for i in tuple:
#    count = my_dict.setdefault(type(i), [])
#    count.append(i)
# print(my_dict)

# my_list = [2, 5, 3, 3, 3, 2, 5, 10, 11, 12]
# result = []
# # for i in my_list:
# #     if my_list.count(i) == 2:
# #         for j in range(2):
# #             my_list.remove(i)
# # print(my_list)
# for k, v in enumerate(my_list, 1):
#     if v % 2 != 0:
#         result.append(k)
# print(result)


# lst = sorted(input().split())
# count = len(max(lst, key=len))

# for k, v in enumerate(lst, 1):
#     print(f'{k} {v:>{count}}')
# print(lst)


# word = input ("Ведите строку: ")   

# _dict ={}

# for letter in word:
#     _dict.setdefault(letter, 0)
#     _dict[letter] +=1

# print(_dict)
from collections import Counter
from itertools import chain, combinations




# def find_combinations(m_dict, max_weight):
#  sorted_items = sorted(m_dict, key=lambda x: x[1], reverse=True)

#  def find_combinations_re(current_weight, current_comb, rem_items):
#    if current_weight<=max_weight:
#      result.append(current_comb)
#    for i in range(len(rem_items)):
#      n_com = current_comb + [rem_items[i]]
#      n_weight = current_weight = rem_items[i][1]
#      n_remain = rem_items[i+1:]
#      find_combinations_re(n_weight, n_com, n_remain)
#  result = [] 
#  find_combinations_re(0,[], sorted_items)  
#  return result
# m_dict = {
#   "ключи": 0.3,
#   "кошелек": 0.4,
#   "телефон": 0.6,
#   "зарядное устройство": 0.2,
#   "зажигалка": 0.1,
#   "еда": 1.0,
#   "напитки": 1.0,
# }
# max_weight = 3
# combo = find_combinations(m_dict, max_weight)
# for com in combo:
#   print(com)

# # items = {"ключи": 0.3,
#     "кошелек": 0.2,
#     "телефон": 0.5,
#     "зажигалка": 0.1
# }

# max_weight = 1.0


# def fill_backpack(items, max_weight):
#     table = [[0] * (max_weight + 1) for _ in range(len(items) + 1)]

#     for i in range(1, len(items) + 1):
#       item_weight = items[i - 1]["weight"]
#       item_value = items[i - 1]["value"]

#     for j in range(1, max_weight + 1):
#       if item_weight > j:
#         table[i][j] = table[i - 1][j]
#       else:
#         table[i][j] = max(table[i - 1][j], table[i - 1][j - item_weight] + item_value)

#       backpack = {}
# i, j = len(items), max_weight
# backpack = fill_backpack(items, max_weight)
# while i > 0 and j > 0:
#      if table[i][j] != table[i - 1][j]:
#         item = items[i - 1]["item"]
#         weight = items[i - 1]["weight"]
#         backpack[item] = weight
#         j -= weight
#         i -= 1
            # return backpack


# print(backpack)

# def fill_backpack(things, max_weight):
#     backpack = {}
#     sorted_things = sorted(things.items(), key=lambda x: x[1], reverse=True)

#     for object, weight in sorted_things:
#         if weight <= max_weight:
#            backpack[object] = weight
#            max_weight -= weight

#     return backpack

# def fill_backpack(things, max_weight):
#   things =  {"ключи": 0.3,
#     "кошелек": 0.2,
#     "телефон": 0.5,
#     "зажигалка": 0.1
# }
#   max_weight = 1.0
#   result = fill_backpack(things, max_weight)
#   print(result)

# items = {"ключи": 0.3,
#     "кошелек": 0.2,
#     "телефон": 0.5,
#     "зажигалка": 0.1
# }

# max_weight = 1.0



# backpack = {}


# for item, weight in items.items():
#     if weight <= max_weight:
#         backpack[item] = weight
#         max_weight -= weight

# print(backpack)



# def fibonacci():
#     a, b = 0, 1
#     for i in range(10):
#         yield a
#         a, b = b, a + b


list_name = []
list_salaries = []
list_bonuses = []

for i in range(3):
    names = input()
    salary  = int(input())
    bonus = input()

    list_name.append(names)
    list_salaries.append(salary)
    list_bonuses.append(bonus)
    
def generate_bonus_dict(nameses, salaries, bonuses):
    return{name: salary * float(bonus.rstrip("%"))/100
           for name, salary, bonus in zip(nameses, salaries, bonuses)}


resuilt_dict = generate_bonus_dict(list_name, list_salaries,  list_bonuses)
print(resuilt_dict)
