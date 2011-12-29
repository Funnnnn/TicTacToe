print('Hello World!')
print('Welcome to my Tic Tac Toe game!\n')
victory = 'none'
var1, var2, var3 = '~', '~', '~'
var4, var5, var6 = '~', '~', '~'
var7, var8, var9 = '~', '~', '~'
while victory == 'none':
	print('Board key:')
	print('1 2 3') 
	print('4 5 6')
	print('7 8 9\n \n \n')
	print(var1, var2, var3)
	print(var4, var5, var6)
	print(var7, var8, var9)
	var = input('\nPlease enter your selection :')
	if var == '1':
		if var1 == '~':
			var1 = 'X'
		else:
			print('\nInvalid selection\n\n\n')
	elif var == '2':
		if var2 == '~':
			var2 = 'X'
		else:
			print('\nInvalid selection\n\n\n')
	elif var == '3':
		if var3 == '~':
			var3 = 'X'
		else:
			print('\nInvalid selection\n\n\n')
	elif var == '4':
		if var4 == '~':
			var4 = 'X'
		else:
			print('\nInvalid selection\n\n\n')
	elif var == '5':
		if var5 == '~':
			var5 = 'X'
		else:
			print('\nInvalid selection\n\n\n')
	elif var == '6':
		if var6 == '~':
			var6 = 'X'
		else:
			print('\nInvalid selection\n\n\n')
	elif var == '7':
		if var7 == '~':
			var7 = 'X'
		else:
			print('\nInvalid selection\n\n\n')
	elif var == '8':
		if var8 == '~':
			var8 = 'X'
		else:
			print('\nInvalid selection\n\n\n')
	elif var == '9':
		if var9 == '~':
			var9 = 'X'
		else:
			print('\nInvalid selection\n\n\n')
	elif var == 'Trevor is amazing':
		victory = 'true'
	elif var == 'Tie game':
		victory = 'tie'
	else:
		print('\nInvalid selection\n\n\n')
	if (var1 == 'X' and var2 == 'X' and var3 == 'X' or
	var4 == 'X' and var5 == 'X' and var6 == 'X' or
	var7 == 'X' and var8 == 'X' and var9 == 'X' or
	var1 == 'X' and var4 == 'X' and var7 == 'X' or
	var2 == 'X' and var5 == 'X' and var8 == 'X' or
	var3 == 'X' and var6 == 'X' and var9 == 'X' or
	var1 == 'X' and var5 == 'X' and var9 == 'X' or
	var3 == 'X' and var5 == 'X' and var7 == 'X'):
		victory = 'true'
print(var1, var2, var3)
print(var4, var5, var6)
print(var7, var8, var9)
if victory == 'true':
	print('\nCongratulations! You win!')
elif victory == 'tie':
	print("\nCat's game!")
else:
	print('\nYou lost. So hard.')