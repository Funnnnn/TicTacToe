print('Hello World!') # Joke
print('Welcome to my Tic Tac Toe game!\n') # Welcome screen
victory = 'none' # Victory status
while victory == "none": # Starting the while loop
	print('Board key:') # Board Key. Will appear after every move
	print('1 2 3') 
	print('4 5 6')
	print('7 8 9\n \n \n')
	var1, var2, var3 = '~', '~', '~' # Initial variable assignment
	var4, var5, var6 = '~', '~', '~'
	var7, var8, var9 = '~', '~', '~'
	print(var1, var2, var3) # First iteration of the empty board
	print(var4, var5, var6)
	print(var7, var8, var9)
	var = input('\nPlease enter your selection:') # Placement selection