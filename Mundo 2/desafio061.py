#Curso em Vídeo
#Python Mundo 02
#Desafio 61
print('Uaile Pi-Ei Versão 2025.3.20 Premium')
termo = int(input('Digite um valor para o termo inicial: '))
razao = int(input('Digite um valor para a razão da progressão: '))
n = 9
nesimo = termo+n*razao
c = termo
while c <= nesimo:
    print(c)
    c += razao
print('Listagem concluída.')
