from functools import wraps 

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            if isinstance(e, KeyError):
                return "Contact not found. Give correct name, Please." 
            elif isinstance(e, ValueError): 
                return "Give me name and phone, Please."
            elif isinstance(e, IndexError):
                return "Contact not found."
    return inner 

phonebook = {}

# Розбиває вхідні данні на команду та аргументи
def parse_input(user_input):
    return user_input.lower().split() 

# Додаємо контакт до словника
@input_error 
def add_contact(name, phone):
    if name and phone:
        phonebook[name] = phone 
        return "Contact added."
    else:
        raise ValueError 
    
# Зміна збереженного контакту 
@input_error
def change_contact(name, phone):
    if name in phonebook:
        phonebook[name] = phone
        return "Contact update."
    else:
        raise KeyError 
    
# Знаходимо номер тел за ім‘ям
@input_error 
def show_phone(name):
    phone = phonebook.get(name)
    if phone:
        return phone 
    else:
        raise IndexError 

# Виводимо у консоль усі записи, якщо існують 
def show_all():
    if not phonebook:
        return "Phonebook is empty."
    else:
        return '\n'.join(f'{name}: {phone}' for name, phone in phonebook.items())

# Головна функція (управляє основним циклом обробки команд)
def main():
    print('Welcome to the assitent bot!')
    
    while True:
        user_input = input('Enter command: ')
        command, *args = parse_input(user_input)
        
        if command == 'hello':
            print('How can I help you?')
            
        elif command == 'add':
            if len(args) == 2:
                name, phone = args 
                print(add_contact(name, phone))
            else:
                print('Give me name and phone please.')
                
        elif command == 'change':
            if len(args) == 2:
                name, phone = args
                print(change_contact(name, phone)) 
            else:
                print('Give me name and phone, Please.')
            
        elif command == 'phone':
            if len(args) == 1:
                name = args[0]
                print(show_phone(name))
            else:
                print('Give me name, Please.')
                
        elif command == 'all' and not args:
            print(show_all())
            
        elif command in ['close', 'exit']:
            print('Good bye!')
            break
        
        else:
            print('Invalid command. Please try again.')
            
if __name__ == '__main__':
    main()        