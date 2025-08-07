#Curso em Vídeo Python - Mundo 03
#Desafio 078
lista = []
print('MMList')
print('Preciso que me passe 5 números:')
for c in range(0,5):
    lista.append(int(input(f'Valor {c+1}: ')))
print(f'A lista digitada foi: {lista}.')
menor = min(lista)
maior = max(lista)
posmenor = lista.index(menor)
posmaior = lista.index(maior)
print(f'O menor número digitado foi {menor} na posição {posmenor}, e o maior foi o número {maior} na posição {posmaior}.')
