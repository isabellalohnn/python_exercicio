mes = int(input('informe o numero do mês: '))
dia = int(input('informe a data: '))
#ano == 365
#mes == 12
#dianmes == 30
##
qtdDiasMes = 30

diasPassados = ((mes*qtdDiasMes)+dia)-qtdDiasMes

print(f"Já se passaram {diasPassados} dias no ano.")