print('Calcula TINTA')
largura = float(input('Digite a largura da parede (em metros): '))
altura = float(input('Digite a altura da parede (em metros): '))
area = largura*altura
consumo = area/2
print('Para pintar uma parede com área de \033[46m{:.2f}m²\033[m, você precisará de \033[46m{:.2f}l\033[m de tinta.'.format(area,consumo))
