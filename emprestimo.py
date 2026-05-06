#emprestimo

casa = float(input("Qual o valor da casa: "))
salario = float(input("Qual o seu salário mensal: "))
ano = float(input("Quantos anos pretende pagar: "))

meses = ano * 12
prestacao = casa / meses
limite = salario * 0.30

print(f"Prestação mensal de {prestacao:.2f}")

if prestacao <= limite:
    print("Aprovado!")
else:
    print("Negado")