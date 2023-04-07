# Realice el juego de piedra papel o tijera contra una Computadora

from choseOptions import chose_options
from checkRules import checkRules
from checkWins import checkWins
options = ('piedra', 'papel', 'tijera')


def runGame():
    computer_winners = 0
    user_winners = 0
    rounds = 3

    for i in range(1, rounds+1):
        print('*' * 10)
        print(f'Rounds: {i}')
        print('Mucho Exito!!')
        print('*' * 10)
        # function checking options the user and the computer
        user_options, computer_options = chose_options()
        # validation the rules in the games
        computer_winners, user_winners = checkRules(
            user_options, computer_options, user_winners, computer_winners)
        # check the winners
        checkWins(computer_winners, user_winners)


runGame()
