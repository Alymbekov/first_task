for x in range(1,101):
	if x % 3 == 0:
		print('Lolo')
	elif x % 5 == 0:
		print('Pepep') 
	elif x % 3 == 0 or x % 5 == 0:
		print('Lolopepep')
	else:
		print(x)

