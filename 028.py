import random
numero = random.randint (0,5)
palpite = int(input('tente adivinhar um numero entre 0 e 5:'))

if palpite == numero:
    print('Parabensss você acertou')
else :
    print(f'Errou o numero era {numero}')