#this module will be where most functionality will be stored
#create your def blocks for the assignment in this module
#Use this  function that will return the item name and price for a given item code
# for example, find_menu_item('D2') should return Lemonade, and integer 3 as the result
import data
def get_item_information(item_code):
  """ this  function that will return the item name and price for a given item code.
    For example, find_menu_item('D2') should return Lemonade, and integer 3 as the result """
  print(item_code)
  for item in data.menu_items:
    item_number, item_name, item_price = item.split(' ')
    if item_number == item_code:
      return item_name.encode("ascii", "ignore").decode(), int(item_price)

def display_items():
  pass

def get_item_number():
  while True:
    print('------------------------------------------')
    print('Drinks', [d.replace('\u200b','') for d in data.menu_items if d[0] == 'D'])
    print('Appetizers', [d.replace('\u200b','') for d in data.menu_items if d[0] == 'A'])
    #write code for displaying the other dishes also
    print('Salads', [d.replace('\u200b','') for d in data.menu_items if d[0]=='S'])
    print('Entrees', [d.replace('\u200b','') for d in data.menu_items if d[0]=='E'])
    print('Desserts', [d.replace('\u200b','') for d in data.menu_items if d[0]=='T'])
    print('------------------------------------------')

    order_item = input('Enter dish number and quantity: ')
    order_item=order_item.upper()
    
    if len(order_item)==2:
      print('---------------------------------------')
      print('Invalid dish number.  Please try again')
      print('---------------------------------------')
    elif order_item.split()[0] in data.all_items:
      return order_item
    else:
      print('---------------------------------------')
      print('Invalid dish number.  Please try again')
      print('---------------------------------------')

