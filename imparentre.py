
#descobrir quantos numeros impares tem entre 
n1 = int(input('digite o numero de inicio: '))
n2 = int(input('digite ate qual numero: '))
par = 0
impar = 0

for i in range(n1, n2+1):
    if i % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'entre o {n1} e o {n2} \ntem {par} numeros pares\ntem {impar} numeros impares')

