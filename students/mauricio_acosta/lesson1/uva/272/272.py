from sys import stdin
bandera=False
inicio="``"
fin="\'\'"

for lectura in stdin:
    lectura=list(lectura)
    for i in range(len(lectura)):
        if lectura[i]=="\"" and bandera==False:
            lectura[i]=inicio
            bandera=True
        elif lectura[i]=="\"" and bandera==True:
            lectura[i]=fin
            bandera=False
    print("".join(lectura),end="")
