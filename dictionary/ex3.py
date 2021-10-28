def char(string):
    # will return the number of unique characters in a string
    characters = { # every character in the alphabet
    }
    string.lower()# transforming all the string in lower case
    i = 0 # will be a auxiliar counter to help me reading the string
    for charact in string:
        characters[charact] = 1
    return len(characters)

def main():
    text = str(input('Digite o texto desejado: '))
    print(char(text))
main()