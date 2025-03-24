print('Calculadora de média bimestral.')
aluno = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2
print('{} tirou {} e {} e, portanto, sua média bimestral é \033[1m{:.2f}\033[m.'.format(aluno,nota1,nota2,media))