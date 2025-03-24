print('----PRECIFICADOR DE VIAGEM----\n\n')
percurso = float(input('Digite a distância total da viagem em quilômetros: '))
print('O valor da viagem será de R$ {:.2f}.'.format(percurso*0.5 if percurso <= 200 else percurso*0.45))
