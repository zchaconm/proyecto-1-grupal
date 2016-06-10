def prob_7():
	multiplos = [];

	for x in range (1, 1000):
		if(x % 4 == 0 or x % 7 == 0):
			multiplos.append(x);
	return(multiplos)