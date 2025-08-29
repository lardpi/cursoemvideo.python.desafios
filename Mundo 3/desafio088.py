#Curso em Vídeo Python - Mundo 03
#Desafio 088
import random
print("MEGA SEIS\n")
qtjogos = 0
num = 0
jogo = list()
jogos = list()
qtjogos = int(input('Digite a quantidade de jogos que deseja fazer: '))
print(f'\n...O sistema gerará aleatoriamente 6 números para cada um dos {qtjogos} jogos...\n')
for cont1 in range(1,qtjogos+1):
    for cont2 in range(1,7):
        while num in (jogo) or num == 0:
            num = random.randrange(1,61)
        jogo.append(num)
    jogo.sort()
    print(f'{cont1}º jogo: {jogo}.')
    jogos.append(jogo[:])
    jogo.clear()
print('\nAí estão seus números! Boa sorte!')
