#atleta nivel
ano = int(input("Qual a data de nascimento: "))
ano_agr = int(input("ano atual: "))

idade = ano_agr - ano

if idade <= 9:
    print("classificação mirim")
elif idade <= 14:
    print("Classificação infantil")
elif idade <= 19:
    print("Classificação junior")
elif idade <= 20:
    print("Classificação sênior")
else:
    print("Master")