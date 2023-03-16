fruits =['banana','apple', 'cranberry']
aml = 0
for w in fruits:
    for l in w:
        aml+=1
    print(w,aml)

dados=[ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
for a in dados:
    print(a)
tabela = []
cont = 0
for l in range(3):
    linha= []
    for i in range(3):
        cont += 1
        linha.append(cont)F
    tabela.append(linha)
print(tabela)

m = 2
for n in range(10):
    for m in range(10):
        print((m+1)*(n+1))