#data é magica quando o dia é considerado quando o dia multiplicado pelo mes = ano
#para acessar os dois ultimos numeros da variavel, basta usar %100, já que estamos falando de mil
d = int(input("dia: "))
m = int(input("mes: "))
a = int(input("ano: "))

def dataMagica (dia, mes, ano):
    if dia*mes == ano%100:
        print("data magica")
    else:
        print("não é data mágica")

dataMagica(d, m, a)