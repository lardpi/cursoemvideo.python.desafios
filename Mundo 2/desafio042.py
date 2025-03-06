print('--- triform 1.0 ---\n\n')
a = int(input('Digite o valor do lado A: '))
b = int(input('Digite o valor do lado B: '))
c = int(input('Digite o valor do lado C: '))
if abs(b-c)<a and abs(b-c)<(b+c):
    if abs(a-c)<b and abs(a-c)<(a+c):
        if abs(a-b)<c and abs(a-b)<(a+b):
            print('Com esses lados É POSSÍVEL formar um triângulo.')
            if a == b and b == c:
                print('E este triângulo será EQUILÁTERO.')
            elif a == b or a == c or b == c:
                print('E este triângulo será ISÓSCELES.')
            else:
                print('E este triângulo será ESCALENO.')
        else:
            print('Com esses lados É IMPOSSÍVEL formar um triângulo.')
    else:
        print('Com esses lados É IMPOSSÍVEL formar um triângulo.')
else:
    print('Com esses lados É IMPOSSÍVEL formar um triângulo.')
