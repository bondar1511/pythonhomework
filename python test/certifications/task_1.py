# Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров. 
import logging
import sys


list_name = []
list_salaries = []
list_bonuses = []

for i in range(3):
 try:
    names = input()
    salary  = int(input())
    bonus = input()

    list_name.append(names)
    list_salaries.append(salary)
    list_bonuses.append(bonus)
 except ValueError as e:
    logging.error("Произошла ошибка при приеме входных данных: {}".format(e))
logging.basicConfig(level=logging.INFO,
format='%(asctime)s [%(levelname)s] %(message)s',
handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()])   

def generate_bonus_dict(nameses, salaries, bonuses):
 try:
    return{name: salary * float(bonus.rstrip("%"))/100
           for name, salary, bonus in zip(nameses, salaries, bonuses)}
 except ValueError as e:
  logging.error("Произошла ошибка при создании бонусного словаря: {}".format(e))
  return {}



resuilt_dict = generate_bonus_dict(list_name, list_salaries,  list_bonuses)
print(resuilt_dict)
logging.info("Результирующий словарь: {}".format(resuilt_dict))
logging.shutdown()



if __name__ == "__main__":
  
    if len(sys.argv) == 3:
       nameses = sys.argv[1] 
       salaries = sys.argv[2] 
       bonuses = sys.argv[3] 
       generate_bonus_dict(nameses, salaries, bonuses) 
    else:
        print("Ошибка! Необходимо передать три параметра при запуске из командной строки.")
