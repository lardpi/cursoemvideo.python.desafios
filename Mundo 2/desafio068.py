#Curso em Vídeo
#Python Mundo 02
#Desafio 68
import random
print('P ou I The Game')
print('Olá! Venha jogar Par ou Ímpar comigo!\n')
pc = -1
numeropc = 0
jogador = -1
numerojogador = 0
soma = 0
ganhou = 0
while True:
    jogador = (0 if (input('Vamos lá! Par (P) ou Ímpar (I)? ')).upper() == 'P' else 1)
    pc = 1 if jogador == 0 else 0
    numeropc = random.randrange(0,5)
    numerojogador = int(input('Digite um número de 0 a 5: '))
    soma = numeropc+numerojogador
    print('\nJÁÁÁÁ!!!\n')
    print(f'Computador: {numeropc}\nJogador: {numerojogador}\nSoma = {soma}')
    if (soma%2==0 and jogador == 0) or (soma%2>0 and jogador == 1):
            ganhou+=1
            print('AÊÊ! Ganhou essa! Mas vamos mais uma!')
            print('\n','%'*30,'\n')
    else:
            break
print('VOCÊ PERDEU!!')
print(f'Total de vitórias antes de perder: {ganhou}')
