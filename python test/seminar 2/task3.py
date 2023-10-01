# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.



from fractions import Fraction


str_1 = (input (" Введите дробь вида a/b: ")).split('/')
str_2 = (input (" Введите дробь вида a/b: ")).split('/')
for i , item in enumerate(str_1):
    str_1[i] = int(item)
   
 
for i , item in enumerate(str_2):
 str_2[i] = int(item)

def fraction_sum(str_1, str_2):
  sum =  str_1[0]+str_2[0]
  sum_1 =  str_1[1]+str_2[1]
  sum_res = f"{sum}/{sum_1}"
  return sum_res
result_1 = fraction_sum(str_1,str_2)
print ("Сумма дробей: ", result_1)

def fraction_multi(str_1, str_2):
   multi =  str_1[0]*str_2[0]
   multi_1 =  str_1[1]*str_2[1]
   multi_res = f"{multi}/{multi_1}"
   return multi_res
result_2 = fraction_multi(str_1,str_2)
print ("Произведений дробей: ", result_2)

def add_and_multiply_fractions(str_1, str_2):
   str_1 = Fraction(str_1)
   str_2 = Fraction(str_2)
   sum_fraction = str_1 + str_2
   multipiy_fraction = str_1*str_2
   sum_fraction_str = f"{sum_fraction.numerator}/{sum_fraction.denominator}"
   multipiy_fraction_str = f"{multipiy_fraction.numerator}/{multipiy_fraction.denominator}"
   return sum_fraction_str, multipiy_fraction_str

sum_fraction, multipiy_fraction  = add_and_multiply_fractions(str_1, str_2)
print ("Сумма дробей: ", sum_fraction)
print ("Произведений дробей: ", multipiy_fraction)