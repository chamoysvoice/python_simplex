#!usr/bin/env python2
from time import sleep
print "Este programa sirve para\nresolver un sistema de N restricciones en la forma Z = ax + by"
print "Donde 'a' y 'b' son constantes numericos \ny 'x' y 'y' son variables naturales\n ambos deben ser valores positivos" 

a = raw_input("Cual es el valor de a? ->")
b = raw_input("Cual es el valor de b? ->")

print "La ecuacion que se busca maximizar es:"
print "Z = "+a+"x + "+b+"y"

z = [-float(a),-float(b)]

array = []

i = 0;
while True:
	print "\nQuieres agregar una restriccion?(si/no)"
	re = raw_input()
	if re.strip().lower() == "si":
		print "Este programa funciona con restricciones ax + by <= c"
		a = raw_input("Cual es el valor de a?->")
		if not a:
			a = 0
		b = raw_input("Cual es el valor de b?->")
		if not b:
			b = 0
		c = raw_input("Cual es el valor de c?->")
		array.append([float(a),float(b),float(c)])
		i += 1
	elif re.strip().lower() == "no":
		break
	else: 
		print "\nNo se registro tu respuesta adecuadamente"

full_array = []
j = 0
t_array = [z[0], z[1]]

for q in range(i + 1):
	t_array.append(0)
full_array.append(t_array)

for a in array:
	w = a[0]
	e = a[1]
	r = a[2]
	t = [w,e]
	for q in range(i):
		if q == j:
			t.append(1)
		else: 
			t.append(0)
	j += 1	
	t.append(r)
	full_array.append(t)

for a in full_array:
	print a
print

def get_pivot(matriz):
	i = 0
	m = 900000
	j = 0
	for a in matriz[0]:
		if a == min(matriz[0]):
			x = i
		i += 1
	for a in matriz:
		if(a[x] <= 0):
			j += 1
			continue
		if((a[len(a)-1] / a[x]) < m):
			m = a[len(a)-1] / a[x]
			y = j 
		j += 1
	return x , y

def resolver(matriz):
	y,x = get_pivot(matriz)
	pivot = matriz[x][y]
	i = 0
	temp_array = matriz
	for a in temp_array[x]:
		temp_array[x][i] /= float(pivot)
		i += 1
	i = 0
	j = 0
	for b in temp_array:
		j = 0
		if temp_array[i][y] == 1:
			i += 1
			continue
		else:
                        dumy = temp_array[i][y]
			for a in b:
                            temp_array[i][j] = temp_array[i][j] - dumy* temp_array[x][j]
                            j += 1
                        i += 1
	
	for b in temp_array:
		print b
	print "\n\n\n"
        return temp_array

while (min(full_array[0]) < 0):
	full_array = resolver(full_array)

