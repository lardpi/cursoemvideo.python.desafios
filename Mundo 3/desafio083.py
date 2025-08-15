#Curso em Vídeo Python - Mundo 03
#Desafio 082
print("X-VAL\n")
val = 0
exp = input("Digite uma expressão matemática/algébrica: ")
for c in range(0,len(exp)):
    if val >= 0:
       if exp[c] == '(':
           val+=1
       elif exp[c] == ')':
           val-=1
    else:
        print('Parênteses utilizados incorretamente. Expressão inválida!')
        break
if val == 0:
    print('A expressão está válida segundo os parâmetros do aplicativo.')
else:
    print('Há mais parênteses do que o necessário. Favor corrigir.')
