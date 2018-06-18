def ntry(algo):
	try:
		algo()
	except Exception as e:
		print(e)
		input("Tecle enter para continuar")