print("Choose a team: Lakers or Celtics")
team1 = input()
team2 = ''

if team1 == 'Lakers':
    team2 = 'Celtics'
elif team1 == 'Celtics':
    team2 = 'Lakers'
else:
    print('Invalid team entered. Please choose either Lakers or Celtics.')
    exit()

print(f'Player 2, choose your team: {team2}')

team1_score = 0
team2_score = 0

print(f'Great! Let\'s get started. {team1} will start with the ball.')

for round in range(3):
    print(f'Round {round+1} starts now!')
    time_remaining = 120
    while time_remaining > 0:
        print(f'Time remaining: {time_remaining} seconds')
        print(f'{team1} score: {team1_score} | {team2} score: {team2_score}')
        print(f'{team1} has the ball.')
        action = input('Choose an action: move or shoot? ')
        if action == 'move':
            direction = input('Choose a direction: up, down, left, or right? ')
            print(f'{team1} moves {direction}.')
        elif action == 'shoot':
            print(f'{team1} shoots the ball!')
            if input('Did it go in? (y/n) ') == 'y':
                print(f'{team1} scores!')
                team1_score += 2
                print(f'{team1} {team1_score} - {team2} {team2_score} {time_remaining}s remaining')
            else:
                print(f'{team2} gets the rebound.')
                print(f'{team1} {team1_score} - {team2} {team2_score} {time_remaining}s remaining')
                print(f'{team2} has the ball.')
                continue
        else:
            print('Invalid action entered. Please choose move or shoot.')
            continue

        print(f'{team2} has the ball.')
        action = input('Choose an action: move or shoot? ')
        if action == 'move':
            direction = input('Choose a direction: up, down, left, or right? ')
            print(f'{team2} moves {direction}.')
        elif action == 'shoot':
            print(f'{team2} shoots the ball!')
            if input('Did it go in? (y/n) ') == 'y':
                print(f'{team2} scores!')
                team2_score += 2
                print(f'{team1} {team1_score} - {team2} {team2_score} {time_remaining}s remaining')
            else:
                print(f'{team1} gets the rebound.')
                print(f'{team1} {team1_score} - {team2} {team2_score} {time_remaining}s remaining')
                print(f'{team1} has the ball.')
                continue
        else:
            print('Invalid action entered. Please choose move or shoot.')
            continue

        print(f'{team1} {team1_score} - {team2} {team2_score} {time_remaining}s remaining')
        time_remaining -= 10

print('The game is over! Let\'s see who won.')
if team1_score > team2_score:
    print(f'{team1} wins! Final score: {team1_score} - {team2_score}')
elif team2_score > team1_score:
    print(f'{team2} wins! Final score: {team2_score} - {team1_score}')
else:
    print('It\'s a tie! Final score: {team1_score} - {team2_score}')

print('Thanks for playing the multiplayer basketball game!')
