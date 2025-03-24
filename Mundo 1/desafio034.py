print('--- SALACALC ---\n\n')
salario = float(input('Digite o salário do colaborador: R$ '))
if salario>=1250:
    percentual = 0.10
else:
    percentual = 0.15
print('Para este salário o aumento será de {}%. O novo valor será de R$ {}.'.format(percentual*100,salario+(salario*percentual)))
