# 2.	Задайте список из n чисел последовательности (1 + 1/n)**n, 
# выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# n = float(input('Введите число: '))
# # list =[]
# sum = 0
# for i in range(n, ((1+1/n)**n)):
     
#  for i in list:
#   while i<len(list):
#      sum = list[i]+sum
#      i+=1
# print(list)
# print(sum)


# новый код

n = float(input('Введите число: '))
sum = 0
list =[x for x in range(n, (1+1/n)**n)]
for i in list:
  while i<len(list):
     sum = lambda i, sum: i+sum 
     i+=1
print(list)
print(sum)