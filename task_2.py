#formuls:
#(x_po- x_ci)**2+(y_po-y_ci)**2 <r**2 in a cirle
#(x_po- x_ci)**2+(y_po-y_ci)**2 =r**2 on the cirle
#(x_po- x_ci)**2+(y_po-y_ci)**2 >r**2 outside the cirle
import math
#values:
f_ci=open("C:\\файл1.txt", 'rt')
x_ci= int(f_ci.read(1))
y_ci=2
r_ci=3

x_po = 1
y_po = 1
#steam
if (x_po- x_ci)**2+(y_po-y_ci)**2 <(r_ci**2):
	print("in a cirle")
elif (x_po- x_ci)**2+(y_po-y_ci)**2 ==(r_ci**2):
	print("on the cirle")
elif (x_po- x_ci)**2+(y_po-y_ci)**2 >(r_ci**2):
	print("outside the cirle")