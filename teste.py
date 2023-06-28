def cripto (palavra):
    mensagem = ""

    for i in palavra:
        mensagem = mensagem + chr ( ord(i) + 5)
    return mensagem

def descripto (mensagem):
    frase = ""
    
    for i in mensagem:
        frase = frase + chr ( ord(i) - 5)
    return frase

palavra = cripto("hello word!")

print(palavra)

print(descripto(palavra))