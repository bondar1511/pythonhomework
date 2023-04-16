# A. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, 
# то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# B. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]

import random
# from venv import create
# k = int(input('Введите натуральную степень: '))

# # with open('text1.txt', 'w') as data:
# #   data.write(str)
# def create_list(k):
#  list = []
#  for i in range(k+1):
#   list.append(random.randint(0,100))
#  return list
# print(list)

# def create_str(sp):
#     list = sp[::-1]
#     str = ''
#     if len(list) <1:
#         str = 'x=0'
#     else:    
#      for i in range (len(list)):
#       if i !=len(list)-1 and list[i] !=0 and i != len(list) -2:
#             str += f'{list[i]}*x + '
#       elif i==list[-1]:
#         str += f'{list[i]} + '
#      else:
#         str +=f'{list[i]}*x**{k} +' 

#     str = str[:-3]
#     str +=f' = 0'
#     print(str)


k = int(input('Введите натуральную степень: '))
polynomial = {}

for i in range(k,-1,-1):
   polynomial[i] = random.randint(0,100)
print(polynomial)
str = ''

for k,v in polynomial.items():
    if k == 1:
        str += f'{v}*x + '
    elif k==0:
        str += f'{v} + '
    else:
        str +=f'{v}*x**{k} + '
   
else:
   str = str[:-3]
   str +=f' = 0'

print(str)

with open('text.txt', 'w') as data:
  data.write(str)
new_str = str.split()
print(new_str)
def conv(new_str):
 new_str =[]
 for i in range(len(str)):
    new_str.append(str[i].replace('+', '').replace('=','').replace('0',''))                    
 return new_str


k = int(input('Введите натуральную степень: '))
polynomial1 = {}
for i in (range(k,-1,-1)):
   polynomial1[i] = random.randint(-100,100)
print(polynomial1)
str1 = ''
for k,v in polynomial1.items():
   if k == 1:
         str1 += f'{v}*x**{k} + '
   elif k==0:
          str1 += f'{v} + '
   else:
          str1 +=f'{v}*x + '
else:
    str1 = str1[:-3]
    str1 +=f' = 0'
print(str1)
with open('text.txt', 'w') as data:
  data.write(str1)
new_str1 = str1.split()

print(new_str1)
def conv(new_str1):
 new_str1 =[]
 for i in range(len(str1)):
    new_str1.append(str1[i].replace('+', '').replace('=','').replace('0',''))                    
 return new_str1

# sum = 0
# for i in range (len(new_str)):
#    if new_str[i]== 

# def addpoly(str,str1):
#     sum = 0
# if len(str)==0:
#     return str1
