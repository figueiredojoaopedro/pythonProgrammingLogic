##########################
'''
Um funcionário de uma empresa recebe aumento salarial anualmente. Sabe-se que: 

a) Esse funcionário foi contratado em 2005, com salário inicial de R$ 5.000,00; 

b) Em 2006 ele recebeu aumento de 1,5% sobre o salário inicial; 

c) A partir de 2007 (inclusive), os aumentos salariais sempre corresponderam ao dobro do percentual do ano anterior. 

Faça um programa que recebe um ano (ano > 2007) e determina o salário atual do funcionário.

Digite o ano desejado: 2012
Salário de 2012: R$ 22322.18

salario em 2007 = 5227,25
'''

ano = int(input("Digite o ano desejado: "))

if ano < 2007:
    print("Por favor digite um ano maior que 2007")
else:
    salario = (5000*1.015)*1.030
    aumento = 0.03
    z = ano - 2007
    while z > 0:
        aumento *= 2
        salario *= (aumento+1)
        z -= 1 

print ("Salário de %d: R$ %.2f" % (ano, salario))