n1 = int(input("digite: "))
n2 = int(input("digite: "))

def maximo (x,y):
    if x % y == 0:
        return True
    else:
        return False

print (maximo (n1, n2))