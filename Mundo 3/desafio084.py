#Curso em Vídeo Python - Mundo 03
#Desafio 084
print("TOP WEIGHT 2K25\n")
resp = 'S'
lista = list()
pessoa = list()
while resp in ('SN'):
    if resp == 'S':
        pessoa.append(input('Nome: '))
        pessoa.append(float(input('Peso (kg): ')))
        lista.append(pessoa[:])
        pessoa.clear()
    elif resp == 'N':
        print('Certo. Vamos parar por aqui.')
        break
    else:
        print('Não consegui entender sua resposta. Tente novamente.')
    resp = input('Você deseja incluir mais alguém? (S/N) ').upper()
qtpessoas = len(lista)    
print(f'Foram cadastradas {qtpessoas} pessoas.')
pesototal = 0
menorpeso = 200
maiorpeso = 0
for cont in range(0,len(lista)):
    pesototal += lista[cont][1]
    if lista[cont][1] > maiorpeso:
        maiorpeso = lista[cont][1]
    elif lista[cont][1] < menorpeso:
        menorpeso = lista[cont][1]
mediapeso = pesototal/qtpessoas
print(f'Média do peso: {mediapeso} kg.')
acimed = list()
abamed = list()
for cont in range(0,len(lista)):
    if lista[cont][1] > mediapeso:
        acimed.append(lista[cont][0])
    elif lista[cont][1] < mediapeso:
        abamed.append(lista[cont][0])
print(f'As pessoas com peso acima da média foram: {acimed}.')
print(f'As pessoas com peso abaixo da média foram: {abamed}.')
print(f'O maior peso registrado foi de {maiorpeso}kg. E o menor foi de {menorpeso}kg.')    

