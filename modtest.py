'''
Este exercício tem a seguinte problemática: 
- Cria um módulo para quando o usuário digitar um número ele dar o fatorial 
- Crir um módulo quando digitar 3 notas dar a média 
- Criar um módulo quando digitar um numero ou palavra retornar uma resposta

'''

def fatorial (num):
    fat = 1
    while (num > 0):
        fat = fat*num
        num = num - 1
    
    return f'O fatorial é: {fat}'

def nota():
    n1 = float(input("digite a primeira nota: "))
    n2 = float(input("digite a primeira nota: "))
    n3 = float(input("digite a primeira nota: "))

    media = (n1 + n2 + n3)/3

    return f'A média da nota é {media}'

def nome (frase):
    n = str(input("palavra: "))
    print(f'{frase}: {n}')
    return n

def numero(num):
    a = int(input("Numero: "))
    print(f'{num}: {a}')
    return a


