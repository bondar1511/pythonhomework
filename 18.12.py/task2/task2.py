# Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# # [2, 3, 5, 6] => [12, 15]

# list1 = []
# list = []

# for i in range(5):
#   i = int(input (f'Введите {i+1} число:'))
#   list1.append(i)

# for i in range(len(list1)):
#  if(len(list1))%2==0:   
#      result1 = list1[0]*list1[-1]
#      result = (list1[0]+1)*(list1[-1]-1)
#      list= [result1, result]

#  elif(len(list1))%2!=0:
#      result1 = list1[0]*list1[-1]
#      result = (list1[0]+1)*(list1[-1]-1)
#      i=len(list1)//2
#      result2 =list1[i]**2
#      list = [result1, result2, result]
   
# print(list1)  
# print(list)


list1 = []
list = []

for i in range(5):
 i = int(input (f'Введите {i+1} число:'))
 list1.append(i)

for i in range(len(list1)):
 if(len(list1))%2==0:   
     result1 = list1[0]*list1[-1]
     result = (list1[0]+1)*(list1[-1]-1)
     list= [result1, result]

 elif(len(list1))%2!=0:
     result1 = list1[0]*list1[-1]
     result = (list1[0]+1)*(list1[-1]-1)
     i=len(list1)//2
     result2 =list1[i]**2
     list = [result1, result2, result]
   
print(list1)  
print(list)



