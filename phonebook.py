def print_phonebook(phonebook_d):
   print('Name\tphone')
   for name, phone in phonebook_d.items():
       print(name, '\t', phone)


phonebook = {}
list_of_help = ['help            - Show this help','quit            - Quit the program','add             - Create a new contact'
                ,'list            - Show list of all contacts','delete          - Delete single contact','edit            - Edit exiting contact']



while True:
   command_input = input("Enter a command (h for help):")
   if command_input == 'h':
       for ele in list_of_help:
        print(ele)
   elif command_input == 'quit':
       break
   elif command_input == 'add':
       name = input("Enter name:")
       phone = input("Enter phone:")
       if name in phonebook:
           print("You already have this contact")
       else:
           phonebook[name] = phone
   elif command_input == 'list':
       print_phonebook(phonebook)
   elif command_input == 'delete':
       print(phonebook)
       name = input("Enter name you want to delete:")
       phonebook.pop(name)
   elif command_input == 'edit':
       name = input("Enter name you want to edit:")
       phone = input("Enter new number:")
       phonebook[name] = phone







