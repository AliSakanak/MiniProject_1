import pickle
try:
    products = pickle.load(open('products.dat', 'rb'))
    print('Loading')
except FileNotFoundError:
    print('Existing File not found. Creating new file.')
    products = []

def mmenu():
    print('\n___Main Menu___')
    print('[0] Exit App')
    print('[1] Product Menu Options\n')
def product_menu():
    print('\n___Product Menu Options___')
    print('[0] Return to Main Menu')
    print('[1] View Products List')
    print('[2] Add New Product')
    print('[3] Update Existing Product')
    print('[4] Delete Product\n')
def save_menu():
    print('\n[1] Yes')
    print('[0] No')
def index_list():
    for i, product in enumerate(products):
        print(i, product)

while True:
    try:    
        mmenu()
        option = int(input('Pick your option: '))
    except ValueError:
        print('Please enter a correct number option')
        continue
    if option == 0:
        print('Exiting App')
        break
    elif option != 1:
        print('Invalid option. Please choose a correct number.')
        continue
    while option != 0:
        product_menu()
        try:
            option = int(input('Pick your option: '))
        except ValueError:
            print('Enter a valid number option')
        if option == 0:
            continue
        elif option == 1:
            print(products)
        elif option == 2:
            product_name = input('Type the product you want to add: ')
            products.append(product_name.title())
        elif option == 3:
            index_list()
            try:
                user_choice = int(input('Type number of item you wish to update: '))
                old_product = products[user_choice]
                new_product = input('Type name of new product name: ').title()
                products[user_choice] = new_product
                print(f'{old_product} changed to {new_product}.')
            except IndexError:
                print('No such number item exists.')
            except ValueError:
                print('Please enter the number of the item, not the word.')
        elif option == 4:
            index_list()
            try:
                deleted_item = int(input('Type number of item you wish to delete: '))
                print(f'Deleted {products[deleted_item]} from products list.')
                del products[deleted_item]
            except IndexError:
                print('No such number item exists.')
            except ValueError:
                print('Please enter the number of the item, not the word.')
        else:
            print('Enter a valid option')
            

save_menu()
save_option = int(input('Would you like to save changes? '))
if save_option == 1:
    print('Saving changes...')
    pickle.dump(products, open('products.dat', 'wb'))
    print('Save successful. Quitting.')
    quit()
elif save_option == 0:
    print('Quitting without saving changes!')
    quit()    