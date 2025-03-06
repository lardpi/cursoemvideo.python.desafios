print('\|/ ACADEMVS \|/')
notaMes1 = float(input('Digite a nota da primeira avaliação: '))
notaMes2 = float(input('Digite a nota da segunda avaliação: '))
mediaBim = float((notaMes1+notaMes2)/2)
print('A média foi {:.2f}. Resultado:'.format(mediaBim))
if mediaBim < 5:
    print('R E P R O V A D O')
elif mediaBim <6.9:
    print('R E C U P E R A Ç Ã O')
else:
    print('A P R O V A D O')
