# Los generadores son como funciones, pero en vez de usar "return"
# utiliza un "yield". Devuelve valores de uno en uno.

# Sirve por ejemplo para procesar mejores listas infinitas

def generaPares(limite):
	num = 1
	miLista = []

	while num<limite:

		yield num*2
		num = num +1

devuelvePares = generaPares(10)

print(next(devuelvePares)) # Esto generará el primer número
print(next(devuelvePares)) # Esto el segundo
 
# Es más eficiente porque no tiene que generar la lista completa
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]