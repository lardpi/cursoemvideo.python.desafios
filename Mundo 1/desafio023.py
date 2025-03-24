numero = input('Digite aqui um número para ser decomposto: ')
print('Unidades: {}'.format(numero[len(numero)-1]))
print('Dezenas: {}'.format(numero[len(numero)-2]))
print('Centenas: {}'.format(numero[len(numero)-3]))
print('Milhares: {}'.format(numero[len(numero)-4]))
print('Dezenas de milhares: {}'.format(numero[len(numero)-5]))
print('Centenas de milhares: {}'.format(numero[len(numero)-6]))
print('Milhões: {}'.format(numero[len(numero)-7]))

#A solução do professor faz uso de divisão por um número e módulo por 10. Ex: unidade = numero // 1 % 10; dezena = numero // 10 % 10.
