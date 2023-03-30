# Realice el juego de piedra papel o tijera contra una Computdaro

from choseOptions import chose_options
from checkRules import checkRules


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

        user_options, computer_options = chose_options()
        computer_winners, user_winners = checkRules(
            user_options, computer_options, user_winners, computer_winners)

    print('* ' * 10)
    if computer_winners > user_winners:
        print('*'*10 + ' ' + 'computador gano')
    elif user_winners > computer_winners:
        print('*'*10 + ' ' + 'Gano el usuario')
    else:
        print('El juago quedo en empate')
        print('* ' * 10)


runGame()
