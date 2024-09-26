groceries_list = []
choice : 0 # oh noo this should be a variable assignment not a colon :(

while choice != 4:
    print('[1] Add an item')
    print('[2] View the list')
    print('[3] Remove an item')
    print('[4] Quit')
    
    choice = int(input('Choice: '))

    match choice:
        case 1:
            add_fruits = input("Add an item: ")  
            groceries_list.append(add_fruits)  
            print(f'{add_fruits} added to the list.')

        case 2:
            if groceries_list:
                print('Your current grocery list:')
                for item in groceries_list:
                    print(f'- {item}')
            else:
                print('Your grocery list is empty.')

        case 3:
            remove_item = input("Enter the item to remove: ") 
            if remove_item in groceries_list:
                groceries_list.remove(remove_item)  
                print(f'{remove_item} removed from the list.')
            else:
                print(f'{remove_item} is not in the list.')

        case 4:
            print('Exiting...')
            

        case _:
            print('Not a valid input.')

print('Bye')

"""
the code is very close to perfect!! it just needs some error handling just incase the user inputs a string when they should
actually input a number. overall very neat and good!!
"""
