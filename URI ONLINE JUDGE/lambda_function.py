#ex1

maximo = lambda x, y: x if x>y else y

print(maximo(10,9))
print(maximo(10,20))

#ex2

multiplo = lambda x, y: True if x % y == 0 else False

print(multiplo(4,2))
print(multiplo(5,2))

#ex3
area_triangulo = lambda b, h: (b*h)/2

print(area_triangulo(5, 4))