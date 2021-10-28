def anagramChecker(text1, text2):
    # we got to create a new dictionary that store the letters in a string and then check if its equal to other string
    checker1 = {#characters from text 1 will be stored here
    }
    checker2 = {
    }
    # trying to explain how its solved
    # basically, we gonna store how many letters there are in the dictionary
    for f in text1:
        if f not in checker1:
            checker1[f] = 1
        else:
            checker1[f] += 1
    for c in text2:
        if c not in checker2:
            checker2[c] = 1
        else:
            checker2[c] += 1
    
    # print(checker2,checker1) if you want to see how the dictionary is
    if checker1 == checker2:
        print('São anagramas')
    else:
        print('Não são anagramas')
    
def main():
    t1 = str(input('Digite a primeira palavra: '))
    t2 = str(input('Digite a segunda palavra: '))

    anagramChecker(t1,t2)
main()