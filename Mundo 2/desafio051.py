#DESAFIO 051
print('/\\'*3,' Meus 10 na PA ','/\\'*3)
print('Vamos trabalhar com progressão aritmética!')
termo = int(input('Digite um valor para o termo inicial: '))
razao = int(input('Digite um valor para a razão da progressão: '))
print('Os 10 primeiros termos da PA com esses parâmetros são:')
for c in range(termo,razao*10,razao):
    print(c)

