#Curso em Vídeo
#Python Mundo 02
#Desafio 62
print('Uaile Pi-Ei Versão 2025.3.20 Premium')
termo = int(input('Digite um valor para o termo inicial: '))
razao = int(input('Digite um valor para a razão da progressão: '))
n = 9
nesimo = termo+n*razao
maistermos = 0
c = termo
while c <= termo+n*razao:
    print(c)
    if c == termo+n*razao:
        print('Quer que eu mostre mais alguns termos?\nSe sim, digite a quantidade. Se não, digite 0.')
        maistermos = int(input())
        if  maistermos > 0:
            n+=maistermos
    c += razao
print('Listagem concluída.')
