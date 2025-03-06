#Curso em Vídeo Python
#Mundo 2
#DESAFIO 056
nome = {}
idade = {}
sexo = {}
media = 0
maiorIdade = 0
homemMaisVelho = 0
mulherMenosVinte = 0
print('--- ClassiPEOPLE ---')
for c in range(1,5):
    print('PESSOA {}'.format(c))
    nome[c] = str(input('Nome: '))
    idade[c] = int(input('Idade: '))
    sexo[c] = str(input('Sexo (M - masculino ou F - feminino: '))
    media += idade[c]
    if sexo[c] == 'M' and idade[c] > maiorIdade:
        maiorIdade = idade[c]
        homemMaisVelho = c
    if sexo[c] == 'F' and idade[c] < 20:
        mulherMenosVinte += 1
media = float(media/4)
print('A média das idades apresentadas é de {} anos.'.format(media))
print('O nome do homem mais velho é {}.'.format(nome[homemMaisVelho]))
print('A quantidade de mulheres abaixo dos 20 anos é {}.'.format(mulherMenosVinte))
