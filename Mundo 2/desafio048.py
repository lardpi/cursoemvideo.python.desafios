#DESAFIO 048
print('SIGMA MULT3')
print('\nEntre 1 e 500, os números múltiplos de 3 são:')
soma = 0
for c in range(1,501,2):
    if (c%3)==0:
        print(c)
        soma += c
print('A soma dos múltiplos de 3 ímpares entre 1 e 500 dá {}.'.format(soma))
