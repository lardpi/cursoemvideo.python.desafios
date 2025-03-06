#DESAFIO 046
import time
for c in range (10,0,-1):
    d = 10
    d -= c
    print(' '*d,'#'*c,' {} '.format(c),'#'*c,' '*d)
    time.sleep(1)
print('             #')
print('    #               #')
print(' #                     #')
print('#           FIM         #')
print(' #                     #')
print('    #               #')
print('             #')
