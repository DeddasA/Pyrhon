# Python coonteiners

# Write your code below!
company_name = "Killer look"
company_location = (15,25)
company_products = ['Banana','Sugar',"Leather sofa", 'Coffer', 'Sugarless sugar']
company_data = {'name': company_name,'location': company_location, 'products': company_products}
print(company_data)

from collections import OrderedDict
 
orders = OrderedDict({'order_4829': {'type': 't-shirt', 'size': 'large', 'price': 9.99},
          'order_6184': {'type': 'pants', 'size': 'medium', 'price': 14.99},
          'order_2905': {'type': 'shoes', 'size': 12, 'price': 22.50}})
 
orders.move_to_end('order_4829')
orders.popitem()
print(orders)

# from helper_functions import process_csv_supplies
from collections import deque

# The first row is skipped since it only contains labels
# csv_data = process_csv_supplies()[1:]

# Here is a sample of 2 elements in csv_data:
# [ ['nylon', '10', 'unimportant'], ['wool', '1', 'important'] ]

# Write your code below!
# supplies_deque = deque()
# for item in csv_data:
#   if 'important' in item:
#     supplies_deque.appendleft(item)
#   else:
#     supplies_deque.append(item)

# ordered_important_supplies = deque()
# count = 0
# for i in range(25):
#     ordered_important_supplies.append(supplies_deque.popleft())
# ordered_unimportant_supplies = deque()
# for i in range(10):
#     ordered_unimportant_supplies.append(supplies_deque.pop())

# print(ordered_important_supplies)
# print(ordered_unimportant_supplies)
from collections import namedtuple  
clothes = [('t-shirt', 'green', 'large', 9.99),
           ('jeans', 'blue', 'medium', 14.99),
           ('jacket', 'black', 'x-large', 19.99),
           ('t-shirt', 'grey', 'small', 8.99),
           ('shoes', 'white', '12', 24.99),
           ('t-shirt', 'grey', 'small', 8.99)]

ClothingItem = namedtuple('ClothingItem',['type', 'color', 'size','price'])
new_coat = ClothingItem('coat', 'black', 'small',14.99)
coat_cost = new_coat.price

updated_clothes_data = []
for item in clothes:
#   updated_clothes_data.append(ClothingItem(item[0], item[1], item[2], item[3]))
  #This saves a lot of time using the * unpack function
  updated_clothes_data.append(ClothingItem(*item))
print(updated_clothes_data)


print('  ')

site_locations = {'t-shirt': 'Shirts',
                  'dress shirt': 'Shirts',
                  'flannel shirt': 'Shirts',
                  'sweatshirt': 'Shirts',
                  'jeans': 'Pants',
                  'dress pants': 'Pants',
                  'cropped pants': 'Pants',
                  'leggings': 'Pants'
                  }
updated_products = ['draped blouse', 'leggings', 
'undershirt', 'dress shirt', 'jeans', 'sun dress', 
'flannel shirt', 'cropped pants', 'dress pants', 
't-shirt', 'camisole top', 'sweatshirt']



site_locations = {'t-shirt': 'Shirts',
                  'dress shirt': 'Shirts',
                  'flannel shirt': 'Shirts',
                  'sweatshirt': 'Shirts',
                  'jeans': 'Pants',
                  'dress pants': 'Pants',
                  'cropped pants': 'Pants',
                  'leggings': 'Pants'
                  }
updated_products = ['draped blouse', 'leggings', 'undershirt', 'dress shirt', 'jeans', 'sun dress', 'flannel shirt', 'cropped pants', 'dress pants', 't-shirt', 'camisole top', 'sweatshirt']

# Write your code below!
from collections import defaultdict
# validated_locations = defaultdict(lambda:'TODO: Add to website')
validated_locations = defaultdict.update('TODO: Add to website')
from collections import defaultdict

site_locations = {'t-shirt': 'Shirts',
                  'dress shirt': 'Shirts',
                  'flannel shirt': 'Shirts',
                  'sweatshirt': 'Shirts',
                  'jeans': 'Pants',
                  'dress pants': 'Pants',
                  'cropped pants': 'Pants',
                  'leggings': 'Pants'
                  }

updated_products = ['draped blouse', 'leggings', 'undershirt', 'dress shirt', 'jeans', 'sun dress', 'flannel shirt', 'cropped pants', 'dress pants', 't-shirt', 'camisole top', 'sweatshirt']

validated_locations = defaultdict(lambda: 'TODO: Add to website')
validated_locations.update(site_locations)

for item in updated_products:
  site_locations[item] = validated_locations[item]
print(site_locations)




   


