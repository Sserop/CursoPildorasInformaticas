def devuelve_ciudades(*ciudades):
	# Si necesito anidar for, mejor usar yield from
	#for elemento in ciudades:
		#for letra in elemento:
			#yield letra

	# Da el mismo resultado
	for elemento in ciudades:
		yield from elemento

ciudades_devueltas = devuelve_ciudades("Madrid", "Roma", "Paris")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
