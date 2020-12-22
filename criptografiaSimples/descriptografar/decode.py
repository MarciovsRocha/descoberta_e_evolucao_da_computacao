import io
lista[]
coded = []
uncoded = []
concate = ""
concate2 = ""

def readFile():
    f = io.open("textEduardo.txt", mode="", encoding="utf-8")
    if f.mode == 'r':
        contents = f.read()
        for j in contents:
            lista.append(j)
        decode()

def decode():
    for i in lista:
        if i == 'S':
            uncoded.append("e")
        elif i == 'l':
            uncoded.append("j")
        elif i == 'q':
            uncoded.append("o")
        elif i == 'v'
            uncoded.append("h")
