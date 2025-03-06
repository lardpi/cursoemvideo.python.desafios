#Curso em Vídeo Python
#Mundo 2
#DESAFIO 054
import datetime
print('IdentOLDER')
print('Informe o ano de nascimento de sete pessoas:')
anos = {}
qtMaiores = 0
qtMenores = 0
for c in range (0,7):
    anos[c] = int(input('{}. '.format(c)))
    if (datetime.datetime.now().year-anos[c]) >= 18:
        qtMaiores += 1
    else:
        qtMenores += 1
print('Considerando os anos de nascimento informados, temos:')
print('Quantidade de maiores de idade: {} pessoas.'.format(qtMaiores))
print('Quantidade de menores de idade: {} pessoas.'.format(qtMenores))
