from sys import stdin

case=int(stdin.readline())
oddInteger=[]
for i in range(case):
    a=int(stdin.readline())
    b=int(stdin.readline())
    for j in range(a,b+1):
        if j%2==0:
            continue
        else:
            oddInteger.append(j)

    print("Case {}: {}".format(i+1,sum(oddInteger)))
    oddInteger=[]
