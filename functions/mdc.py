###########################################
'''
O Máximo Divisor Comum (MDC) de dois números inteiros positivos, n e m, é o maior número,
d, que divide de forma inteira n e m. Existem vários algoritmos que podem ser usados 
para resolver esse problema, incluindo: Utilize o pseudocódigo acima para fazer um
programa em Python que leia dois números inteiros positivos do usuário, determina
e reporta o maior divisor comum entre eles.
'''
###########################################

#entrada dos valores e d = 0
n = int(input("Digite n: "))
m = int(input("Digite m: "))

#uma cadeia de repetição sera feita agora para verificar se o d é um divisor de m e n ao mesmo tempo
mdc = n

while n % mdc != 0 or m % mdc != 0: 
    mdc = mdc - 1

print(mdc)