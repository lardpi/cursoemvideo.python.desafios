print('CALCULADORA DE CUSTOS')
kminicio = float(input('Digite a quilometragem incial: '))
kmfim = float(input('Digite a quilometragem final: '))
kmperc = kmfim-kminicio
valorkm = kmperc*0.15
qtdias = int(input('Digite a quantidade de dias pelos quais o carro foi alugado: '))
valordias = qtdias*60
valortotal = valorkm+valordias
print('O valor total a ser pago pela locação e uso do veículo é de R$ {:.2f}.'.format(valortotal))
