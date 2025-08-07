#Curso em Vídeo Python - Mundo 03
#Desafio 079
lista = []
n = -998
print("/\\"*15)
print(f'{"UNIQUE LST":^30}')
print("\\/"*15)
print('Preciso que me forneça alguns números.')
while True:
    n = int(input('Digite um número (ou -999 para finalizar): '))
    if n == -999:
        print('Ok. Finalizando a lista.')
        break
    elif n not in lista:
        lista.append(n)
    else:
        print('Este valor já está na lista.')
print(f'A sua lista de valores únicos é composta por: {sorted(lista)}.')
    
