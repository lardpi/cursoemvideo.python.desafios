print('Nosso IMC!! \n\n')
print('Olá! Eu posso calcular seu IMC e apresentar sua situação. Quer saber?\n')
peso = float(input('Digite seu peso (em kg): '))
altura = float(input('Digite sua altura (em m): '))
situacoes = {1:'Abaixo do normal',2:'Normal',3:'Sobrepeso',4:'Obesidade Grau I',5:'Obesidade Grau II',6:'Obesidade Grau III'}
imc = peso/(altura**2)
if imc <= 18.5:
    situacao = 1
elif imc <= 24.9:
    situacao = 2
elif imc <= 29.9:
    situacao = 3
elif imc <= 34.9:
    situacao = 4
elif imc <= 39.9:
    situacao = 5
else:
    situacao = 6
print('Considerando seu IMC, sua situação é {}.'.format(situacoes[situacao]))
