'''
Este exercício tem a seguinte problemática: 

Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: adição, subtração, multiplicação e divisão

'''


n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

r1 = n1 + n2
r2 = n1 - n2
r3 = n1*n2
r4 = n1/n2

print(f'O resultado da soma de {n1} com {n2} é igual a: {r1}')
print(f'O resultado da subtração de {n1} com {n2} é igual a: {r2}')
print(f'O resultado da multiplicação de {n1} com {n2} é igual a: {r3}')
print(f'O resultado da divisão de {n1} com {n2} é igual a: {round(r4,2)}')