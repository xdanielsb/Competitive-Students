from sys import stdin

cadena = stdin.read().splitlines()


for linea in cadena:
    contador = 0
    cadenaplit = linea.split()

    string = str()


    for letra in linea:

        if letra.isalpha():
            string += letra

        else:
            string += " "


    for cualquier in string.split():

        contador += 1

    print(contador)
