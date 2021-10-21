from array import *
#create_array
n=int(input ('input_n:'))
m=int(input('input_m:'))
g=(0)
p=(0)
q=(0)
k=(0)
z=2
list_1=[]
list_2=[0]
list_3=[]
while g<n:
	g=g+1
	p=p+1
	list_1.append(p)
#create_m
while z>1:
	z=z+1
	if int(list_1[1])==int(list_2[-1]):
		break
	elif int(list_1[1])!=int(list_2[-1]):
		for i in list_1:
			if k<m:
				k=k+1
				list_2.append(i)
				print(list_3)
			elif k==m:
				k=2
				list_2.append(list_2[-1])
				list_3.append(list_2[-1])
				list_2.append(i)
				print(list_3)
			elif list_1[1]==list_2[-1]:
				break
print(list_3)


