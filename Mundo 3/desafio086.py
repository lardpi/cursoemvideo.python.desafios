#Curso em Vídeo Python - Mundo 03
#Desafio 086
print("The Matrix Maker\n")
matriz = list()
linhacheia = list()
num = 0
for linha in range(0,3):
    for coluna in range(0,3):
        num = int(input(f'Digite o número da posição {linha},{coluna}: '))
        linhacheia.append(num)
    matriz.append(linhacheia[:])
    linhacheia.clear()
print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
