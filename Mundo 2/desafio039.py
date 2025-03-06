import datetime
print('_-_- Alista FORCE -_-_')
anoNasc = int(input('Digite o ano que você nasceu: '))
anoAtual = datetime.date.today().year
diferenca = anoAtual - anoNasc
if diferenca < 18:
    print('Aguarde mais um pouco. Daqui a {} anos você poderá se alistar.'.format(18 - (anoAtual-anoNasc)))
elif diferenca == 18:
    print('Parabéns! Este é o ano certo para você fazer seu alistamento militar.')
else:
    print('Lamento... Você deveria ter feito o alistamento há {} anos.'.format((anoAtual-anoNasc)-18))
