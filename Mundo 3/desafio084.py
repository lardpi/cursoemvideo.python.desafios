# Curso em Vídeo Python - Mundo 03
# Desafio 084
print('PERSONAS Alpha\n')
resposta = 'S'
lista = []
pessoa = []
while resposta in ('SN'):
    if resposta == 'S':
        pessoa.insert(0, input('Digite o nome da pessoa: '))
        pessoa.insert(1, input('Digite o peso da pessoa: '))
        resposta = input('Deseja incluir outra pessoa?')
    else:
        lista.append(pessoa[:])
        break

print(lista)