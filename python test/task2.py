# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

num = int(input("Введите число от 1 до 100000: \n"))
count = 0
if num>=1 and num<=10000:
 for i in range(2, num - 1):
    if (num% i == 0):
            count += 1
 if (count <= 0):
        print("Число является простым")
 else:
        print("Число является составным")
else:
    print("Введённое число не входит в заданный диапазон")