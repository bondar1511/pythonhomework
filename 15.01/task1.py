# Задайте список из вещественных чисел. 
# Напишите программу, которая
#  найдёт разницу между максимальным и минимальным 
# значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
#  старый код
# list1 =[1.1, 1.2, 3.1, 5, 10.1]
# max =0
# min = list1[0]
# for i in range (len(list1)):
#     if max< list1[i]:
#      max = list1[i]
#     if min > list1[i]:
#      min = list1[i]
# i+=1
# result = (max-int(max)) - (min- int(max))
# print (list1)
# print (result)

# новый код


list1 =[1.1, 1.2, 3.1, 5, 10.1]
max =0
min = list1[0]
my_list =list(enumerate(list1,0))

max = max(my_list, key=lambda i: i[1])
min = min(my_list, key=lambda i: i[1])
      
result = max - min
print (result)
