print('--- QUEM É O MENOR?! ---\n\n')
num1 = int(input('Digite o número 1: '))
num2 = int(input('Digite o número 2: '))
num3 = int(input('Digite o número 3: '))
if num1 < num2:
    menor = num1
    maior = num2
else:
    menor = num2
    maior = num1
if num3 < menor:
    menor = num3
if num3 > maior:
    maior = num3
print('O menor número digitado foi {}.'.format(menor))
print('O maior número digitado foi {}.'.format(maior))
