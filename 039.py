ano = int(input("Que ano você nasceu: "))
ano_agr = int(input("Em que ano estamos: "))

idade = ano_agr - ano
tempo_passou = idade - 18
tempo_falta = 18 - idade

if idade < 18:
    print(f"ainda vai se alistar daqui {tempo_falta} anos ")
elif idade == 18:
    print("È hora de se alistar")
else:
    print(f"Já passou do tempo, sua data de alistamento foi a {tempo_passou} ano")

