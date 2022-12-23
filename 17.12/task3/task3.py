# 3.	Реализуйте алгоритм перемешивания списка. ,
#  максимум использование библиотеки Random для получения случайного int
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 


num  =int(input('ВВедите число: '))
list = []

for i in range(1, num+1):

   list.append(i)
print(list)
p= -1
for i in list:
   if i<(len(list)):
    list[i] = list[p]-1
    p-=1
print(list)