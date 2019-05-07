from sys import stdin
import math

lprimos = [2,3,5,7,11,13,17,19,23,29,31]

def primos(n): #n esimo numerp primos
    if len(lprimos) > n:
        return lprimos[n]
    else:

        pnp = lprimos[-1] # Presunto Numero Primo
        flag = False
        while not flag:
            pnp += 2
            flag = True
            for primo in lprimos:
                if pnp % primo == 0:
                    flag = False
                    break
        lprimos.append(pnp)
        return pnp




def descomponer(num):
    factores = []
    i = 0
    while i<len(lprimos):
        primo = primos(i)
        res = num % primo
        #print("num:{}, primo:{}, res:{}".format(num,primo,res))
        if res == 0 :
            num = num // primo
            factores.append(primo)
        elif res > num // primo:
            break
        else:
            i+=1
    if num != 1:
        factores.append(num)
    return factores


def mcd(a,b):
    if a == 0 or b == 0:
        return 1
    mul = 1
    i = 0
    while i<len(lprimos): # puede ser que no halla suficientes numeros primos en lprimos ?
        p = primos(i)
        (r1,r2) = (a%p,b%p)
        if r1 == 0 and r2 == 0:
            (a,b) = (a//p,b//p)
            mul*= p
        elif r1 > a // p or r2 > b // p:
            break
        else:
            i+=1
    return mul

#while True:
lectura= stdin.read().splitlines()
#(a,b) = map(int, input().split())
for leer in lectura:
    (a,b)=map(int,leer.split())
    if a == 0 and b == 0:
        break

    la = descomponer(a)
    lb = descomponer(b)

    if len(lb) != 0:
        k = mcd(len(la),len(lb))
        N = round(math.pow(b,1/k))
    else:
        k = round(math.log(a)/math.log(2))
        N = 1
    #print("k:{},N:{}".format(k,N))
    if N == 1:
        print(k,2*a-b)
    else:
        print(round((1-b)/(1-N)),N*(a-b)+a)
