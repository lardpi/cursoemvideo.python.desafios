print('APLICADOR DE AUMENTO')
salario = float(input('Digite o salário do funcionário: R$ '))
aumento = float(input('Digite o percentual de aumento desejado: '))
novosalario = salario+salario*(aumento/100)
print('O salário de R$ {:.2f} com {}% de aumento fica \033[1;32mR$ {:.2f}\033[m.'.format(salario,aumento,novosalario))
