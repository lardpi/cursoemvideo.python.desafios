#Curso em Vídeo Python - Mundo 03
#Desafio 082
print("Separador IMPAPAR\n\n")
opcao = "S"
listaoriginal = []
while opcao in ('s','S','n','N'):
    if opcao == 'S':
        numero = int(input('Digite um número: '))
        listaoriginal.append(numero)
        opcao = input('Quer incluir mais um número? (S/N) ').upper()
    else:
        break
print(("-")*10)
listapares = []
listaimpares = []
for c in range(0,len(listaoriginal)):
    if listaoriginal[c]%2 == 0:
        listapares.append(listaoriginal[c])
    else:
        listaimpares.append(listaoriginal[c])

print(f"A lista original contém os {len(listaoriginal)} números seguintes: {listaoriginal}")
print(f"A lista dos pares contém os {len(listapares)} números seguintes: {listapares}")
print(f"A lista dos ímpares contém os {len(listaimpares)} números seguintes: {listaimpares}")
