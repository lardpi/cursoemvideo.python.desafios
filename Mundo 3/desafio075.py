#Curso em Vídeo Python - Mundo 03
#Desafio 075
print('Bem-vindo ao Tupla Hunter!')
print('Vamos preencher uma tupla com 4 números. Você precisa digitá-los.')
tupla = (int(input('Número 1: ')),int(input('Número 2: ')),int(input('Número 3: ')),int(input('Número 4: ')))
contanove = int(tupla.count(9))
positres = None
listapares = []
if tupla.count(3)>0:
#Aqui o professor põe o equivalente a 'if 3 in tupla'
    positres = tupla.index(3)
print(f'O número 9 apareceu {contanove} vezes na tupla.' if contanove>0 else 'O número 9 não foi encontrado.')
print(f'O primeiro número 3 foi encontrado na posição {positres}.' if positres!=None else 'O número 3 não foi encontrado.')
for c in range(0,4):
    if tupla[c]%2==0:
        listapares.append(tupla[c])
    else: next
print(f'Os números pares da tupla foram: {sorted(listapares)}.' if len(listapares)>0 else 'Não foram encontrados números pares.')
