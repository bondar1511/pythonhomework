import view
import model

def start():
    choice = ''
    while choice !=8:
      choice = view.main_menu()
              
      match choice:
        case 1:
            model.open_file()
            view.information('\n Файл успешно открыт\n')
        case 2:
           model.save_file()
           view.information('\n Файл успешно сохранен\n')
        case 3:
           view.show_contacts(model.get_phonebook())
        case 4:
           new_contact = list(view.create_new_contact())
           model.add_new_contact(new_contact)
           view.information('\n Контакн {new_contact[0]} успешно создан\n')
        case 5:  
          del_name = view.del_contact()
          contact = model.get_contact(del_name)
          if contact:
            confirm = view.delete_confirm(contact[0][0])
            if confirm:
               model.delete_contact(contact[0])
               view.information(f'\n Контакт{contact[0][0]} успешно удален\n')
          elif contact == []:
            view.empty_request()
          else:
            view.many_request()
        case 6:
            name = view.select_contact('Введите изменяемы контакт: ')
            contact = model.get_contact(name)
            if contact:
              change_contact = view.change_contact
              model.change_contact(contact[1], list(change_contact))
              view.information(f'\n Контакт{contact[0][0]} успешно изменен\n')
            elif contact == []:
             view.empty_request()
            else:
              view.many_request()
        case 7:  
           find = view.find_contact()
           result = model.searh_contact(find)
           view.show_contacts(result)

        case _:
         view.input_error()
