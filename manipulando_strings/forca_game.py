def main():
    lenght = ''
    forca = """X==:==
X  :
X
X
X
X
===========
"""
    secret_word = input('Digite a palavra secreta:')
    #for each characther we got in the word, will be replaced by a -2
    for i in range(len(secret_word)):
        lenght = str(lenght) + '-'
    print('\n\n\n\n\n\n\n\n\n\n%s\n'%lenght)
    entrada = str(input('Digite uma letra:'))
    for j in range(len(secret_word)):
        if entrada == secret_word[j]:
            print(forca)        
            lenght[j] = secret_word[j]
            print('%s\n'%lenght)
        else:
            print('Você errou!')
main()