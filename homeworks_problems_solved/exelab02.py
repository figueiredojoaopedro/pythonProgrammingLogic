"""
Uma loja dá desconto de 10% para compras à vista, 
5% para compras em 2 ou 3 parcelas e não dá desconto para compras acima de 3 parcelas. 
Além disso, a loja dá mais 5% de desconto (você pode somar essa porcentagem ao outro possível desconto) 
aos clientes que comprarem um total superior a R$5.000,00.
Faça um programa para ler o valor da compra e o número de parcelas, calcular e mostrar o valor do desconto,
o valor final da compra com desconto e o valor de cada parcela. Utilize duas casas decimais.
"""

valor_da_compra = float(input("Digite o valor da compra: "))
parcelas = int (input ("Digite a quantidade de parcelas: "))

if parcelas == 1: 
    desconto = valor_da_compra*0.1
if parcelas == 2:
    desconto = valor_da_compra*0.05
if parcelas == 3:
    desconto = valor_da_compra*0.05
if parcelas > 3:
    desconto = 0
if valor_da_compra > 5000:
    desconto = valor_da_compra*0.05 + desconto

valor_final = valor_da_compra - desconto
quantidade_parcelas = valor_final / parcelas

print("Desconto total: %.2f" % desconto)
print("Valor final da compra com desconto: %.2f" % valor_final)
print("Cada parcela será de: %.2f" % quantidade_parcelas)


    
