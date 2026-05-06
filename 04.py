altura = float(input('qual a sua altura em cm: '))
peso = float(input('qual o seu peso: '))

imc = peso / (altura**2)

if imc < 18.5:
    classificacao = 'abaixo do peso'
elif 18.5 <= imc < 24.9:
    classificacao = 'peso normal'
elif 25 <= imc < 29.9:
    classificacao = 'sobrepeso'
elif 30 <= imc < 34.9:
    classificacao = 'obesidade 1'
elif 35 <= imc < 39.9:
    classificacao = 'obesidade 2'  
else imc > 40:
    classificacao = 'obesidade 3 '  

print(f'sua classificação {classificacao}')