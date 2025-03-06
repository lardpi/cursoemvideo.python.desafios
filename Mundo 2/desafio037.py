#DESAFIO 037
import sys
print('### NUMCONV ###')
numero = int(input('Informe o número que você deseja converter: '))
bases = {1:'Binária',2:'Octal',3:'Hexadecimal'}
base = int(input('Digite a base de conversão, sendo: {}: '.format(bases)))
if base == 1:
    numConvertido = bin(numero)[2:]
elif base == 2:
    numConvertido = oct(numero)[2:]
elif base == 3:
    numConvertido = hex(numero)[2:]
else:
    print('Base inválida! O número não foi convertido.')
    exit()
print('O número {} convertido para a base {} é {}.'.format(numero,bases[base],numConvertido))
