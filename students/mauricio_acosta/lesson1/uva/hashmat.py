from sys import stdin

lectura = stdin.read().splitlines()

for leer in lectura:
    soldados=leer.split()
    if int(soldados[1])>int(soldados[0]):
        print(int(soldados[1])-int(soldados[0]))
    else:
        print(int(soldados[0])-int(soldados[1]))
