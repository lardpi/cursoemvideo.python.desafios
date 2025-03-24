# Desafio 2: Receber um nome e dar boas vindas.
print('Olá, amigo! Como você se chama?')
nome = input('Nome: ')
sobrenome = input('Sobrenome: ')
nomeCompleto = nome,sobrenome
print('Seja bem-vindo, \033[7;34m{} {}\033[m!'.format(nome,sobrenome))

