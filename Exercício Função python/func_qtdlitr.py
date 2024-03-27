'''
Este exercício tem a seguinte problemática: 

Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem
- Função para ler os valores (não recebe parâmetro e retorna os dois valores)
- Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)
- Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros)
- Função para apresentar o resultado (recebe como parâmetro os valores e somente imprime o resultado)

'''

def leitura(): 
    tempo = float(input("Digite o tempo percorrido: "))
    velocidade = float(input("Digite a velocidade percorrida: "))
    return tempo, velocidade

def calc(tempo, velocidade):
    distancia = tempo*velocidade
    return distancia

def quant(distancia):
    litros = distancia/12
    return litros

def receb(tempo, velocidade, distancia, litros):
    return(f'o tempo é: {tempo}, a velocidade é: {velocidade}, a distancia é: {distancia}, a qntd de litros é {litros}')

temp, veloc = leitura()
dist = calc(temp, veloc)
qtd = quant(dist)
imprim = receb(temp,veloc,dist,qtd)

print(f'{imprim}')
