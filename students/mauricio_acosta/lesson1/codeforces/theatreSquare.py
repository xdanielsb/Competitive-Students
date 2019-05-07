#Math
from sys import stdin
n,m,a=stdin.readline().split()
n=int(n)
m=int(m)
a=int(a)

aux1 = m//a
if m%a != 0:
    aux1+=1
aux2 = n//a
if n%a != 0:
    aux2+=1
print(aux1*aux2)
