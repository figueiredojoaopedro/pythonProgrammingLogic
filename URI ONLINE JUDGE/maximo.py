e1 = int (input ("digite o numero: "))
e2 = int (input ("digite o numero: "))

def maximo(x, y):
    if x > y:
        return x
    else:
        return y
    
print (maximo(e1, e2))