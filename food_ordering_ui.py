#user interface to the main menu
import data
import functions

order_list=[]

def show_main_menu():
  while True:
    print("Gangadhar's diner") #edit to show your name
    print("-----------------")
    print('N for a new order')
    print('C for change order')
    print('X for close orders and print the check')
    print('Q for quit')
    user_menu_choice = input('Your choice: ')
    if user_menu_choice in 'Qq':
      break
    elif user_menu_choice in 'Xx':
      print('This option prints the list of items ordered, extended price, total, Taxes, and Grand total ')
      close_order(user_menu_choice)
    elif user_menu_choice in 'Nn':
      print('New order')
      make_order(user_menu_choice.upper())  #calls a function for adding to the orders
    elif user_menu_choice in 'cC':
      change_order()


def change_order():
    print('Here is your order:')
    print('--------------------')
    print(order_list)
    add_remove()

def add_remove():
  global order_list
  print('What operation required?')
  print('R for Remove Item')
  print('A for Add Item')
  change=input('Enter your choice:')
  if change in 'Rr':
      item=input('Enter dish number to remove: ')
      order_list=[O for O in order_list if O[0]!=item]
      print(f'{item} is removed',order_list)
  else:
     add()
     if contin in 'yY':
            make_order(contin)
     else:
        breakpoint
    
        

def make_order(menu_choice):
    
    while True:
        print('Functionality for menu choice', menu_choice)
        user_selection = functions.get_item_number()
        item_code, quantity = user_selection.split()
        item_name, item_price =functions.get_item_information(item_code)
    
        if item_name: 
          order_list.append((item_code,item_name,item_price,int(quantity)))
          print(item_name, quantity)
        add()
        if contin!='y' and contin!='Y':
            break
         

def add():
   global contin 
   while True:
          contin= input('Do you want add any other items? (Y/N):')
          if contin not in 'yY' and contin not in 'nN':
            print('Please enter valid input.')
          else: break



def close_order(menu_choice):
    print('Functionality for menu choice ', menu_choice)

    if not order_list:
      print('No items')
      return

    total=0
    print('Order Details:')
    print('--------------')
    for item_code, item_name, quantity, item_price in order_list:
       item_total= quantity*item_price
       total= total + item_total
       print(f'{quantity}x{item_name}- ${item_price}={item_total}')

    tax= total *0.07
    grand_total= total+tax
    print('--------------------')
    print(f'Subtotal: ${total:.2f}')
    print(f'Tax (7%): ${tax:.2f}')
    print(f'Grand Total: ${grand_total:.2f}')
    print('-------------------\n')
    # Reset order list
    order_list.clear()




if __name__ == '__main__':
    #initialize the lists
    drinks = []
    appetizers = []
    salads = []
    entrees = []
    dessert= []
    #print(functions.get_item_information('D1'))
    show_main_menu()


