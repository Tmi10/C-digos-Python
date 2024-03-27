'''
Este exercício tem a seguinte problemática: 

Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é a temperatura em graus Celsius
- Função para ler e retorna o valor da temperatura (não recebe parâmetro)
- Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius)
- Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão

'''

def ler():
    temp = float(input("Digite o valor da temperatura em celsus: "))
    return temp

def transf():
    C = ler()
    temp_f = (9*C + 160)/5
    return temp_f

def imprim():
    F = transf()
    return(f'O valor da temperatura em Fahrenheit é: {F}')

view = imprim()
print(f'{view}')
