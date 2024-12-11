## Rock paper scissors game ##
## By Seb ##
import random

moves = ['rock', 'paper', 'scissors']

def rps_game(game_int, name):
    print("          <<< NEW GAME >>>")
    computer_moves = random.choice(moves)
    while True:
        user_move = input('What is your move? Rock, paper, or scissors? ')
        user_move_lower = user_move.lower()
        print('       ----------------------')

        if user_move_lower in moves:
            break
        else:
            print('Please input a valid move.')
            print('       ----------------------')

    if user_move_lower == 'rock':
        print(f'{str.capitalize(name)} chose rock. Computer chose {computer_moves}.')
        if computer_moves == 'scissors':
            print('          <<< YOU WIN >>>')
            print('       ----------------------')
            return 'win'
        elif computer_moves == 'rock':
            print('           <<< TIE >>>')
            print('       ----------------------')
            return 'tie'
        else:
            print('         <<< YOU LOSE >>>')
            print('       ----------------------')
            return 'lose'
    elif user_move_lower == 'paper':
        print(f'{str.capitalize(name)} chose paper. Computer chose {computer_moves}.')
        if computer_moves == 'scissors':
            print('         <<< YOU LOSE >>>')
            print('       ----------------------')
            return 'lose'
        elif computer_moves == 'rock':
            print('          <<< YOU WIN >>>')
            print('       ----------------------')
            return 'win'
        else:
            print('           <<< TIE >>>')
            print('       ----------------------')
            return 'tie'
    elif user_move_lower == 'scissors':
        print(f'{str.capitalize(name)} chose scissors. Computer chose {computer_moves}.')
        if computer_moves == 'scissors':
            print('           <<< TIE >>>')
            print('       ----------------------')
            return 'tie'
        elif computer_moves == 'rock':
            print('          <<< YOU LOSE >>>')
            print('       ----------------------')
            return 'lose'
        else:
            print('          <<< YOU WIN >>>')
            print('       ----------------------')
            return 'win'

name = input("What is your name? ")
print('       ----------------------')
print(f'Hello {str.capitalize(name)}. Welcome to Rock, Paper Scissors!')
print('       ----------------------')
print('Choose scissors, paper, or rock by typing in your selection.')
print('The rules are simple: Scissors cuts paper, paper covers rock, and rock crushes scissors.')
print('       ----------------------')
game_int = int(input('How many games do you want to play? '))
score = {'win': 0, 'lose': 0, 'tie': 0}
total_rounds = game_int

if game_int == 0:
    print('       ----------------------')
    print('             Goodbye!')
else:
    for i in range(game_int):
        result = rps_game(game_int, name)
        score[result] += 1

    print('       ----------------------')
    print('         <<< SCOREBOARD >>>')
    print(f'Total Rounds: {total_rounds}')
    print(f'Ties: {score["tie"]}')
    print(f'Wins: {score["win"]}')
    print(f'Loses: {score["lose"]}')
    print('       ----------------------')
    print(f'Win Rate: {score["win"]/total_rounds:.2%}')
    print(f'Lose Rate: {score["lose"]/total_rounds:.2%}')
    print(f'Tie Rate: {score["tie"]/total_rounds:.2%}')