import io
lista = []
coded = []
decoded = []
uncoded = []
concate = ""
concate2 = ""
def readFile():
    f = io.open("text.txt",mode="r", encoding="utf-8")
    if f.mode == 'r':
        contents = f.read()
        for j in contents:
            lista.append(j)
        print("indo para code")
        code()


























        
        
def code():
    for i in lista:
        if i == 'a' or i == 'A':
            coded.append('25')
        elif i == 'b' or i == 'B':
            coded.append('24')
        elif i == 'c' or i == 'C':
            coded.append('23')
        elif i == 'd' or i == 'D':
            coded.append('22')
        elif i == 'e' or i == 'E':
            coded.append('21')
        elif i == 'f' or i == 'F':
            coded.append('20')
        elif i == 'g' or i == 'G':
            coded.append('19')
        elif i == 'h' or i == 'H':
            coded.append('18')
        elif i == 'i' or i == 'I':
            coded.append('17')
        elif i == 'j' or i == 'J':
            coded.append('16')
        elif i == 'k' or i == 'K':
            coded.append('15')
        elif i == 'l' or i == 'L':
            coded.append('14')
        elif i == 'm' or i == 'M':
            coded.append('13')
        elif i == 'n' or i == 'N':
            coded.append('12')
        elif i == 'o' or i == 'O':
            coded.append('11')
        elif i == 'p' or i == 'P':
            coded.append('10')
        elif i == 'q' or i == 'Q':
            coded.append('09')
        elif i == 'r' or i == 'R':
            coded.append('08')
        elif i == 's' or i == 'S':
            coded.append('07')
        elif i == 't' or i == 'T':
            coded.append('06')
        elif i == 'u' or i == 'U':
            coded.append('05')
        elif i == 'v' or i == 'V':
            coded.append('04')
        elif i == 'x' or i == 'X':
            coded.append('03')
        elif i == 'w' or i == 'W':
            coded.append('02')
        elif i == 'y' or i == 'Y':
            coded.append('01')
        elif i == 'z' or i == 'Z':
            coded.append('00')
        elif i == ' ':
            coded.append('66')
        elif i == 'é' or i == 'É':
            coded.append('67')
        elif i == 'ã' or i == 'Ã':
            coded.append('68')
        elif i == 'á' or i == 'Á':
            coded.append('69')
        elif i == 'à' or i == 'À':
            coded.append('70')
        elif i == 'õ' or i == 'Õ':
            coded.append('71')
        elif i == 'è' or i == 'È':
            coded.append('72')
        elif i == 'ì' or i == 'Í':
            coded.append('73')
        elif i == 'ú' or i == 'Ú':
            coded.append('74')
        elif i == 'ì' or i == 'Ì':
            coded.append('75')
        elif i == 'ò' or i == 'Ò':
            coded.append('76')
        elif i == 'ù' or i == 'Ù':
            coded.append('77')
        elif i == '.':
            coded.append('78')
        elif i == ',':
            coded.append('79')
        elif i == ':':
        # provavelmente a partir desta parte pode haver erro na criptografia 
            coded.append('80')
        elif i == '\ ':
            coded.append('81')
        elif i == '/':
            coded.append('82')
        elif i == '?':
            coded.append('83')
        elif i == ' " ':
            coded.append('85')
        elif i == '&':
            coded.append('86')
        elif i == '*':
            coded.append('87')
        elif i == '$':
            coded.append('88')
        elif i == 'ç' or i == 'Ç':
            coded.append('89')
        #else:
         #   coded.append(i)

def decode():
    i = 0
    pos = len(concate)/2
    while i <= pos:
        decoded.append(concate[i] + concate[i+1])
        i += 2
    for j in decoded:
        if j == '66':
            uncoded.append(' ')
        elif j == '\ ' and j[j+1] == 'n':
            uncoded.append('\n')
        elif j == '00':
            uncoded.append('z')
        elif j == '01':
            uncoded.append('y')
        elif j == '02':
            uncoded.append('w')
        elif j == '03':
            uncoded.append('x')
        elif j == '04':
            uncoded.append('v')
        elif j == '05':
            uncoded.append('u')
        elif j == '06':
            uncoded.append('t')
        elif j == '07':
            uncoded.append('s')
        elif j == '08':
            uncoded.append('r')
        elif j == '09':
            uncoded.append('q')
        elif j == '10':
            uncoded.append('p')
        elif j == '11':
            uncoded.append('o')
        elif j == '12':
            uncoded.append('n')
        elif j == '13':
            uncoded.append('m')
        elif j == '14':
            uncoded.append('l')
        elif j == '15':
            uncoded.append('k')
        elif j == '16':
            uncoded.append('j')
        elif j == '17':
            uncoded.append('i')
        elif j == '18':
            uncoded.append('h')
        elif j == '19':
            uncoded.append('g')
        elif j == '20':
            uncoded.append('f')
        elif j == '21':
            uncoded.append('e')
        elif j == '22':
            uncoded.append('d')
        elif j == '23':
            uncoded.append('c')
        elif j == '24':
            uncoded.append('b')
        elif j == '25':
            uncoded.append('a')
        elif j == '67':
            uncoded.append('é')
        elif j == '68':
            uncoded.append('ã')
        elif j == '69':
            uncoded.append('á')
        elif j == '70':
            uncoded.append('à')
        elif j == '71':
            uncoded.append('õ')
        elif j == '72':
            uncoded.append('è')
        elif j == '73':
            uncoded.append('í')
        elif j == '74':
            uncoded.append('ú')
        elif j == '75':
            uncoded.append('ì')
        elif j == '76':
            uncoded.append('ò')
        elif j == '77':
            uncoded.append('ù')
        elif j == '78':
            uncoded.append('.')
        elif j == '79':
            uncoded.append(',')
        elif j == '80':
            uncoded.append(':')
        elif j == '81':
            uncoded.append('\ ')
        elif j == '82':
            uncoded.append('/')
        elif j == '83':
            uncoded.append('?')
        elif j == '84' or j == '85':
            uncoded.append('" ')
        elif j == '89':
            uncoded.append('ç')
        #else:
         #   uncoded.append(j)

























         


readFile()
print("criando string")
for u in coded:
    concate += u
print("indo para decode")
print(concate)
print("indo para decode")
decode()
print(uncoded)
for k in uncoded:
        concate2 += k
print(concate2)
p = open("textoProf.txt","w+")
for h in concate:
    p.write(h)
p.close
