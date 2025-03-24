print('Bem-vindo ao SILTECTOR, o detector de Silvas')
nome = input('Digite aqui o nome a ser investigado: ')
print('Presença de SILVA no nome dado: {}'.format(nome.upper().count('SILVA')))

#O professor resolve utilizando a expressão de verificação de presença: format('silva' in nome)
