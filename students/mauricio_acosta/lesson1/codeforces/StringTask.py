#Implementation, strings
from sys import stdin

palabra=stdin.readline()
palabra=palabra.lower()
palabra = palabra.replace('a',"")
palabra = palabra.replace('e',"")
palabra = palabra.replace('i',"")
palabra = palabra.replace('o',"")
palabra = palabra.replace('u',"")
palabra = palabra.replace('y',"")

newpalabra=''

for i in range(len(palabra)-1):
    newpalabra=newpalabra+'.'+palabra[i]
print(newpalabra)
