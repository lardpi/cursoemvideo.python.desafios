import math
cateop = float(input('Digite o valor do cateto oposto: '))
catead = float(input('Digite o valor do cateto adjacente: '))
hipote = math.hypot(cateop,catead)
print('A hipotenusa de um triângulo cujos catetos são {} e {} é {}.'.format(cateop,catead,hipote))
