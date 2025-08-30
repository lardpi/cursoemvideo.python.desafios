#Curso em Vídeo Python - Mundo 03
#Desafio 087
print("The Matrix Maker\n")
matriz = list()
linhacheia = list()
num = 0
somapares = 0
somatercol = 0
maiorseglin = 0
for linha in range(0,3):
    for coluna in range(0,3):
        num = int(input(f'Digite o número da posição {linha},{coluna}: '))
        if num % 2 == 0:
            somapares += num
        if coluna == 2:
            somatercol += num
        if linha == 1:
            if num > maiorseglin:
                maiorseglin = num
        linhacheia.append(num)
    matriz.append(linhacheia[:])
    linhacheia.clear()
print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
print(f'A soma de todos os valores pares digitados é {somapares}.')
print(f'Já a soma dos valores da terceira coluna é {somatercol}.')
print(f'Por fim, o maior valor da segunda linha é {maiorseglin}.')
