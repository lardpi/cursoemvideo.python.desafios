import time
import random
#Curso em Vídeo
#Python 3 - Mundo 02
#Desafio 058
npens = 0
nsug = -1
qtpalp = 1
print('Olá, amiguinho! Eu sou o Dr. Pensatudo.')
time.sleep(1)
print('Quero saber se és mesmo muito esperto como dizes...')
time.sleep(1)
print('Pensarei em um número.')
for c in range(0,2):
    print('Pensando...')
    time.sleep(1)
print('PENSEI!\n')
npens = random.randrange(0,10)
print('Agora, dize-me: que número está em meu pensamento?')
nsug = int(input('Eu acho que é '))
while nsug != npens:
    print('NÃO.')
    qtpalp+=1
    nsug = int(input('Bem, então deve ser '))
if qtpalp == 1:
    print('UAU! Acertaste de primeira!')
else:
    print('Aê! Muito bem! Acertaste no {}º palpite! '.format(qtpalp))
print('Obrigado por me divertires.')
