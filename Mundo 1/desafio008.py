print('Conversor de medidas.')
valor = float(input('Digite o valor em metros: '))
cent = valor*100
mili = valor*1000
print('A medida de \033[32m{}m\033[m equivale a \033[33m{}cm\033[m ou \033[34m{}mm\033[m.'.format(valor,cent,mili))