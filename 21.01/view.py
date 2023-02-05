# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Создать контакт
# 5. Удалить контакт
# 6. Изменить контакт
# 7. Найти контакт
# 8. Выход из программы

commands = ['Открыть файл',
             'Сохранить файл',
             'Показать все контакты',
              'Создать контакт',
              'Удалить контакт',
              'Изменить контакт',
              'Найти контакт',
              'Выход из программы']

def main_menu():
    print('Главное меню: ')
    for i, item in enumerate(commands, 1):
        print(f'\t{i}. {item}')
    while True:
        try:
            choice = int(input('Выберите пункт меню: '))
            if 0<choice<9:
                return choice
            else:
                print('Введите значение от 1 до 8')
        except ValueError:
         print('Введите правильное значение ')


def show_contacts(phone_list: list):
    if len(phone_list)<1:
        print('Телефоная книга пуста или не открыта')
    else:
        for i, contact in enumerate(phone_list, 1):
            print(f'\t{i}. {contact[0]:30} {contact[1]:13} {contact[2]:20}')
        print()

def input_error():
    print('Ошибка ввода, введите корректный пункт меню ')

def empty_request():
    print('Контакт не найден')
def many_request():
    print(' Введите точнее данные')


def create_new_contact():
    name = input('Введите имя и фамилию: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment

def del_contact():
    name = input('Введите имя и фамилию: ')
    return name

def delete_confirm(contact: str):
  name_del = ('Вы уверены, что хотите удалить контакт %s(yes,no)?: '% contact).lower()
  if name_del == 'yes':
    print('Данный контакт успешно удален')
    return True
  else:
    return False

def find_contact():
    find = input( 'Введите искомый элемент: ')
    return find

def select_contact(message: str):
    contact = input(message)
    return contact

    
def change_contact():
    print('ВВедите новые (если изменения не требуются нажмите Enter ')
    name = input('Введите имя и фамилию: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment