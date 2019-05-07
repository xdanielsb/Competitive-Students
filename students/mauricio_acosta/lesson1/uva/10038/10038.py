from sys import stdin

def logica(lista,n):
    p=-1
    a = dict()
    for i in range(0,n-1):
        num1=abs(lista[i]-lista[i+1])
        if not (num1>=1 and num1<n) or a.get(num1):
            return False
        a[num1] = True
        p = num1
    return True

def main():
    while True:
        caracteres=stdin.readline().split()

        caracteres = [int(x) for x in caracteres]
        if not caracteres:
            break
        valor=logica(caracteres[1:],caracteres[0])
        if valor==True:
            print("Jolly")
        elif valor==False:
            print("Not jolly")

if __name__ == '__main__':
    main()
