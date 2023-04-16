# Задайте список из нескольких чисел. # Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12




# list = [2, 3, 5, 9, 3]
# sum = 0
# for i in range (1, len(list),2):
#     if list[i]%2!=0:
#       sum+=list[i]

# print(list)
# print(F'ОТВЕТ: {sum}')


# новый код
list = [2, 3, 5, 9, 3]
list1 = []
count = 0

for count, i  in enumerate(list):
    if count%2!=0:
      list1.append(i)
      count+=1  
      result = sum(list1)
print(list)
print(F'ОТВЕТ: {result}')




