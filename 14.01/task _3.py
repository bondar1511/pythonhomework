
# Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем. На вход будет подаваться дата в формате "день.месяц.год". 
# Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нет.

# Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна) в зависимости от результата проверки.


from sys import argv


def is_valid_date(date):
# Проверка на корректность формата даты
    if date.count('.') != 2:
     return False

# Разбиение строки даты на массив подстрок
    date_elements = date.split('.')

# Проверки на диапазон значений каждой из подстрок (дня, месяца, года)
    day = int(date_elements[0])
    month = int(date_elements[1])
    year = int(date_elements[2])     

    if year < 100:
         if (year < 70 and month == 2) or (year >= 70 and month <= 4 and year % 4 == 0):
                 print(False)
    else:
         year_last_two_digits = year % 100
         if month == 2 and (year_last_two_digits < 70 or year_last_two_digits > 99):
                 print(False)
         
         
date = input('Введите дату в формате "день.месяц.год": ') 



def _is_leap(year :int) -> bool:
    return not(year % 4 != 0 or year % 100 == 0 and year % 400 != 0)

def valid(full_date: str) -> bool:
    date, month, year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or month > 12 or date < 1 or date > 31:
        return False
    if month in (4, 6, 9, 11) and date > 30:
        return False
    if month == 2 and _is_leap(year) and date > 29:
        return False
    if month == 2 and not _is_leap(year) and date > 28:
        return False
    return True


if __name__ == "__main__":
    if len(argv) != 2:
        print("использование: python date_validator.py <дата в формате DD.MM.YYYY")
    else:
     input_date = argv[1]
     if valid(input_date):
         print("дата существует")
     else:
          print("дата невозможна")





# def is_valid_date(date):
#     if date.count('.') != 2:
#         return False

#     date_elements = date.split('.')
#     day = int(date_elements[0])
#     month = int(date_elements[1])
#     year = int(date_elements[2])

#     if year < 100:
#         if (year < 70 and month == 2) or (year >= 70 and month <= 4 and year % 4 == 0):
#             return False
#     else:
#         year_last_two_digits = year % 100
#         if month == 2 and (year_last_two_digits < 70 or year_last_two_digits > 99):
#             return False

#     return (day > 0 and day < 32) and (month > 0 and month < 13)

# while True:
#     date_to_prove = input()
#     if user_input == "":
#          break

# is_valid_result = is_valid_date(user_input)
# print(f"{date_to_prove} = {is_valid_result}")