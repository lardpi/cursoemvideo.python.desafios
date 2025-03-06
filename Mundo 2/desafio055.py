#Curso em Vídeo Python
#Mundo 2
#DESAFIO 055
pesos = {}
maior = -1
menor = -1
print('8 ou 80 - versão balança')
print('Informe o peso de 5 pessoas em quilogramas. Eu direi qual o mais leve e o mais pesado.')
for c in range(1,8):
    pesos[c] = float(input('Peso (em kg) da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = pesos[c]
        menor = pesos[c]
    elif pesos[c] > maior:
        maior = pesos[c]
    elif pesos[c] < menor:
        menor = pesos[c]
if maior == menor:
    print('Os pesos maior e menor são iguais: {}kg.'.format(maior))
else:
    print('O maior peso registrado foi de {}kg.'.format(maior))
    print('O menor peso registrado foi de {}kg.'.format(menor))
