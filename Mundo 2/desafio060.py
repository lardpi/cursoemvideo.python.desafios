import time
import random
#Curso em Vídeo
#Python 3 - Mundo 02
#Desafio 060
num = 0
fat = 0
print('Este é o FATGEN!')
num = int(input('Informe um número inteiro e lhe darei o fatorial dele: '))
fat = num
cont = num
while cont > 1:
    fat*=cont-1
    cont-=1
print('O fatorial de {} é {}.'.format(num,fat))
