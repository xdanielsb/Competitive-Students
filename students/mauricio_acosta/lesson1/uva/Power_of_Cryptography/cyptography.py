from sys import stdin
import math
def calcula(n,p):
    return math.pow(p,1/n)
lectura=stdin.read().splitlines()
while(lectura!= []):
    n = lectura.pop(0)
    p = lectura.pop(0)
    print(round(calcula(int(n),int(p))))
