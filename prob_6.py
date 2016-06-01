
def prob_6(lista):
	longitud = len(lista)
	for x in range(longitud):
		for y in range(x + 1, longitud):
			if lista[x] < lista[y]:
				# Voltear
				temp = lista[y]
				lista[y] = lista[x]
				lista[x] = temp
	return lista

test = [-10, 100, 5, 90, 80 , -9]

print(prob_6(test))