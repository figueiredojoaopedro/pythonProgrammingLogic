def converte(codigo_morse, string):
    lista = []
    string_morse = []
    resultado = str()
    for i in range(len(string)):
        lista.append(string[i].upper())
    for j in range(len(lista)):
        for key, value in codigo_morse.items():
            if lista[j] == key:
                string_morse.append(value)
            else:
                pass
    return ' '.join(string_morse)

codigo_morse = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.'}
mensagem = input('Digite alguma coisa: ')
print(converte(codigo_morse,mensagem))