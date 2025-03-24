nome = input('Digite aqui um nome completo de pessoa para análise: ')
print('Em maiúscula: {}'.format(nome.upper()))
print('Em minúscula: {}'.format(nome.lower()))
print('Caracteres sem espaço: {}'.format(len(nome.strip())-nome.count(' ')))
print('Letras no primeiro nome: {}'.format(len(nome.split()[0])))

