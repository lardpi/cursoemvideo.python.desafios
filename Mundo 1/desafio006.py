print('\033[4mHora do jogo do dobro, do triplo e da raiz quadrada. Dê-me um número.\033[m')
num = float(input('Número: '))
print('O dobro de {} é {}, \no triplo é {} \ne a raiz quadrada é {:.2f}.'.format(num,num*2,num*3,num**0.5))