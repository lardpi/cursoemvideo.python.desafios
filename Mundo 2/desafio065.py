#Curso em Vídeo
#Python Mundo 02
#Desafio 65
print('SomaTUDO Plus')
print('Este programa somará todos os números digitados, apresentará a média, o menor e o maior.\n')
opcao = 'S'
maior = -1
menor = -1
soma = 0
media = 0
quantidade = 0
numero = -1
while opcao != 'N':
    numero = int(input('Digite um número: '))
    if quantidade == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    quantidade+=1
    soma+=numero
    opcao = input('Deseja digitar mais um número? (S - SIM ou N - NÃO) ')
media = float(soma/quantidade)
print('#'*10+'\n')
print('Foram digitados {} números, a soma deles é {} e a média é {}.'.format(quantidade,soma,media))
print('O maior número foi {} e o menor foi {}.'.format(maior,menor))
