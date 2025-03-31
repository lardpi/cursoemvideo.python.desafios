#Curso em Vídeo
#Python Mundo 02
#Desafio 67
print('TABU Break')
print('Este programa apresenta a tábua de multiplicação para os números escolhidos.\n')
numero = 0
while True:
    numero = int(input('Digite um número (negativo para parar): '))
    if numero >= 0:
        c = 1
        for c in range(1,11):
            print(f'{numero} x {c} = {numero*c}')
    else:
        break
print('#'*10+'\n')
print('FIM')
