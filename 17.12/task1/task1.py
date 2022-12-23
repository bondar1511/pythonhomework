# 1.	Напишите программу, которая принимает 
# на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

n = (input('Введите число: '))
num = str(n)
num_str = list(num)
lst_num = map(int, num_str)
result = sum(lst_num)
print(list)
print(result)
