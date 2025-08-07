#Curso em Vídeo Python - Mundo 03
#Desafio 076
print('BóComprar - Sua lista de compras')
print('Forneça os nomes e preços de cada item. Digite FIM como produto para concluir.')
nome = ''
lista = []
while nome.upper()!='FIM':
    if nome!='':
        lista.append(nome)
        lista.append(float(input('Preço: R$ ')))
    nome = str(input('Produto: '))
tupla = tuple(lista)
print('='*30)
print(f"{'LISTA DE PREÇOS':^30}")
print('='*30)
print(f"{'Produtos':^20}{'Valores':^10}")
for c in range(0,len(tupla),2):
    print(f"{tupla[c]:.<20}R$ {tupla[c+1]:>8.2f}")
