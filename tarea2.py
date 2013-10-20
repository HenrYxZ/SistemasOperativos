# Tarea 2
# C - Look Simulation
beginning = 0
end = 100

text = raw_input("ingrese lista de peticiones	")
current = input("ingrese la posicion inicial del cabezal	")
print current

petitions = text.split("-")

for i in range(len(petitions)):
	petitions[i] = int(petitions[i])

petitions.sort()
order = []
times = []
total_time = 0

# OJO: ------ Se maneja la lista petitions como strings de numeros y no ints

while(petitions):

	# Primero se encuentra el mas cercano
	min_distance = 100
	min_cilinder = petitions[0]
	distance = 100
	print petitions

	for cilinder in petitions:
		# Solo se cuentan cilindros mayores, pues estamos en orden creciente
		print "hello"
		# print str(num_cilinder) + "num_cilinder"
		# print str(current) + "current"
		# ************ PROBLEMAAAAAAAAAAAAAAAAA ********************
		if cilinder > current:
			print "mayor"
			distance = cilinder - current
			print distance
			if distance < min_distance:
				min_distance = distance
				min_cilinder = cilinder

	# Luego este se guarda junto con toda la informacion
	current = min_cilinder
	order.append(current)
	times.append(min_distance)
	total_time += min_distance

	print current
	petitions.remove(current)

	# Si se llego al ultimo cilindro volver al inicio
	if (len(petitions)!= 0) and (current > max(petitions)):
		distance = current - int(petitions[0])

		# Si esta ordenado el primero de la lista es el cilindro inicial
		current = int(petitions[0])
		order.append(current)
		times.append(distance)
		total_time += distance

		petitions.remove(current)
		print str(current) + " from C"

	
		

	

# Hemos terminado de generar los outputs, ahora queda imprimirlos
print "Orden"
print order
print "Tiempos"
print times
print "Total"
print total_time