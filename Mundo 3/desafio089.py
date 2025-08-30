# Curso em Vídeo Python - Mundo 03
# Desafio 089
print('[     BEM-VINDO AO PyCademic     ]\n')
turma = list()
aluno = list()
aluno_notas = list()
id = 1
nome = ''
nota1 = 0
nota2 = 0
media = 0
resposta = 'S'
print('Você deverá informar os nomes dos alunos e suas notas para fins de controle acadêmico e geração de boletim.')
while resposta in 'SN':
    if resposta == 'S':
        nome = input('Digite o nome do aluno: ')
        aluno_notas.append(float(input('Digite a primeira nota: ')))
        aluno_notas.append(float(input('Digite a segunda nota: ')))
        aluno.append(id)
        aluno.append(nome)
        aluno.append(aluno_notas[:])
        turma.append(aluno[:])
        id += 1
        aluno_notas.clear()
        aluno.clear()
    elif resposta == 'N':
        break
    else:
        print('Sua resposta foi inválida!')
    resposta = input('Deseja incluir mais algum aluno? ').upper()
print('#########################################\n')
print('___________________________________________')
print('|                BOLETIM                  |')
print('___________________________________________')
print('[ ID ][ ALUNO ]          [ MÉDIA ]         ')
print('-------------------------------------------')
for cont in range (0,len(turma)):
    media = (turma[cont][2][0]+turma[cont][2][1])/2
    print(f'[ {turma[cont][0]} ][ {turma[cont][1]} ][ {media} ]')
print('\n')
resposta = -1
while not resposta == 0:
    if resposta > 0:
        print(f'Nome: {turma[resposta-1][1]}')
        print(f'Nota 1: {turma[resposta-1][2][0]}; Nota 2: {turma[resposta-1][2][1]}\n')
    resposta = int(input('Digite o ID de um aluno para ver suas notas ou 0 para encerrar: '))
print('PyCademic agradece o seu acesso!')