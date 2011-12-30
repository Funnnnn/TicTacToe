print('\n\n\nHello World!')
print('Welcome to my Tic Tac Toe game!\n')
victory = 'none'
def viccheck():
    for ecks in 'XO':
        if (ponzi[0] == ecks and ponzi[1] == ecks and ponzi[2] == ecks or
            ponzi[3] == ecks and ponzi[4] == ecks and ponzi[5] == ecks or
            ponzi[6] == ecks and ponzi[7] == ecks and ponzi[8] == ecks or
            ponzi[0] == ecks and ponzi[3] == ecks and ponzi[6] == ecks or
            ponzi[1] == ecks and ponzi[4] == ecks and ponzi[7] == ecks or
            ponzi[2] == ecks and ponzi[5] == ecks and ponzi[8] == ecks or
            ponzi[0] == ecks and ponzi[4] == ecks and ponzi[8] == ecks or
            ponzi[2] == ecks and ponzi[4] == ecks and ponzi[6] == ecks):
            if ecks == 'X':
                return 'true'
            else:
                return 'false'
    if (ponzi[0] != '~' and ponzi[1] != '~' and ponzi[2] != '~' and
        ponzi[3] != '~' and ponzi[4] != '~' and ponzi[5] != '~' and
        ponzi[6] != '~' and ponzi[7] != '~' and ponzi[8] != '~'):
        return 'tie'
ponzi = ['~'] * 9 # ponzi is the positions on the board
while victory == 'none':
    valid = 'true'
    print('Board key:')
    print('1 | 2 | 3\n--+---+--') 
    print('4 | 5 | 6\n--+---+--')
    print('7 | 8 | 9\n \n \n')
    print(ponzi[0] + ' | ' + ponzi[1] + ' | ' + ponzi[2] + '\n--+---+--')
    print(ponzi[3] + ' | ' + ponzi[4] + ' | ' + ponzi[5] + '\n--+---+--')
    print(ponzi[6] + ' | ' + ponzi[7] + ' | ' + ponzi[8])
    var = input('\nPlease enter your selection :')
    for i, spot in enumerate(ponzi):
        if var == str(i + 1):
            if spot == '~':
                ponzi[i] = 'X'
            else:
                print('\nInvalid selection\n\n\n')
                valid = 'false'
    if var == 'pass':
        print('Turn skipped.')
    elif var not in '123456789':
        print('\nInvalid selection\n\n\n')
        valid = 'false'
    catch = viccheck()
    if catch is not None:
        victory = catch
        break
    if valid == 'true':
        for i, spot in enumerate(ponzi):
            if spot == '~':
                ponzi[i] = 'O'
                break
    catch = viccheck()
    if catch is not None:
        victory = catch
        break
print(ponzi[0] + ' | ' + ponzi[1] + ' | ' + ponzi[2] + '\n--+---+--')
print(ponzi[3] + ' | ' + ponzi[4] + ' | ' + ponzi[5] + '\n--+---+--')
print(ponzi[6] + ' | ' + ponzi[7] + ' | ' + ponzi[8])
if victory == 'true':
    print('\nCongratulations! You win!')
elif victory == 'tie':
    print("\nCat's game!")
else:
    print('\nYou lost. So hard.')