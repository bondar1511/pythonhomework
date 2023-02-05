import model

def welcom():
    print('Добро пожаловать в наш калькулятор!!')

def data_entry():
     list = (input('Введите пример: ')).split(' ')
     return list

def end():
    choice = input('\n Вы хотите дальше продолжить (yes,no)?\n')
    if choice == 'yes':
      return choice
    elif choice == 'no':
       print('До скорой встречи!!!')
    else:
     return choice

def error(): 
 i=0 
 if  list[i]=='/':
     while True:
        try:
           int(list[i+1]) == 0 
        except ZeroDivisionError:
         print('Делить на ноль нельзя!!!!')
         return list[i]
 
 if list[i]!=int:
  while True:
          try:
            num = list[i]
            return num
          except ValueError:
             print('Введите натуральное число')
            
        
def result():
   global list
   list = print("Результат: ")





