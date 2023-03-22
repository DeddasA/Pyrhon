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


# from collections import OrderedDict


# order_data = [['Order: 1', 'purchased'],
#               ['Order: 2', 'purchased'],
#               ['Order: 3', 'purchased'],
#               ['Order: 4', 'returned'],
#               ['Order: 5', 'purchased'],
#               ['Order: 6', 'canceled'],
#               ['Order: 7', 'returned'],
#               ['Order: 8', 'purchased'],
#               ['Order: 9', 'returned'],
#               ['Order: 10', 'canceled'],
#               ['Order: 11', 'purchased'],
#               ['Order: 12', 'returned'],
#               ['Order: 13', 'purchased'],
#               ['Order: 14', 'canceled'],
#               ['Order: 15', 'purchased']]

# # Write your code below!
# orders = OrderedDict(order_data)
# to_move =[]
# to_remove = []
# for lst in order_data:
#     for value in lst:
#         if value == 'returned':
#             to_move.append(lst[0])
#         if value == 'canceled':
#             to_remove.append(lst[0])
# print(to_move)
# print(to_remove)
# for item in to_remove:
#     for item_1 in to_move:
#         if item in orders:
#             orders.pop(item)
#         if item_1 in orders:
#             orders.move_to_end(item_1)
# print(orders)
print('   ')



year_profit_data = [
    {'jan_profit': 15492.30, 'jan_holiday_profit': 2589.12},
    {'feb_profit': 17018.05, 'feb_holiday_profit': 3701.88},
    {'mar_profit': 11849.13},
    {'apr_profit': 9870.68},
    {'may_profit': 13662.34},
    {'jun_profit': 12903.54},
    {'jul_profit': 16965.08, 'jul_holiday_profit': 4360.21},
    {'aug_profit': 17685.69},
    {'sep_profit': 9815.57},
    {'oct_profit': 10318.28},
    {'nov_profit': 23295.43, 'nov_holiday_profit': 9896.55},
    {'dec_profit': 21920.19, 'dec_holiday_profit': 8060.79}
]

new_months_data = [
    {'jan_profit': 13977.85, 'jan_holiday_profit': 2176.43},
    {'feb_profit': 16692.15, 'feb_holiday_profit': 3239.74},
    {'mar_profit': 17524.35, 'mar_holiday_profit': 4301.92}
]

# Write your code below!

from collections import ChainMap

profit_map = ChainMap(*year_profit_data)
update = profit_map.new_child(new_months_data)

last_year_standart_profits= 0.0
last_year_holiday_profits = 0.0
def get_profits(data):
    global last_year_standart_profits,last_year_holiday_profits
    for key, value in data.items():
        if 'holiday' not in key:
            last_year_standart_profits += value
          
        else:
            last_year_holiday_profits += value
           
            
    print(f'The standart month profit is {last_year_standart_profits:.2f}.')
    print(f'The holiday month profit is {last_year_holiday_profits}.')
    
get_profits(profit_map)
current_year_standart =0 
current_year_holiday = 0
def get_profits_2(data):
    global current_year_standart,current_year_holiday
    for key, value in data.items():
        if 'holiday' not in key:
            current_year_standart+= value
          
        else:
            current_year_holiday += value
           
            
    print(f'The current standart month profit is {current_year_standart:.2f}.')
    print(f'The current holiday month profit is {current_year_holiday}.')
             
        


for item in new_months_data:
    profit_map_updated = profit_map.new_child(item)
    
get_profits_2(profit_map_updated)
        
def difference():
    diff_standart = current_year_standart - last_year_standart_profits
    diff_holiday = current_year_holiday - last_year_holiday_profits
    print(f'{diff_standart:.2f}')
    print(f'{diff_holiday:.2f}')
difference()
    
    
    


  

   


