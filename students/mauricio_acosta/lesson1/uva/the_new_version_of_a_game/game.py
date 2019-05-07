# version del programa en python usando expresiones regulares para la validacion
import re
from sys import stdin

def logic(t,w):
    count = 0
    for i in range(len(t)-len(w)+1):
        a = t[i:i+len(w)]

        if re.match(w,a):
            count += 1
    return count

while True:
    t = stdin.readline() #al llamar a readline, se incluye el caracter '\n'
    w = stdin.readline()
    if not t or not w:
        break
    w = str.replace(w,"?",".")
    print(logic(t[:-1],w[:-1])) # se quita \n
