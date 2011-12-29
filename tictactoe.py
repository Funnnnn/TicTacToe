print('Hello World!') # Joke
print('Welcome to my Tic Tac Toe game!\n') # Welcome screen
victory = 'none' # Victory status
var1, var2, var3 = '~', '~', '~'
var4, var5, var6 = '~', '~', '~'
var7, var8, var9 = '~', '~', '~'
while victory == 'none': # Starting the while loop
	print('Board key:') # Board Key. Will appear after every move
	print('1 2 3') 
	print('4 5 6')
	print('7 8 9\n \n \n')
	print(var1, var2, var3) # First iteration of the empty board
	print(var4, var5, var6)
	print(var7, var8, var9)
	var = input('\nPlease enter your selection :') # Placement selection
	if var == '1':
		if var1 == '~':
			var1 = 'X'
		else:
			print('Invalid selection')
	elif var == '2':
		if var2 == '~':
			var2 = 'X'
		else:
			print('Invalid selection')
	elif var == '3':
		if var3 == '~':
			var3 = 'X'
		else:
			print('Invalid selection')
	elif var == '4':
		if var4 == '~':
			var4 = 'X'
		else:
			print('Invalid selection')
	elif var == '5':
		if var5 == '~':
			var5 = 'X'
		else:
			print('Invalid selection')
	elif var == '6':
		if var6 == '~':
			var6 = 'X'
		else:
			print('Invalid selection')
	elif var == '7':
		if var7 == '~':
			var7 = 'X'
		else:
			print('Invalid selection')
	elif var == '8':
		if var8 == '~':
			var8 = 'X'
		else:
			print('Invalid selection')
	elif var == '9':
		if var9 == '~':
			var9 = 'X'
		else:
			print('Invalid selection')
	elif var == 'Trevor is amazing':
		victory = 'true'
	else:
		print('Invalid selection')
if victory == 'true':
	print('Congratulations! You win!')
else:
	print('You lost. So hard.')