def contaPalavras(string):
    lista = []
    dic = {}
    #how to count words in python?
    unstuffed_string = string.replace('!', "").replace(',', "").replace('?','')
    lista = unstuffed_string.split()
    for i in range(len(lista)):
        if lista[i].lower() in dic:
            dic[lista[i].lower()] = dic[lista[i].lower()]+1
        else:
            dic[lista[i].lower()] = 1
        
    return dic
















