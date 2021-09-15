
def test_prime(n):
    mult = 0
    for count in range (2, n):
        if n % count == 0:
            mult += 1
            return False

    if mult == 0:
        return True
