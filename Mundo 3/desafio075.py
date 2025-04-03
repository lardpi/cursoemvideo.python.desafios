#Curso em Vídeo Python - Mundo 03
#Desafio 075
print('Bem-vindo ao Tupla Hunter!')
print('Vamos preencher uma tupla com 4 números. Você precisa digitá-los.')
tupla = (int(input('Número 1: ')),int(input('Número 2: ')),int(input('Número 3: ')),int(input('Número 4: ')))
contanove = tupla.count(9)
postres = tupla.index(3)
print(f'O número 9 apareceu {contanove} vezes na tupla.')
print(f'O primeiro número três foi encontrado na posição {postres}.')
print(f'Os números pares da tupla foram: ')
for numero in tupla:
    print(numero if numero%2==0 else next)
