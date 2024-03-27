'''
Este exercício tem a seguinte problemática:

Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os armazene dentro de uma lista. Após a leitura, crie outra estrutura de repetição para somar todos os valores digitados

'''
lista = []
som = 0
for i in range(0,5):
    num = int(input(" Digite um número: "))
    lista.append(num)
    som += num



print(f'A lista preenchida é: {lista}')
print(f'O valor da soma é: {som}')
