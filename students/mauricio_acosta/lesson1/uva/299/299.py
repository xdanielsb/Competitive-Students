from sys import stdin

def ordenar(lista):
    cont=0
    for i in range(len(lista)):
        anterior = i
        for k in range(i, len(lista)):
            if lista[k] < lista[anterior]:
                anterior = k
                cont=1+cont
            intercambio(lista, anterior, i)
    return cont

def intercambio(lista, anterior, i):
    temp = lista[anterior]
    lista[anterior] = lista[i]
    lista[i] = temp

def main():
    case=int(stdin.readline())
    for i in range(case):
        numtrain=int(stdin.readline())
        train=[int(c) for c in stdin.readline().split()[:numtrain]]
        cont=ordenar(train)
        print("Optimal train swapping takes {} swaps.".format(cont))

if __name__ == '__main__':
    main()
