from sys import stdin

lines = int(stdin.readline())

while (lines>0):
    num, divi=stdin.readline().split()
    num=int(num)
    divi=int(divi)
    count=0
    while num>0:
        if (num % divi) == 0:
            num=num//divi
            count+=1
        else:
            count+=(num % divi)
            num = num-(num % divi)
    print(int(count))
    lines-=1
