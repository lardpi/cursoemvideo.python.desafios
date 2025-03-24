print('Bem-vindo ao SANTO COMEÇO, o detector de cidades iniciadas por SANTO!')
nome = input('Digite aqui o nome de cidade a ser investigado: ')
if (nome.upper().find('SANTO') == 0):
    print('Este nome de cidade inicia com SANTO.')
else:
    print('Este nome de cidade NÃO inicia com SANTO.')

#O professor resolve utilizando verificação de condição dentro do print.
#Ex: print(nome[:5].upper() == 'SANTO')
