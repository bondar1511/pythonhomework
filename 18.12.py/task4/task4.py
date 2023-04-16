# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# # 2 -> 10
# num = int(input('Введите число:  '))
# number = ' '
# while num >0:
#     number = str(num%2) + number
#     num = num//2
# print(number)


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

num = int(input('Введите число:  '))
number = ' '
if num > 0:
    number = list(lambda num: not num%2 + number) 
    num = list(lambda num: not num//2)
print(number)