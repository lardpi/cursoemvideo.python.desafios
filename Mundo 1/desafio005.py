print('Forneça um número e eu lhe direi o antecessor e o sucessor dele.')
num = float(input('Número: '))
print('Essa foi fácil! Antes dele vem \033[4m{}\033[m e depois dele vem \033[4m{}\033[m.'.format(num-1,num+1))
