'''
Este exercício tem a seguinte problemática: 

Imprimir a tabuada do número 3 (3 x 1 = 3 ; 3 x 10 = 30)

'''

'''

num = 3

cont = 0

while (cont < 10): 
    cont += 1
    resp = num*cont
    print(f'{num} x {cont} = {resp}')

'''


num = 3

for cont in range(1,11) :
    resp = num*cont
    print(f'{num} x {cont} = {resp}')

