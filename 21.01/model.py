





phonebook = []
path = r'C:\Users\Anna\Documents\python homework\21.01\data.txt'
def get_phonebook():
    global phonebook
    return phonebook

def get_contact(text: str):
    global phonebook
    result = []
   
    for i, contact in enumerate(phonebook):
        for field in contact:
            if text in field:
                result.append((contact, i))
                break
            if len(result)>1:
                return False
            elif result==[]:
                return result
            else:
                return result[0]
                 

def open_file():
    global phonebook
    global path
    with open(path, 'r', encoding='UTF-8') as data:
        file =  data.readlines()
    
    for contact  in file:
       phonebook.append(contact.strip().split(';'))

def save_file():
        global phonebook
        global path
        pb_str = []
        for contact  in phonebook:
          pb_str.append(';'.join(contact))
        with open(path, 'w', encoding='UTF-8') as data:
          data.write('\n'.join(pb_str))



def add_new_contact(new_contact: list):
    global phonebook
    phonebook.append(new_contact)
def searh_contact(find: str):
    global phonebook
    result =[]
    for contact in phonebook:
        for field in contact:
            if find in field:
                result.append(contact)
                break
    return result

def delete_contact(contact: list):
    global phonebook
    phonebook.remove(contact)


def change_contact(index: int, new: list):
    global phonebook
    phonebook[index][0] = new[0] if new[0] != ' ' else phonebook[index][0]
    phonebook[index][1] = new[1] if new[0] != ' ' else phonebook[index][1]
    phonebook[index][2] = new[2] if new[0] != ' ' else phonebook[index][2]











