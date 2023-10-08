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
from itertools import chain, combinations




def find_combinations(m_dict, max_weight):
 sorted_items = sorted(m_dict, key=lambda x: x[1], reverse=True)

 def find_combinations_re(current_weight, current_comb, rem_items):
   if current_weight<=max_weight:
     result.append(current_comb)
   for i in range(len(rem_items)):
     n_com = current_comb + [rem_items[i]]
     n_weight = current_weight = rem_items[i][1]
     n_remain = rem_items[i+1:]
     find_combinations_re(n_weight, n_com, n_remain)
 result = [] 
 find_combinations_re(0,[], sorted_items)  
 return result
m_dict = {
  "ключи": 0.3,
  "кошелек": 0.4,
  "телефон": 0.6,
  "зарядное устройство": 0.2,
  "зажигалка": 0.1,
  "еда": 1.0,
  "напитки": 1.0,
}
max_weight = 3
combo = find_combinations(m_dict, max_weight)
for com in combo:
  print(com)