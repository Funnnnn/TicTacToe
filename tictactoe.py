print('\n\n\nHello World!')
print('Welcome to my Tic Tac Toe game!\n')
victory = 'none'
def viccheck():
	for ecks in 'XO':
		if (var1 == ecks and var2 == ecks and var3 == ecks or
		var4 == ecks and var5 == ecks and var6 == ecks or
		var7 == ecks and var8 == ecks and var9 == ecks or
		var1 == ecks and var4 == ecks and var7 == ecks or
		var2 == ecks and var5 == ecks and var8 == ecks or
		var3 == ecks and var6 == ecks and var9 == ecks or
		var1 == ecks and var5 == ecks and var9 == ecks or
		var3 == ecks and var5 == ecks and var7 == ecks):
			if ecks == 'X':
				return 'true'
			else:
				return 'false'
	if (var1 != '~' and var2 != '~' and var3 != '~' and
	var4 != '~' and var5 != '~' and var6 != '~' and
	var7 != '~' and var8 != '~' and var9 != '~'):
		return 'tie'
ponzi = ['~'] * 9 # ponzi is the positions on the board
while victory == 'none':
	valid = 'true'
	print('Board key:')
	print('1 | 2 | 3\n--+---+--') 
	print('4 | 5 | 6\n--+---+--')
	print('7 | 8 | 9\n \n \n')
	print(ponzi[1] + ' | ' + ponzi[2] + ' | ' + ponzi[3] + '\n--+---+--')
	print(ponzi[4] + ' | ' + ponzi[5] + ' | ' + ponzi[6] + '\n--+---+--')
	print(ponzi[7] + ' | ' + ponzi[8] + ' | ' + ponzi[9])
	var = input('\nPlease enter your selection :')
	if var == '1':
		if var1 == '~':
			var1 = 'X'
		else:
			print('\nInvalid selection\n\n\n')
			valid = 'false'
	elif var == '2':
		if var2 == '~':
			var2 = 'X'
		else:
			print('\nInvalid selection\n\n\n')
			valid = 'false'
	elif var == '3':
		if var3 == '~':
			var3 = 'X'
		else:
			print('\nInvalid selection\n\n\n')
			valid = 'false'
	elif var == '4':
		if var4 == '~':
			var4 = 'X'
		else:
			print('\nInvalid selection\n\n\n')
			valid = 'false'
	elif var == '5':
		if var5 == '~':
			var5 = 'X'
		else:
			print('\nInvalid selection\n\n\n')
			valid = 'false'
	elif var == '6':
		if var6 == '~':
			var6 = 'X'
		else:
			print('\nInvalid selection\n\n\n')
			valid = 'false'
	elif var == '7':
		if var7 == '~':
			var7 = 'X'
		else:
			print('\nInvalid selection\n\n\n')
			valid = 'false'
	elif var == '8':
		if var8 == '~':
			var8 = 'X'
		else:
			print('\nInvalid selection\n\n\n')
			valid = 'false'
	elif var == '9':
		if var9 == '~':
			var9 = 'X'
		else:
			print('\nInvalid selection\n\n\n')
			valid = 'false'
	elif var == 'pass':
		print('Turn skipped.')
	else:
		print('\nInvalid selection\n\n\n')
		valid = 'false'
	catch = viccheck()
	if catch is not None:
		victory = catch
		break
	if valid == 'true':
		if var1 == '~':
			var1 = 'O'
		elif var2 == '~':
			var2 = 'O'
		elif var3 == '~':
			var3 = 'O'
		elif var4 == '~':
			var4 = 'O'
		elif var5 == '~':
			var5 = 'O'
		elif var6 == '~':
			var6 = 'O'
		elif var7 == '~':
			var7 = 'O'
		elif var8 == '~':
			var8 = 'O'
		elif var9 == '~':
			var9 = 'O'
	catch = viccheck()
	if catch is not None:
		victory = catch
		break
print(ponzi[1] + ' | ' + ponzi[2] + ' | ' + ponzi[3] + '\n--+---+--')
print(ponzi[4] + ' | ' + ponzi[5] + ' | ' + ponzi[6] + '\n--+---+--')
print(ponzi[7] + ' | ' + ponzi[8] + ' | ' + ponzi[9])
if victory == 'true':
	print('\nCongratulations! You win!')
elif victory == 'tie':
	print("\nCat's game!")
else:
	print('\nYou lost. So hard.')