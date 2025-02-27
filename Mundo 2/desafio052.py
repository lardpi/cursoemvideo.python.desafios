#Desafio 052
print('_._Cata Primo Lite_._')
print('Digite um número inteiro e eu verificarei se ele é primo ou não.')
numero = int(input('Seu número: '))
eprimo = True
for c in range(2,numero):
    if numero%c == 0:
        eprimo = False
if eprimo:
    print('Coisa boa! {} é sim um número primo!'.format(numero))
else:
    print('Bem, {} não é um número primo.'.format(numero))
