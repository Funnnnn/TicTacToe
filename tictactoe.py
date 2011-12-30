print('\n\n\nHello World!')
print('Welcome to my Tic Tac Toe game!\n')
victory = 'none'
def viccheck():
	if (var1 == 'X' and var2 == 'X' and var3 == 'X' or
	var4 == 'X' and var5 == 'X' and var6 == 'X' or
	var7 == 'X' and var8 == 'X' and var9 == 'X' or
	var1 == 'X' and var4 == 'X' and var7 == 'X' or
	var2 == 'X' and var5 == 'X' and var8 == 'X' or
	var3 == 'X' and var6 == 'X' and var9 == 'X' or
	var1 == 'X' and var5 == 'X' and var9 == 'X' or
	var3 == 'X' and var5 == 'X' and var7 == 'X'):
		return 'true'
	if (var1 == 'O' and var2 == 'O' and var3 == 'O' or
	var4 == 'O' and var5 == 'O' and var6 == 'O' or
	var7 == 'O' and var8 == 'O' and var9 == 'O' or
	var1 == 'O' and var4 == 'O' and var7 == 'O' or
	var2 == 'O' and var5 == 'O' and var8 == 'O' or
	var3 == 'O' and var6 == 'O' and var9 == 'O' or
	var1 == 'O' and var5 == 'O' and var9 == 'O' or
	var3 == 'O' and var5 == 'O' and var7 == 'O'):
		return 'false'
	if (var1 != '~' and var2 != '~' and var3 != '~' and
	var4 != '~' and var5 != '~' and var6 != '~' and
	var7 != '~' and var8 != '~' and var9 != '~'):
		return 'tie'
var1, var2, var3, var4, var5, var6, var7, var8, var9 = '~' * 9
while victory == 'none':
	valid = 'true'
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
	elif var == 'pass'
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
print(var1, var2, var3)
print(var4, var5, var6)
print(var7, var8, var9)
if victory == 'true':
	print('\nCongratulations! You win!')
elif victory == 'tie':
	print("\nCat's game!")
else:
	print('\nYou lost. So hard.')