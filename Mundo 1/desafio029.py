print('---SENSOR DA STRANS---')
velocidade = int(input('Em que velocidade o carro acaba de passar pelo sensor? '))
if velocidade >= 80:
    multa = float((velocidade-80)*7)
    print('Velocidade acima da máxima permitida. Você cometeu infração.\nSua multa é de R$ {:.2f}.'.format(multa))
else:
    print('Velocidade permitida. Sem infração. Sem multa.')
