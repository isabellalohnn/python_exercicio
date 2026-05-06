salario =float(input('Qual o seu salario: '))
soma = salario * 1.15
soma1 = salario * 1.10

if salario <= 1250:
    print(f'com o aumento fica: {soma:.2f} ')
else:
    print(f'com o aumento fica {soma1:.2f}')