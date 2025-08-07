#Curso em Vídeo Python - Mundo 03
#Desafio 081
opcao = "S"
lista = []
while opcao in ('s','S','n','N'):
    if opcao == 'S':
        numero = int(input('Digite um número: '))
        lista.append(numero)
        opcao = input('Quer incluir mais um número? (S/N) ').upper()
    else:
        break
print(("-")*10)
lista.sort(reverse=True)
if len(lista)==1:
    print('Só foi digitado 1 número na lista.')
else:
    print(f"Foram digitados {len(lista)} números numa lista.")
print(f"A lista, em ordem descrescente, é: {lista}")
if 5 in lista:
    print("O número 5 está presente.")
else:
    print("O número 5 não está presente.")
