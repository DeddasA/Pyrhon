temps = [[20, 19.5], [20, 19.7],
[20, 20.2], [20, 20.1], [21, 19.9], 
[21, 20.7], [21, 21.2], [21, 21.5],
[25, 25.5], [25, 24.7], [25, 25.2], [25, 24.1]] 


class temp_checker:
    def __init__(self,list_temp):
        self.list_temp = list_temp
    def media(self):
        medias = {}
        count = 0
        for list_01 in self.list_temp:
            count += 1
            med = sum(list_01) / len(list_01)
            medias[f'media {count}'] = med
        print(medias)
            
 
t1 = temp_checker(temps)
t1.media()
print('   ')
class temp_checker:
    def __init__(self,list_temp):
        self.list_temp = list_temp
    def media(self):
        medias = []
        count = 0
        for list_01 in self.list_temp:
            count+=1
            med = sum(list_01) / len(list_01)
            for n in list_01:
                dvp_sum = sum((n - med) ** 2 for n in list_01) 
                dvp_final = (dvp_sum / len(list_01)) **0.5
            
                
           
            yield f'A media {count} é {med} e o desvio padrão é {dvp_final:.2f}'
            
t1 = temp_checker(temps)
t1.media()
gen_1 = t1.media()
for g in gen_1:
    print(g)

                                
