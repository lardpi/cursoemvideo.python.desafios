import datetime
print('---- B6: seu informe de anos bissextos ----\n\n')
ano = int(input('Digite o ano para pesquisa: '))
print('Esse ano é bissexto.' if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else 'Esse ano não é bissexto.')
