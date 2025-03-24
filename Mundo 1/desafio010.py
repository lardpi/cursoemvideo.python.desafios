print('DÓLAR HOJE!')
valor = float(input('Digite o quanto você tem na carteira (R$): '))
dolar = 6.03
print('\033[34mA quantia de R$ {} vale US$ {:.2f} na cotação de hoje.\033[m'.format(valor,valor/dolar))