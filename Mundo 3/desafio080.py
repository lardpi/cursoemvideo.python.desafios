#Curso em Vídeo Python - Mundo 03
#Desafio 080
lista = []
print('Ordena LST')
print('Forneça 5 números. Eles serão inseridos de forma ordenada numa lista.')
for c in range(0,5):
    n = int(input('Digite um número: '))
    pos = 0
    if len(lista)==0:
        lista.insert(0,n)
    else:
        for d in range (0,len(lista)):
            if n <= lista[d]:
                pos = d
                break
            else:
                pos = d+1
        if pos < len(lista):
            lista.insert(pos,n)
        else:
            lista.append(n)
    print(lista)
                
