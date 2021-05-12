"""
Rock - Paper - Scissors
"""
import random

N_GAMES = 3
ai = ''
human = ''
winner = ''
score = 0


def main():
    global N_GAMES, ai, human, winner, score
    print_welcome()
    rockPaperScissors()

def rockPaperScissors():
    global N_GAMES, ai, human, winner, score
    while (N_GAMES > 0):
        aiMove()
        humanMove()
        decideWinner()
        announceResult()
        calcScore()
        N_GAMES -= 1
    print(f"Your Score is {score}")

def aiMove():
    global N_GAMES, ai, human, winner, score
    value = random.randint(1, 3)
    if value == 1:
        ai = 'rock'
    elif value == 2:
        ai = 'paper'
    else:
        ai = 'scissors'

def humanMove():
    global N_GAMES, ai, human, winner, score
    choice = input("What do you play? ")
    human = choice
    if (choice != 'rock' and choice != 'paper' and choice != 'scissors'):
        print('invalid choice!')
        humanMove()

def decideWinner():
    global N_GAMES, ai, human, winner, score
    if ai == human:
        winner = 'tie'
    elif ai == 'rock':
        if human == 'scissors':
            winner = 'ai'
        else:
            winner = 'human'
    elif ai == 'scissors':
        if human == 'paper':
            winner = 'ai'
        else:
            winner = 'human'
    elif ai == 'paper':
        if human == 'rock':
            winner = 'ai'
        else:
            winner = 'human'
    else:
        print('should not get here!')
    

def announceResult():
    global N_GAMES, ai, human, winner, score
    print('The AI plays: ' + ai)
    print('The winner is: ' + winner)
    print('')

def calcScore():
    global N_GAMES, ai, human, winner, score
    if winner == 'human':
        score += 1
    elif winner == 'ai':
        score -= 1

def print_welcome():
    print('Welcome to Rock Paper Scissors')
    print('You will play '+str(N_GAMES)+' games against the AI')
    print('rock beats scissors')
    print('scissors beats paper')
    print('paper beats rock')
    print('----------------------------------------------')
    print('')

if __name__ == '__main__':
    main()