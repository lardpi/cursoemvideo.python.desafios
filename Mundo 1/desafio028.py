import random
print('TENTE ADIVINHAR!')
queroTentar = True
while queroTentar:
    numero = random.randint(0,5)
    print('A-ha! Acabei de pensar num número qualquer entre 0 e 5. Adivinhe qual é!')
    tentativa = int(input('Eu acho que foi: '))
    print('Você acertou!' if tentativa==numero else 'Errou!')
    if input('Quer tentar novamente? (S ou N) ') == 'S':
        queroTentar = True
    else:
        queroTentar = False
