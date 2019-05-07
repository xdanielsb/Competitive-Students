from sys import stdin
lista=[0]*1000001

def calcular(n):
    p = 0
    inicial = n
    count=1
    if lista[inicial]:
        return lista[inicial]
    while n!=1:
        count+=1
        if n%2!=0:
            p=3*n+1
            n=p
        else:
            p=n//2
            n = p
    lista[inicial] = count
    return count

while True:
    numero=stdin.readline().split()
    if not numero:
        break
    i,j = [ int(x) for x in numero]
    ti,tj = i,j
    if i>j:
        i,j = j,i
    max_ciclo=0
    while i < j+1:
        pmax = calcular(i)
        if pmax>max_ciclo:
            max_ciclo=pmax
        i+=1
    print(ti,tj,max_ciclo)
