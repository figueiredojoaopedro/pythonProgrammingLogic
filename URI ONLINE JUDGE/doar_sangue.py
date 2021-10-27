Sexo = input("digite: ")
Peso = int(input ("Digite o peso: "))

def allow_donate (sexo, peso):
    if ((sexo == "masculino" or sexo == "Masculino") and peso >= 60) or ((sexo == "feminino" or sexo == "Feminino") and peso >= 50):
        print("Pode doar sangue")
    else:
        print("Não pode doar sangue ")

allow_donate(Sexo, Peso)