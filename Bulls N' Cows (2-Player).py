import sys
bulls1 = 0
bulls2 = 0
cows2 = 0
cows1 = 0
outputsList = ["  Player 1   PLayer 2"]
## Print empty lines to instantly hide info
def spacer(lines):
    for i in range(lines):
        print('')

player1Number = input(str("Player 1, enter your 4-digit number with no repeated digits: "))
if len(player1Number) != 4:
    print('Player did not input a 4-digit number, try again!')
    sys.exit()
spacer(100)
player2Number = input(str('Player 2, enter your 4-digit number with no repeated digits!: '))
if len(player2Number) != 4:
    print('Player did not input a 4-digit number, try again!')
    sys.exit()
spacer(100)

while bulls1 != 4 and bulls2 != 4:
    bulls1 = 0
    bulls2 = 0
    cows2 = 0
    cows1 = 0

    player1Guess, player2Guess = map(str, input("Input both your guesses (ex. 1234 6789): ").split())
    for i in range(4):
        if player1Guess[i] == player2Number[i]:
            bulls1 += 1
        elif player1Guess[i] in player2Number:
            cows1 += 1

    for i in range(4):
        if player2Guess[i] == player1Number[i]:
            bulls2 += 1
        elif player2Guess[i] in player1Number:
            cows2 += 1

    outputsList.append(f"{player1Guess} {bulls1}B {cows1}C | {player2Guess} {bulls2}B {cows2}C")
    print()
    for row in outputsList:
        print(row)
    print()
    if bulls1 == 4:
        print(f"Player 1 won the game! They guessed the number: {player2Number}")
        break
    if bulls2 == 4:
        print(f"Player 2 won the game! They guessed the number: {player1Number}")
        break

