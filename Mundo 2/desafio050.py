#DESAFIO 050
numeros = {}
soma = 0
qtpar = 0
print('+6PAR')
print('Dê-me 6 números e eu retornarei a soma dos que forem pares entre eles.')
for c in range(1,7):
    numeros[c] = int(input('{}: '.format(c)))
    if numeros[c]%2 == 0:
        soma+=numeros[c]
        qtpar+=1
print('Você digitou {} números pares e a soma deles é {}.'.format(qtpar,soma))

