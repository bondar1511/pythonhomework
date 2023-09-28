# . Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)
from random import randint

num = randint(0, 1000)
res = int(input())
for i in range(10):
 if res !=num:
  if res > num:
    print(" Загаданое число меньше данного числа")
    res = int(input())
  if res < num:
    print(" Загаданое число больше данного числа")
    res = int(input())
 if res == num:
    print("Поздравлю!!! Вы угадали число")
    break
 else:
    print("Превышено число попыток")