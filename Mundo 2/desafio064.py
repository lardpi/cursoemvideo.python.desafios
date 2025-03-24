#Curso em Vídeo
#Python Mundo 02
#Desafio 64
print('SomaTUDO')
print('Este programa somará todos os números digitados.\n')
print('Para terminar, digite 999.')
digitado = 0
quantidade = -1
soma = 0
while digitado != 999:
    quantidade+=1
    soma+=digitado
    digitado = int(input('Digite um número: '))
print('#'*10+'\n')
print('Foram digitados {} números e a soma deles é {}.'.format(quantidade,soma))
