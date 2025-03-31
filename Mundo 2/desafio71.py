#Curso em Vídeo
#Python Mundo 02
#Desafio 71
print('LARD Bank - seu banco em Python\n')
valorasacar = qt50 = qt20 = qt10 = qt1 = resto = 0
print('Esta agência trabalha somente com cédulas de R$ 1, R$ 10, R$ 20 e R$ 50.\n')
while True:
    valorasacar = int(input('Quanto deseja sacar? (Permitido apenas valor inteiro!) R$ '))
    resto = valorasacar
    if resto >= 50:
        qt50 = int(resto/50)
        resto -= (qt50*50)
    if resto >= 20:
        qt20 = int(resto/20)
        resto -= (qt20*20)
    if resto >= 10:
        qt10 = int(resto/10)
        resto -= (qt10*10)
    if resto >= 1:
        qt1 = resto
        resto -= (qt1)
    break
print('Contando as cédulas. Você receberá o valor em:')
print(f'{qt50} notas de R$ 50.')
print(f'{qt20} notas de R$ 20.')
print(f'{qt10} notas de R$ 10.')
print(f'{qt1} notas de R$ 1.')
print('=-'*20)
print('Favor retirar as cédulas. Obrigado.')
