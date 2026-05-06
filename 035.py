#triangulo
a = float(input('Qual o primeiro lado: '))
b = float(input('Qual o segundo lado: '))
c = float(input('Qual o terceiro lado: '))

if a + b > c and b + c > a and c + b > a:
    print('da um triangulo')
else:
    print('não da um triangulo')