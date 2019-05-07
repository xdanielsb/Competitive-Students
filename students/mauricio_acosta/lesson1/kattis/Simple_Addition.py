from sys import stdin

carry=0
result=[0]
a=stdin.readline().rstrip('\n')
b=stdin.readline().rstrip('\n')

if int(a)>int(b):
    for _ in range(len(a)-len(b)):
        b='0'+b
elif int(b)>int(a):
    for _ in range(len(b)-len(a)):
        a='0'+a

for i in range(1,len(a)+1):
    aux=int(a[-i])+int(b[-i])+carry
    #print("carriado",carry)
    #print("num1: ",a[-i])
    #print("num2: ",b[-i])
    #print("aux: ",aux)

    if aux>9:
        #print("entra carry")
        aux2=str(aux)
        carry=int(aux2[0])
        result.insert(1,aux2[-1])
        #print("carry:",carry)
        #print("resultOne:",result)
    else:
        carry=0
        result.insert(1,aux)
result=[str(x) for x in result]
if carry==1:
    result[0]=str(carry)
    aux3=int("".join(result))

    print(aux3)
else:
    aux3=int("".join(result[1:]))
    print(aux3)
