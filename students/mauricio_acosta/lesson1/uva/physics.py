from sys import stdin

lectura = stdin.read().splitlines()

for leer in lectura:
    variables=leer.split()
    if -100<=int(variables[0])<=100 and 0<=int(variables[1])<=200:
        print(2*(int(variables[0])*int(variables[1])))
