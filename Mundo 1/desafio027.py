nomeCompleto = input('Digite seu nome completo: ')
primeiroNome = nomeCompleto[0:nomeCompleto.find(' ')]
ultimoSobrenome = nomeCompleto[nomeCompleto.rfind(' ')+1:len(nomeCompleto)]
print('Ah, entendi! Seu nome de usuário será {} {}.'.format(primeiroNome,ultimoSobrenome))

#O professor resolveu fazendo uso do split e pegando nome[0] e nome[len(nome)-1].
