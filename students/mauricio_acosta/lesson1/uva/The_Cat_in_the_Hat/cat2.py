from sys import stdin
def logic(a,b):
    (N,k) = (2,0)
    if b == 1:
        N = 1
    while True:
        if a == 0 or b == 0:
            break
        (cos1,res1) = divmod(a,N+1)
        (cos2,res2) = divmod(b,N)
        if res1 == 0 and res2 == 0:
            k += 1
            (a, b) = (cos1, cos2)
        elif res1 > cos1 or res2 > cos2:
            break
        else:
            N += 1
    return (N,k)
lectura=stdin.read().splitlines()
for leer in lectura:
    (a,b) = map(int, leer.split())
    if a == 0 and b == 0:
        break
    (N,k) = logic(a,b)
    if N == 1:
        print(k,2*a-b)
    else:
        print(round((b-1)/(N-1)),N*(a-b)+a)
