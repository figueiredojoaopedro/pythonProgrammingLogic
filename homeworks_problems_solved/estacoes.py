dia = int(input ("Digite o dia desejado: "))
mes = input ("Digite o mês desejado: ")

if mes == "dezembro" and dia >= 21 or mes == "janeiro" or mes == "fevereiro" or mes == "março" and dia < 20:
    print("Verão")
elif mes == "março" and dia >= 20 or mes == "abril" or mes == "maio" or mes == "junho" and dia < 21:
    print("Outono")
elif mes == "junho" and dia >= 21 or mes == "julho" or mes == "agosto" or mes == "setembro" and dia < 22:
    print("Inverno")
elif mes == "setembro" and dia >= 22 or mes == "outubro" or mes == "novembro" or mes == "dezembro" and dia < 21:
    print("Primavera")