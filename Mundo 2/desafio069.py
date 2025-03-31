#Curso em Vídeo
#Python Mundo 02
#Desafio 69
import random
print('Bem-vindo ao Omnes Gentes!\n')
print('Vamos efetuar o cadastro de várias pessoas, com os dados sexo e idade.')
resposta = 'S'
maiordeidade = 0
homens = 0
mulheresmenosvinte = 0
pessoas = 0
while resposta == 'S':
    idade = int(input('\nDigite a idade da pessoa (em anos): '))
    sexo = input('Digite o sexo da pessoa (M - Masculino; F - Feminino): ').upper()
    pessoas+=1
    if sexo == 'M':
        homens+=1
    elif idade < 20:
        mulheresmenosvinte+=1
    if idade >= 18:
        maiordeidade+=1
    resposta = input(f'{pessoas} pessoas foram cadastradas. Deseja cadastrar mais alguém? (S - Sim; N - Não): ').upper()
print('=-'*25,'\n')
print(f'DAS {pessoas} PESSOAS CADASTRADAS TEMOS:')
print(f'A - {maiordeidade} pessoas maiores de 18 anos.')
print(f'B - {homens} homens cadastrados.')
print(f'C - {mulheresmenosvinte} mulheres abaixo dos 20 anos.')

      
                        
