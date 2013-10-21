# Tarea 2
# C - Look Simulation
# list 3-45-32-67-94-73

def getMin(petitions, current, orderer):

	if orderer == 1:
		return getMinClook(petitions, current)
	elif orderer == 2:
		return getMinSSTF(petitions, current)
	else:
		return getMinScan(petitions, current)

def getMinClook(petitions, current):

	min_distance = end
	for cilinder in petitions:
		# Solo se cuentan cilindros mayores, pues estamos en orden creciente
		print "hello"
		# print str(num_cilinder) + "num_cilinder"
		# print str(current) + "current"
		if cilinder > current:
			print "mayor"
			distance = cilinder - current
			print "distance: " + str(distance)
			if distance < min_distance:
				min_distance = distance
				min_cilinder = cilinder

	return [min_cilinder, min_distance]

def getMinSSTF(petitions, current):

	min_distance = end
	for cilinder in petitions:
		# Solo se cuentan cilindros mayores, pues estamos en orden creciente
		print "hello"
		# print str(num_cilinder) + "num_cilinder"
		# print str(current) + "current"
		distance = abs(cilinder - current)
		print "distance: " + str(distance)
		if distance < min_distance:
			min_distance = distance
			min_cilinder = cilinder

	return [min_cilinder, min_distance]

def getMinScan(petitions, current):

	min_distance = end
	for cilinder in petitions:
		# Solo se cuentan cilindros mayores, pues estamos en orden creciente
		print "hello"
		# print str(num_cilinder) + "num_cilinder"
		# print str(current) + "current"
		if direction == -1:
			# Si vamos en orden descendente damos vuelta todo
			cilinder *= -1
			current *= -1

		if cilinder > current:
			print "mayor"
			distance = cilinder - current
			print "distance: " + str(distance)
			if distance < min_distance:
				min_distance = distance
				min_cilinder = cilinder

	if direction == -1:
		# Si vamos en orden descendente volvemos a lo anterior
		min_cilinder *= -1
		current *= -1

	return [min_cilinder, min_distance]

def checkBorder(petitions, current):

	# Si se llego al ultimo cilindro volver al inicio
	if current > max(petitions):
		return True
	else:
		return False

def comeBackClook(petitions, current):
	
	distance = current - petitions[0]
	# Si esta ordenado el primero de la lista es el cilindro inicial
	cilinder = petitions[0]
	return cilinder, distance

def comeBackScan(petitions, current):
	
	distance = end - current + end - max(petitions)
	# Si esta ordenado el primero de la lista es el cilindro inicial
	cilinder = max(petitions)
	return cilinder, distance

# --------------    main ---------------------------------

beginning = 0
end = 100
# global direction
direction = 1

text = raw_input("ingrese lista de peticiones \r\n")
current = input("ingrese la posicion inicial del cabezal \r\n")
orderer = input("ingrese 1: C-Look, 2: SSTF, 3: SCAN \r\n")
print current

petitions = text.split("-")

for i in range(len(petitions)):
	petitions[i] = int(petitions[i])

petitions.sort()
order = []
times = []
total_time = 0

# ------ Hasta que las peticiones se acaben
while(petitions):

	
	print petitions

	# Primero se encuentra el mas cercano
	[min_cilinder, min_distance] = getMin(petitions, current, orderer)

	# Luego este se guarda junto con toda la informacion
	current = min_cilinder
	order.append(current)
	times.append(min_distance)
	total_time += min_distance

	print current
	petitions.remove(current)

	if len(petitions) != 0 and orderer != 2:

		if checkBorder(petitions, current):
			if orderer == 1:
				# Esto es C-Look o Scan asi que checkear bordes
				[cilinder, distance] = comeBackClook(petitions, current)
			else:
				direction *= -1
				[cilinder, distance] = comeBackScan(petitions, current)

			current = cilinder
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

