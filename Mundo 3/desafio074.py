#Curso em Vídeo Python - Mundo 03
#Desafio 074
import random
print('Bem-vindo ao TUP MinMax 2025.')
print('Primeiramente vou preencher uma tupla com 5 números aleatórios entre 0 e 100.')
tupla = (random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100))
print(f'Pronto! A tupla ficou assim: {tupla}.')
print(f'Agora ei-la ordenada: {sorted(tupla)}.')
print(f'O menor número é {sorted(tupla)[0]} e o maior é {sorted(tupla)[-1]}.')
