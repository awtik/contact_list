#    ___ _       ______________ ___                           __             __     ___      __ 
#   /   | |     / /_  __/  _/ //_( )_____   _________  ____  / /_____ ______/ /_   / (_)____/ /_
#  / /| | | /| / / / /  / // ,<  |// ___/  / ___/ __ \/ __ \/ __/ __ `/ ___/ __/  / / / ___/ __/
# / ___ | |/ |/ / / / _/ // /| |  (__  )  / /__/ /_/ / / / / /_/ /_/ / /__/ /_   / / (__  ) /_  
#/_/  |_|__/|__/ /_/ /___/_/ |_| /____/   \___/\____/_/ /_/\__/\__,_/\___/\__/  /_/_/____/\__/  
                                                                                               
import os
from sql import Database
os.system('cls') # Clear console

db = Database() # Initialization db class
db.create() # Create db

def contact_add():
    """function to create contact"""
    name = input('Insert contact name: \n: ') # Get contact info
    number = input('Insert contact number: \n: ') # Get contact info
    os.system('cls') # Clear console
    try:
        db.insert(name, number)
        os.system('cls') # Clear console
        print('Succesful added!')
    except SyntaxError:
        print('Error!')

def contact_list():
    output = '          Contact list' # Title of list
    num = 1 # Num of contact
    for contact in db.get_contacts():
        output += f'\n{num}) Name: {contact[1]} | Number: +{contact[2]}' # 1) Name: test | Number: +test
        num += 1
    print(output + '\n')

def commands():
    print('''           Command List
        add - Create new contact
        list - Show Contact List
        del - Delete contact
        edit - Edit the contact
        exit - Close program\n''')

def remove():
    name = input('Insert contact name for delete: \n: ')
    try:
        db.remove_contact(name) # Remove db item
        os.system('cls') # Clear console
        print('Succesful deleted!')
    except:
        os.system('cls') # Clear console
        print('Error!')

def edit():
    choose = input('''          Choose one:
    name    |   number  |   back\n: ''') # Choose method
    os.system('cls') # Clear console
    if choose == 'name':
        os.system('cls') # Clear console
        name = input('Insert contact name for edit: \n: ') # Get name of contact
        os.system('cls') # Clear console
        newName = input('Insert new contact name: \n: ') # Get new name of contact
        try:
            db.edit_contact_name(name, newName) # Edit name in Database
            os.system('cls') # Clear console
            print('Succesful edited!\n')
        except:
            os.system('cls') # Clear console
            print('Error!\n')
    elif choose == 'number':
        os.system('cls') # Clear console
        name = input('Insert contact name for edit: \n: ') # Get name of contact
        os.system('cls') # Clear console
        newNumber = input('Insert new contact number: \n: ') # Get new number of contact
        try:
            db.edit_contact_number(newNumber, name) # Edit number in Database
            os.system('cls') # Clear console
            print('Succesful edited!\n')
        except:
            os.system('cls') # Clear console
            print('Error!\n')
    elif choose == 'back': # Exit from editor
        pass

commands()
while(1):
    command = input('Insert command: \n: ') # Get command
    os.system('cls') # Clear console
    if command == 'add':
        contact_add()
    elif command == 'list':
        contact_list()
    elif command == 'del':
        remove()
    elif command == 'commands':
        commands()
    elif command == 'edit':
        edit()
    elif command == 'exit':
        exit()
    else:
        print('Unknown command!')