'''
Este exercício tem a seguinte problemática: 

Considerando o dicionário com o nome dos alunos e suas respectivas notas abaixo, crie uma estrutura de repetição para percorrer cada elemento do dicionário para gravar cada aluno em um novo arquivo de texto
- Cada aluno deve ocupar uma linha do novo arquivo de texto
- O formato deve ser: nome,nota (Pedro,8.0)
- Após a criação do arquivo de texto, faça a leitura do arquivo e mostre todos os alunos

alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

'''

aluno = []
soma = 0
for i in range(0,3):
    nome = str(input("Digite o nome do aluno: "))
    nota = float(input("Digite a nota do aluno: "))
    soma += nota
    aluno.append((nome,nota))

media = soma / 3

aluno = dict(aluno)

print(f'{aluno}')
print(f'A média dos alunos é {media}')

