
# # Online Python - IDE, Editor, Compiler, Interpreter
# class Calc:
#     def __init__(self,x1,x2,x3,y1,y2,y3):
#         self.x1 = x1
#         self.x2 = x2
#         self.x3 = x3
#         self.y1 = y1
#         self.y2 = y2
#         self.y3 = y3
#     def cal_medidas_do_triangulo(self):
#         dist_a =(((self.x2-self.x1)**2) +((self.y3-self.y1)**2)**5)/2
#         dist_b =(((self.x3-self.x2)**2) +((self.y3-self.y2)**2)**5)/2
#         dist_c =(((self.x3-self.x1)**2) +((self.y2-self.y1)**2)**5)/2
#         p = dist_a + dist_b + dist_c
#         area = (p*(p- dist_a) * (p - dist_b) * (p - dist_c))**5
#         print('As medidas do triângulo são, ' ,self.x1,',',self.x2,',',self.x3,',',self.y1,
#         ',',self.y2, 'e',self.y3, '.',  '\n'' A área é', area,'\n','O perimetro do triângulo é',p)
        

# a1 = Calc(1,4,2,1,4,2)
# a1.cal_medidas_do_triangulo()

class Box:
    def __init__(self, weight):
        self.__weight = weight
    @property
    def weight(self):
        print (self.weight)
 
    @weight.setter
    def weight(self,weight):
        if weight >= 0:
            self.__weight = weight
            print(weight)
        else:
            print('lol')
            
    @weight.deleter
    def weight(self):
        del self.__weight
    

box = Box(100) 
box.weight = - 10
 
print('ass')

instrument_catalog = {
  'Marimba': 1999,
  'Kora': 499,
  'Flute': 899
}

def print_instrument_price(instrument):

  # Write your code below:
 if instrument in instrument_catalog:
      print('The price of a ' + instrument + ' is ' + str(instrument_catalog[instrument]))
    # Checkpoint 3
 else:
      raise KeyError( 'The item' + instrument + ' is not found in instrument catalog!')

print_instrument_price('Marimba')
print_instrument_price('Flute')
print_instrument_price('Piano')




#codecademy 25/02/2022
# Try / except

staff = {
  'Austin': {
    'floor managers': 1,
    'sales associates': 5
  },
  'Melbourne': {
    'floor managers': 0,
    'sales associates': 8
  },
  'Beijing': {
    'floor managers': 2,
    'sales associates': 5
  },
}

def print_staff_report(location, staff_dict):
  managers = staff_dict['floor managers']
  sales_people = staff_dict['sales associates']
  ratio = sales_people / managers
  print('Instrument World ' + location + ' has:')
  print(str(sales_people) + ' sales employees')
  print(str(managers) + ' floor managers')
  print('The ratio of sales people to managers is ' + str(ratio))
  print()

for location, staff in staff.items():
  try:
      print_staff_report(location, staff)
  # Write your code below:
  
  except ZeroDivisionError as e:
      print('Could not print sales report for ' + location)
      print(e)


# lesson 6/11


instrument_prices = {
  'Banjo': 200,
  'Cello': 1000,
  'Flute': 100,
}

def display_discounted_price(instrument, discount):
  full_price = instrument_prices[instrument]
  discount_percentage = discount / 100
  discounted_price = full_price - (full_price * discount_percentage)
  print("The instrument's discounted price is: " + str(discounted_price))

instrument = 'Banjo'
discount = '20'

# Write your code below:
try:
  display_discounted_price(instrument, discount)
except KeyError:
  print('An invalid instrument was entered!')
except TypeError:
  print('Discount percentage must be a number!')
except Exception:
  print('Hit an exception other than KeyError or TypeError!') 

# semi- fix


instrument_prices = {
  'Banjo': 200,
  'Cello': 1000,
  'Flute': 100,
}

def display_discounted_price(instrument, discount):
  full_price = instrument_prices[instrument]
  discount_percentage = discount / 100
  discounted_price = full_price - (full_price * discount_percentage)
  print("The instrument's discounted price is: " + str(discounted_price))

instrument = 'Clarinet'
discount = 20

# Write your code below:
try:
    display_discounted_price(instrument, discount)
except:
    for instrument, value in instrument_prices.items():
        display_discounted_price(instrument, discount)


