from sys import stdin
def main():
    while True:
        a=int(input())
        if a==0:
            break
        centrox,centroy=[int(x) for x in stdin.readline().split()]
        for i in range(0,a):
            puntx,punty=[int(x) for x in stdin.readline().split()]
            if (puntx-centrox)>0 and (punty-centroy)>0:
                print("NE")
            elif (puntx-centrox)<0 and (punty-centroy)>0:
                print("NO")
            elif (puntx-centrox)<0 and (punty-centroy)<0:
                print("SO")
            elif (puntx-centrox)>0 and (punty-centroy)<0:
                print("SE")
            else:
                print("divisa")
if __name__ == '__main__':
    main()
