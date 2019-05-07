#Implementation
from sys import stdin

n=stdin.readline().split()
p=stdin.readline().split()
aux=0
for i in p[:int(n[0])]:
    if int(i)>=int(p[int(n[1])-1]) and int(i)>0:
        aux=1+aux
print(aux)
