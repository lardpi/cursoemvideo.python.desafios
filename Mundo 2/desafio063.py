#Curso em Vídeo
#Python Mundo 02
#Desafio 63
print('FiboN Community')
print('Este programa apresenta termos da sequência de Fibonacci.\n')
print('Informe a quantidade de termos que deseja que sejam apresentados: ')
ultimo = 0
atual = 1
c = 1
qttermos = int(input())
while c <= qttermos:
    print(atual)
    novo = atual + ultimo
    ultimo = atual
    atual = novo
    c+=1
print('Listagem terminada.')
