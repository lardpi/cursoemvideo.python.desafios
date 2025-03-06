print('### quem é o MAIOR ? 1.0 ###')
print('Este programa comparará dois números inteiros.')
numero1 = int(input('Digite o número 1: '))
numero2 = int(input('Digite o número 2: '))
if numero1 == numero2:
    print('Não existe valor maior, pois os dois números são iguais.')
elif numero1 > numero2:
    maior = numero1
    print('O número maior é {}.'.format(maior))
else:
    maior = numero2
    print('O número maior é {}.'.format(maior))
