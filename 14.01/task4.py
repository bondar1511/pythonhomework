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

import math

# площадь круга
def circle_diameter(dim):
    return math.pi *pow((dim/2),2)
# длина окружности
def circumference(diameter):
  return 3.14*diameter
diameter = 999 
print(circle_diameter(diameter))
print(circumference(diameter))
