print('CONVERSOR DE TEMPERATURA')
tempC = float(input('Digite a temperatura em graus Celsius: '))
tempF = tempC*1.8+32
tempK = tempC+273.15
print('A temperatura de {}ª C é igual a {}ª F e {} K.'.format(tempC,tempF,tempK))
