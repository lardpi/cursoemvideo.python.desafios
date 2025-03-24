import math
numreal = float(input('Digite um número real qualquer: '))
parteinteira = int(math.modf(numreal)[1])
partedecimal = math.modf(numreal)[0]
print('A parte inteira de {} é {} e a parte decimal é {}.'.format(numreal,parteinteira,partedecimal))
