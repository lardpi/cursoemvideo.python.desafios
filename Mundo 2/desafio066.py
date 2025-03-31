#Curso em Vídeo
#Python Mundo 02
#Desafio 66
print('SomaTUDO Break')
print('Este programa somará todos os números digitados.\n')
soma = quantidade = numero = 0
while True:
    numero = int(input('Digite um número (999 para parar): '))
    if numero!=999:
        quantidade+=1
        soma+=numero
    else:
        break
print('#'*10+'\n')
print(f'Foram digitados {quantidade} números e a soma deles é {soma}.')
