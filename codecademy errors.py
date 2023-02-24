
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



