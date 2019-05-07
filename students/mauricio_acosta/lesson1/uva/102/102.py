from sys import stdin

def logic(bottles):
	dic1={}
	dic2={}
	dic3={}
	l1=bottles[0:3]
	l2=bottles[3:6]
	l3=bottles[6:9]
	valor1 = max(l1)
	print (valor1)
	valor2 = max(l2)
	print (valor2)
	valor3 = max(l3)
	print (valor3)
	total=int(valor1)+int(valor2)+int(valor3)
	return total



def main():

	while True:
		bottles=stdin.readline().split()
		if not bottles:
			break
		print(logic(bottles))


if __name__ == '__main__':
	main()
