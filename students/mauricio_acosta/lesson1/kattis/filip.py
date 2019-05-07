from sys import stdin
a,b=stdin.readline().split()
numa=int(a[2]+a[1]+a[0])
numb=int(b[2]+b[1]+b[0])
if numa>numb:
    print(numa)
else:
    print(numb)