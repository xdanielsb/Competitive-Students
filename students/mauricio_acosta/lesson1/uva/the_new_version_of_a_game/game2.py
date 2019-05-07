# version del programa en python usando una funcion especializada para la validacion
from sys import stdin

def  match(w,t): # suponiendo len(w) == len(t)
    flag = True
    for i in range(len(w)):
        if w[i] == '?':
            continue
        elif w[i] != t[i]:
            flag = False
            break
    return flag

def logic(t,w):
    count = 0
    for i in range(len(t)-len(w)+1):
        a = t[i:i+len(w)]

        if match(w,a):
            count += 1
    return count

while True:
    t = stdin.readline() #al llamar a readline, se incluye el caracter '\n'
    w = stdin.readline()
    if not t or not w:
        break
    print(logic(t[:-1],w[:-1])) # se quita \n
