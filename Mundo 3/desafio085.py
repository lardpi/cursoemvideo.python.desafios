#Curso em Vídeo Python - Mundo 03
#Desafio 085
print("UNI-SEGREGATION\n")
lista = list()
pares = list()
impares = list()
num = 0
for cont in range(0,6):
    num = int(input(f'Digite o {cont+1}º número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
lista.append(pares[:])
lista.append(impares[:])
print(f'Números pares: {lista[0]}.')
print(f'Números ímpares: {lista[1]}.')
