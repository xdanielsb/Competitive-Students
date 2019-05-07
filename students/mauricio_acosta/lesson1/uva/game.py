import re,string
from sys import stdin
def logic(t,w):
    count = 0
    for i in range(len(t)-len(w)+1):
        if re.match(w,t[i:i+len(w)]):
            count += 1
    return count

lista= stdin.read().splitlines()
while(lista != []):
    t = lista.pop(0)
    w = lista.pop(0)
    print(logic(t,string.replace(w,"?",".")))
