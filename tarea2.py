# Tarea 2
# C - Look Simulation
beginning = 0
end = 100

text = raw_input("ingrese lista de peticiones")
current = input("ingrese la posicion inicial del cabezal")

petitions = text.split("-")
petitions.sort()
print petitions
order = []
times = []
total_time = 0

# OJO: ------ Se maneja la lista petitions como strings de numeros y no ints

while(petitions):
	# Primero se encuentra el mas cercano
	min_distance = 100
	min_cilinder = 0
	for cilinder in petitions:
		# Solo se cuentan cilindros mayores, pues estamos en orden creciente
		num_cilinder = int(cilinder)
		if num_cilinder < current:
			break;
		distance = num_cilinder - current
		if distance < min_distance:
			min_distance = distance
			min_cilinder = cilinder

	# Luego este se guarda junto con toda la informacion
	current = min_cilinder
	order.append(current)
	times.append(min_distance)
	total_time += min_distance

	petitions.remove(current)

	# Si se llego al ultimo cilindro volver al inicio
	if current > max(petitions):
		distance = current - int(petitions[0])

		# Si esta ordenado el primero de la lista es el cilindro inicial
		current = petitions[0]
		order.append(current)
		times.append(distance)
		total_time += distance

		petitions.remove(current)

	
		

	

# Hemos terminado de generar los outputs, ahora queda imprimirlos
print "Orden"
print order
print "Tiempos"
print times
print "Total"
print total_time