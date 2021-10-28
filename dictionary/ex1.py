def procuraReversa(dicionario, valor):
    chaves = []
    for chave, value in dicionario.items():
        if value == valor:
            chaves.append(chave)
    print(chaves)


def main():
    dicionario = {
    'um':'ola',
    'dois':'ola',
    'tres':'ahhh'
    }
    procuraReversa(dicionario,'ola')

main()