'''
Este exercício tem a seguinte problemática: 

Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem

'''

tempo = float(input("Digite o tempo percorrido: "))
velocidade = float(input("Digite a velocidade média: "))

Distancia = tempo*velocidade

Litros_usados = Distancia/12

print(f'o tempo percorrido é {tempo}, a velocidade média é {velocidade}, a distância percorrido é {Distancia}, a quantidade de litros usados é {round(Litros_usados,1)}')