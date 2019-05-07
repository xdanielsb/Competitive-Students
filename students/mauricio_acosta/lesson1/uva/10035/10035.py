from sys import stdin

def logic(number1,number2,lennum1,lennum2):
    num1=str(number1)
    num2=str(number2)
    aux=-1
    carry=0
    carries=0
    if lennum1>lennum2:
        for i in range(len(str(number1))-1):
            if len(num2)==len(num1):
                continue
            num2='0'+num2
    if lennum1<lennum2:
        for i in range(len(str(number2))-1):
            if len(num1)==len(num2):
                continue
            num1='0'+num1
    for i in num1:
        if int(num1[aux])+int(num2[aux])+carry>9:
            carry = 1
            carries+=1
        else:
            carry=0
        aux=aux-1
    return carries

while True:
    a,b=[int(c) for c in input().split()]
    if a==0 and b==0:
        break
    carry=logic(a,b,len(str(a)),len(str(b)))
    if carry==0:
        print("No carry operation.")
    elif carry==1:
        print("{} carry operation.".format(carry))
    else:
        print("{} carry operations.".format(carry))
