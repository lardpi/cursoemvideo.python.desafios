print('~~~ Confederação Nacional de Natação ~~~')
print(' - Classificador de Atletas - \n\n')
anoNasc = int(input('Digite o ano de nascimento do atleta: '))
anoAtual = 2025
idade = anoAtual-anoNasc
categorias = {1:'Mirim',2:'Infantil',3:'Júnior',4:'Sênior',5:'Master'}
catAtleta = 0
if idade <= 9:
   catAtleta = 1
elif idade <= 14:
    catAtleta = 2
elif idade <= 19:
    catAtleta = 3
elif idade <= 20:
    catAtleta = 4
else:
    catAtleta = 5
print('O atleta tem aproximadamente {} anos de idade e será incluído na Categoria {}.'.format(idade,categorias[catAtleta]))

