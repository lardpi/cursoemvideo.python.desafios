#Curso em Vídeo Python - Mundo 03
#Desafio 077
tupla = ('família','futuro','vida','alegria','mandamentos','quaresma','trabalho','cotidiano')
print(f'Na tupla dada há {len(tupla)} palavras.')
for palavra in tupla:
    print(f'Na palavra {palavra.upper()} temos as vogais: ',end='')
    for letra in palavra:
        if letra.upper() in ('AEIOUÁÀÂÃÉÍÓÔÕÚ'):
            print(letra,end=',')
    print()
