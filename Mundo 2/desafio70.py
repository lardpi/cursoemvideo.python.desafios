#Curso em Vídeo
#Python Mundo 02
#Desafio 70
print('Bem-vindo ao KOMPRAKOiZA!\n')
print('Vamos efetuar a compra de produtos, registrando seus nomes e preços.')
resposta = 'S'
caros = 0
menorpreco = 0
maisbarato = 0
produtos = 0
gasto = 0
while resposta == 'S':
    nome = input('\nDigite o nome do produto: ').upper()
    preco = float(input('Digite o preço do produto: R$ '))
    gasto+=preco
    produtos+=1
    if (produtos==1 or preco < menorpreco):
        maisbarato = nome
        menorpreco = preco
    if preco >= 1000:
        caros+=1
    resposta = input(f'{produtos} produtos foram cadastrados. Deseja cadastrar mais algum? (S - Sim; N - Não): ').upper()
print('=-'*25,'\n')
print(f'DOS {produtos} PRODUTOS CADASTRADOS TEMOS:')
print(f'A - Foram gastos R$ {gasto:.2f} na compra.')
print(f'B - {caros} produtos estão acima de R$ 1.000,00.')
print(f'C - O produto mais barato foi {maisbarato}, que custou R$ {menorpreco:.2f}.')

      
                        
