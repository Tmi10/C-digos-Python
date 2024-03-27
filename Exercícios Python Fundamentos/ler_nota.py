'''
Este exercício tem a seguinte problemática: 

Ler 5 notas e informar a média

'''

'''

cont = 0
aux = 0
while (cont < 5) :
    cont += 1
    nota = float(input(f'Digite a {cont}ª nota: '))
    aux += nota

media = aux/cont

print(f'A média do aluno é {media}')

'''
aux = 0
for cont in range(1,6):
    nota = float(input(f'Digite a {cont}ª nota: '))
    aux += nota

media = aux/cont
print(f'A média do aluno é {media}')
