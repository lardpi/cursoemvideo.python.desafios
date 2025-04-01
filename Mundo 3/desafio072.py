num = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove',
'Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove',
'Vinte')
print('NUMEXT')
numero = -1
while not 0 <= numero <= 20:
    numero = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {num[numero]}.')
