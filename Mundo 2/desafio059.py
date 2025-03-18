import time
import random
#Curso em Vídeo
#Python 3 - Mundo 02
#Desafio 059
num1 = -1
num2 = -1
opcao = 0
maior = -1
print('Bem-vindo ao TETROP!')
print('Este programa trabalha de acordo com suas escolhas.')
print('Você dirá o que devo fazer com dois números à sua escolha.')
num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
print('Confira o menu abaixo e faça sua escolha.')
while opcao < 5:
    print('\n1: SOMAR\n2: MULTIPLICAR\n3: MAIOR\n4: ESCOLHER NOVOS NÚMEROS\n5: SAIR')
    opcao = int(input('Opção: '))
    if opcao == 1:
        print('A soma de {} e {} é {}.'.format(num1,num2,num1+num2))
    elif opcao == 2:
        print('O produto de {} por {} é {}.'.format(num1,num2,num1*num2))
    elif opcao == 3:
        print('O maior número entre {} e {} é {}.'.format(num1,num2,max(num1,num2)))
    elif opcao == 4:
        num1 = int(input('Número 1: '))
        num2 = int(input('Número 2: '))
    elif opcao > 5:
        print('Opção inválida!')
print('\nF I M')
    
